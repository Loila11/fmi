n <- 3
p <- 0.1
k <- 1

combin <- function(n, k) {
  (factorial(n) / factorial(k)) / factorial(n - k)
}

pbernoulli <- function(n, k, p) {
  combin(n, k) * p^k * (1 - p) ^ (n - k)
}

fbernoulli <- function(n, k, p) {
  sol <- 0
  for (i in 0:k) {
    sol <- sol + pbernoulli(n, i, p)
  }
  return (sol)
}

ppoisson <- function(x, k) {
  x^k * exp(-x) / factorial(k)
}

fpoisson <- function(x, k) {
  sol <- 0
  for (i in 0:k) {
    sol <- sol + ppoisson(x, i)
  }
  return (sol)
}

phiper <- function(n, n1, m, k) {
  combin(n1, k) * combin(n - n1, m - k) / combin(n, m)
}

fhyper <- function(n, n1, m, k) {
  sol <- 0
  for (i in 0:k) {
    sol <- sol + phiper(n, n1, m, i)
  }
  return (sol)
}

pgeom <- function(p, k) {
  (1 - p)^k * p
}

fgeom <- function(p, k) {
  sol <- 0
  for (i in 0:k) {
    sol <- sol + pgeom(p, i)
  }
  return (sol)
}
