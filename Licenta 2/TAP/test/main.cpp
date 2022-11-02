#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <sys/stat.h>
#include <errno.h>
#include <signal.h>
#include <dirent.h>
#include <readline/readline.h>
#include <readline/history.h>

const int MAX_LENGTH = 300;
char **command;

void  INThandler(int sig) {
    char  c;
    signal(sig, SIG_IGN);
    for (int i = 0; i < 100; ++i)
        free(command[i]);
    free(command);
    printf ("\nProgramul s-a oprit\n");
    exit(0);
}

void format_input(char *path) {

    while (path[0] == '/' || path[0] == '.') {
        char *aux = (char *) malloc(MAX_LENGTH * sizeof(char));
        strcpy(aux, path + 1);
        strcpy(path, aux);
        free(aux);
    }
    while (path[strlen(path) - 1] == ' ' || path[strlen(path) - 1] == '\n') {
        path[strlen(path) - 1] = NULL;
    }
    while (path[strlen(path) - 1] == '/') {
        path[strlen(path) - 1] = '\0';
    }
}

int file_or_folder_local(const char *path) {
    struct stat path_stat;
    stat(path, &path_stat);
    if (S_ISREG(path_stat.st_mode)) {
        return 0; // FILE
    }
    DIR* dir = opendir(path);
    if (dir) {
        closedir(dir);
        return 1; // FOLDER
    }
    return -1; // NU exista
}

int file_or_folder_dbxcli(char *path) {
    char *comanda = (char *) malloc(MAX_LENGTH * sizeof(char));
    strcpy(comanda , "./dbxcli ls ");
    strcat(comanda, path);
    strcat(comanda, " > /tmp/V.TXT 2>null");
    if (system(comanda)) {
       // printf("%s\n", comanda);
        free(comanda);
        return -1;
    }
    FILE * F = fopen("/tmp/V.TXT", "r");
    char *p = (char *) malloc (MAX_LENGTH * sizeof(char));
    getline(&p, &MAX_LENGTH, F);
    format_input(p);
    int ret;
    if (strcmp(p, path) == 0)
        ret = 0; // FILE
    else ret = 1; //FOLDER
    free(comanda);
    free(p);
    return ret;
}

int find_dest_index(int fin) {
    int idx = fin;
    for (int i = 0; i < fin; i ++) {
        if (command[i][0] != '-') {
            idx = i;
        }
    }
    if (idx != fin) {
        format_input(command[idx]);
    }
    return idx;
}

int find_src_index(int fin) {
    for (int i = 2; i < fin; i ++) {
        if (command[i][0] != '-') {
            format_input(command[i]);
            return i;
        }
    }
    return fin;
}

int run_command(char **command, const char *target) {
    pid_t pid = fork();
    if (pid < 0) {
        return -1;
    }
    else if (pid == 0) {
        if (execv(target, command) < 0 ) {
            perror(NULL);
            return errno;
        }
    }
    else {
        wait(NULL);
        printf("\n");
        return 0;
    }
}

int set_command(char **command, const char *prefix) {
    char *target = (char *) malloc(1000 * sizeof(char));
    strcpy(target, prefix);
    strcat(target, command[0]);

    run_command(command, target);
    free (target);
}

void process_folder_dbxcli(char *path, int dest, char *real_source) {
    format_input(path);
    format_input(real_source);
    char *dest_path = (char *) malloc (MAX_LENGTH * sizeof(char));
    strcpy(dest_path, command[dest]);
    strcat(dest_path, "/");
    char *auxx = (char *) malloc (MAX_LENGTH * sizeof(char));
    strcpy(auxx, strstr(path, real_source));
    strcat(dest_path, auxx);
    free(auxx);

    char *aux = (char *) malloc (MAX_LENGTH * sizeof(char));
    if (file_or_folder_dbxcli(path) == 0) {
        strcpy(aux, "./dbxcli get ");
        strcat(aux, path);
        strcat(aux, " ");
        strcat(aux, dest_path);
    } else {
        strcpy(aux, "mkdir ");
        strcat(aux, dest_path);
    }
    system(aux);

    free(dest_path);
    free(aux);
}

void process_folder_local(char *path, int dest, char *real_source) {
    format_input(path);
    char *dest_path = (char *) malloc (MAX_LENGTH * sizeof(char));
    strcpy(dest_path, command[dest]);
    char *auxx = (char *) malloc (MAX_LENGTH * sizeof(char));
    format_input(real_source);
    strcpy(auxx, strstr(path, real_source) + strlen(real_source));
    strcat(dest_path, auxx);
    free(auxx);
    char *aux = (char *) malloc (MAX_LENGTH * sizeof(char));
    if (file_or_folder_local(path) == 0) {
        strcpy(aux, "./dbxcli put ");
        strcat(aux, path);
        strcat(aux, " ");
        strcat(aux, dest_path);
    } else {
        strcpy(aux, "./dbxcli mkdir ");
        strcat(aux, dest_path);
    }
    system(aux);

    free(dest_path);
    free(aux);
}

void write_ls(int length, char *p) {
    for (int i = 2; i < length; ++i) {
        strcat(p, command[i]);
        strcat(p, " ");
    }
    strcat(p, " > /tmp/W.TXT");
    system(p);
}

void put_local_ls(int dest, char *real_source) {
    FILE * F = fopen("/tmp/W.TXT", "r");
    char *path = (char *) malloc (MAX_LENGTH * sizeof(char));
    char *p = (char *) malloc (MAX_LENGTH * sizeof(char));
    char *full_path = (char *) malloc (MAX_LENGTH * sizeof(char));
    while (getline(&p, &MAX_LENGTH, F) > 0)  {

        format_input(p);
        if (strlen(p) == 0) continue; // linia goala dintre 2 foldere distincte
        if (p[strlen(p) - 1] == ':') { // daca e folder
            p[strlen(p) - 1] = '\0';
            strcpy(path, p);
            continue;
        }
        strcpy(full_path, path);
        strcat(full_path, "/");
        strcat(full_path, p);
        process_folder_local(full_path, dest, real_source);
    }
   free(path);
   free(p);
   free(full_path);
}

void local_ls() {
    FILE * F = fopen("/tmp/W.TXT", "r");
    char *p = (char *) malloc (MAX_LENGTH * sizeof(char));
    while (getline(&p, &MAX_LENGTH, F) > 0) {
        printf("%s", p);
    }
    fclose(F);
    free(p);
}

void dbxcli_ls(int dest, char *real_source) {
    FILE * F = fopen("/tmp/W.TXT", "r");
    char *p = (char *) malloc (MAX_LENGTH * sizeof(char));
    char *buffer = (char *) malloc (MAX_LENGTH * sizeof(char));
    while (getline(&p, &MAX_LENGTH, F) > 0) {
        //p[strlen(p) - 1] = '\0';
        format_input(p);
        char *aux1 = p - 1;
        while (aux1 + 1 != NULL) {
            char *aux2 = strstr(aux1 + 1, " /");
            if (aux2 == NULL) {
                if (aux1[1] != '\0') {
                    if (dest == 0) {
                        printf("%s\n", aux1 + 1);
                    } else {
                        process_folder_dbxcli(aux1 + 1, dest, real_source);
                    }
                }
                break;
            }
            strncpy (buffer, aux1 + 1, aux2 - aux1 - 1);
            buffer[aux2 - aux1 -1] = '\0';
            if (buffer[0] != '\0') {
                if (dest == 0) {
                    printf("%s\n", buffer);
                } else {
                   process_folder_dbxcli(buffer, dest, real_source);
                }
            }
            aux1 = aux2;
        }
        if (feof(F)) break;
    }
    fclose(F);
    free(p);
    free(buffer);
}

int main() {
    // Expun functionalitatile utilitarului dbxcli
    command = (char **) malloc (100 * sizeof(char*));
    for (int i = 0; i < 100; ++i)
        command[i] = (char *) malloc (MAX_LENGTH * sizeof(char));
    signal(SIGINT, INThandler);

    //rl_bind_key('\t', rl_complete);
    strcpy(command[0], "./dbxcli");
    strcpy(command[1], "help");
    free(command[2]);
    command[2] = NULL;
    set_command(command, ".");
    command[2] = (char *) malloc (MAX_LENGTH * sizeof(char));
    printf("Add \"l\" before any local commands\n");
    printf("Use \"exit\" to stop the program\n\n");
    // Rulez comenzile
    char *shell_prompt[100];
    snprintf(shell_prompt, sizeof(shell_prompt), "%s:%s $ ", getenv("USER"), getcwd(NULL, 1024));
    while(1) {
        unsigned long int buff_size = 1000;
        char *s = readline(shell_prompt);
        add_history(s);
        unsigned long int length = 1;
        char *p = strtok(s, " \n");
        while (p != NULL) {
            strcpy(command[length], p);
            ++length;
            p = strtok(NULL, "  \n");
        }
        free(command[length]);
        command[length] = NULL;

        if (strcmp(command[1], "exit") == 0) {
            break;
        }

        int dest = find_dest_index(length);
        p = (char*) malloc(MAX_LENGTH * sizeof(char));

        if (strcmp(command[1], "ls") == 0) {
            strcpy(p, "./dbxcli ls ");
            write_ls(length, p);
            dbxcli_ls(0, NULL);
        } else if (strcmp(command[1], "lls") == 0) {
            strcpy(p, "ls ");
            write_ls(length, p);
            local_ls();
        } else if (command[1][0] == 'l' && strcmp(command[1], "logout") != 0) {
            char *aux = (char*) malloc(MAX_LENGTH * sizeof(char));
            strcpy (aux, command[1] + 1);
            strcpy(command[1], aux);
            set_command(command + 1, "/bin/");
            free(aux);
        } else if(strcmp(command[1], "get") == 0) {
            int src = find_src_index(length);
            int dest_type = file_or_folder_local(command[dest]);
            int src_type = file_or_folder_dbxcli(command[src]);

            if (dest_type == 0) {
                printf("Error: File already exists!\n");
            } else {
                if (src_type == -1) {
                    printf("Error: Source doesn't exist\n");
                } else {
                    if (src_type == 0) {
                        set_command(command, ".");
                    } else {
                        // Sursa e folder si destinatia e buna
                        char *aux = (char*) malloc(MAX_LENGTH * sizeof(char));
                        strcpy(aux, "./dbxcli ls -R ");
                        strcat(aux, command[src]);
                        strcat(aux, " > /tmp/W.TXT");
                        system(aux);
                        free(aux);
                        char *p = strrchr(command[src], '/');
                        if (p == NULL) p = command[src];
                        dbxcli_ls(dest, p);
                    }
                }
            }
        } else if(strcmp(command[1], "put") == 0) {
            int src = find_src_index(length);
            int dest_type = file_or_folder_dbxcli(command[dest]);
            int src_type = file_or_folder_local(command[src]);

            if (dest_type == 1) {
                char *p = strrchr(command[src], '/');
                if (p == NULL) {
                    strcat(command[dest], "/");
                    strcat(command[dest], command[src]);
                }
                else
                    strcat(command[dest], p);
            }
            dest_type = file_or_folder_dbxcli(command[dest]);

            if (dest_type == 0) {
                printf("Error: File already exists\n");
            } else {
                if (src_type == -1) {
                    printf("Error: Source doesn't exist\n");
                } else {
                    if (src_type == 0) {
                        set_command(command, ".");
                    } else {
                        // Sursa e folder si destinatia e buna
                        char *aux = (char*) malloc(MAX_LENGTH * sizeof(char));
                        strcpy(aux, "ls -R ");
                        strcat(aux, command[src]);
                        strcat(aux, " > /tmp/W.TXT");
                        system(aux);
                        free(aux);
                        char *p = strrchr(command[src], '/');
                        if (p == NULL) p = command[src];
                        put_local_ls(dest, p);
                    }
                }
            }
        }
        else {
            set_command(command, ".");
        }

        command[length] = (char *) malloc (MAX_LENGTH * sizeof(char));
        free(s);
    }

    for (int i = 0; i < 100; ++i)
        free(command[i]);
    free(command);
    return 0;
}
