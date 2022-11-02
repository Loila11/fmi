# functii

functie.smechera <- function() {
  return (pi^2)
}

f2 <- function(x) {
  1 / (x^2 + 1)
}

f2(1)
x <- 1:40
f2(x)
cbind(x, x) -> m
f2(m)

#solutia mea pt Gamma
gama <- function(a) {
  f3 <- function(x) {
    x^(a-1) * exp(-x)
  }
  integrate(f3, 0, Inf)
}
gama(5)

#solutie Gheorghe
f2 <- function(x, a) {
  x^(a-1) * exp(-x)
}

gama2 <- function(parA) {
  integrate(f2, 0, Inf, a = parA)
}

gama2(5)

#solutie Livia completa
check.integer <- function(x) {
  x == round(x)
}

gama3 <- function(a) {
  if(a == 1) {
    return (1)
  } else if (a == 0.5) {
    return (sqrt(pi))
  } else if (check.integer(a)) {
    return (factorial(a - 1))
  } else if (a > 1) {
    return ((a-1) * gama3(a - 1))
  } else {
    fgama <- function(x) {
      x^(a-1) * exp(-x)
    }
    return (integrate(fgama, 0, Inf))
  }
}

a <- 1:100
(er <- gama3(a) - gamma(a))

#*******************************************************************
x <- 0.3
y <- 0.6
((x+y) == 0.9)
all.equal(x+y, 0.9)
all.equal(1.9999999, 2)
all.equal(1.99999999, 2)
all.equal(900000003, 2)

#*******************************************************************
plot(x = 1:10, # x-coordonate
     y = 1:10, # y-coordinate
     type = "p", # puncte (nu linii)
     main = "Primul grafic",
     xlab = "Axa x",
     ylab = "Axa y",
     xlim = c(0, 11), # Valorile min si max pe axa x
     ylim = c(0, 11), # Valorile min si max pe axa y
     col = "blue", # Culoarea punctelor
     pch = 16, # Tipul simbolului
     cex = 1) # Marimea simbolului