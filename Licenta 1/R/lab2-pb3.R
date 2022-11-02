# Scrieti un program, folosind bucle de tip while, care sã permitã 
# calcularea radicalului numãrului a ??? N plecând de la relatia de 
# recurentã: 2x[n+1] = x[n] + a/x[n], x1 = a / 2

radical <- function(a) {
  x <- a / 2
  while (abs(x^2 - a) > 1e-10) {
    x <- (x + a / x) / 2
  }
  x
}

(radical(9))