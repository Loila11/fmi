# creez un tabel de rentz
players_table <- function(x, games, players) {
  matrix (data = 0, nrow = 7, ncol = x, 
             dimnames = list(games, players))
}

games <- c("1. K rosu", "2. Dame", "3. Romburi", "4. Rentz", 
           "5. Totale +", "6. Totale -", "7. Scor")
players <- c("Lorena","Miruna", "Mami")

m <- players_table(3, games, players)

Lorena <- function(scor) {
  m[7, 1] = m[7, 1] + scor
}

m[3, 1] = 2
Lorena(scor = 150)
(m)
