# Considerãm urmãtoarea functie g : R › R, g(x) = 
# sin(x)^2 * log(x), x > 0
# sin(x)^2 * x, x ??? 0

# a) Definiti functia folosind comenzile if-else si Vectorize(???) 
r1 <- function(x) {
  sin(x) * sin(x) * log(x)
}

r2 <- function(x) {
  sin(x) * sin(x) * x
}

g <- function(x) {
  if (x > 0) {
    rez <- r1(x)
  } else {
    rez <- r2(x)
  }
  rez
}

# iar apoi folosind comanda ifelse
g <- function(x) {
  rez <- ifelse(x > 0, r1(x), r2(x))
}

# b) Trasati graficul curbei pe intervalul [-??, ??].
x <- -pi:pi
y <- vector()
for (i in -pi:pi) {
  y <- c(y, g(i))
}
plot(x, y, type = "l")