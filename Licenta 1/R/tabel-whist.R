#creez un tabel de whist 
games <- function(x) {
  c(rep(c(1), x), 2:7, rep(c(8), x), 7:2, rep(c(1), x))
}

players_table <- function(x, players) {
  matrix (data = 0, nrow = length(games(x)), ncol = x,
             dimnames = list(games(x), players))
}
players <- c("Lorena","Miruna", "Mami")

w <- players_table(3, players)
(w)
