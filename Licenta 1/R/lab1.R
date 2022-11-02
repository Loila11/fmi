# matrice
m = matrix(data = 1:10,
           nrow = 2,
           ncol = 5)

# lista
l <- list(nume = c("Ana", "Betty"), "Rob", cifra = 6, 
          m[1,], matrice = m, lista = list("a", numar = 20, T))

# adaugare elemente
l[[7]] = FALSE
l$d = "element nou"
l[9:10] = c("unu", "doi")

# stergere elemente
l[2] = NULL
l$cifra = NULL
l[5:7] = NULL

# data frame
survey <- data.frame("index" = c(1, 2, 3, 4, 5),
                     "sex" = c("m", "m", "m", "f", "f"),
                     "age" = c(99, 46, 23, 54, 23),
                     stringsAsFactors = FALSE)
View(survey)

# data
data()
mtcars$mpg
mtcars[mtcars$mpg > 25, ]

subset(x = mtcars,
      subset = mpg < 12 &
        cyl > 6,
      select = c(disp, wt))

# afisarea celor mai usoare masini
cars_increasing = rownames(mtcars[order(mtcars$wt),])

# afisarea celor mai grele 10 masini
cars_decreasing = rownames(mtcars[order(mtcars$wt, decreasing = TRUE)
                                  ,])
cars_decreasing[1:10]

# ordonare dupa 2 coloane
mtcars[order(mtcars$cyl, mtcars$wt), 1:6]

# functia merge
stat_course = data.frame(student = c("Ionel", "Maria", "Gigel", 
                                     "Vasile", "Ana"),
                         note_stat = c(9, 8, 5, 7, 9))

alg_course = data.frame(student = c("Maria", "Ana" , "Gigel", 
                                    "Ionel", "Vasile", "Liviu"),
                        note_alg = c(10, 8, 9, 7, 9, 5))

combined_courses = merge(x = stat_course,
                         y = alg_course,
                         by = "student",
                         all = TRUE)

# functia aggregate
aggregate(formula = weight ~ Diet + Time,
          FUN = mean,
          subset = Time >= 4,
          data = ChickWeight)
