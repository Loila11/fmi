# Construiti urmãtoarele matrice de dimensiune 10 × 10: ... .
# Puteti construi matricea M si matricea N fãrã a folosi bucle for? 
# (Hint: ce face comanda outer?)

# cu for:
m <- matrix(nrow = 10, ncol = 10)
for (i in 1:10) {
  for (j in 1:10) {
    m[i, j] = 1 / sqrt(abs(i - j) + 1)
  }
}

n <- matrix(nrow = 10, ncol = 10)
for (i in 1:10) {
  for (j in 1:10) {
    n[i, j] = i / (j * j)
  }
}

# fara for:
m <- 1 / sqrt(abs(outer(1:10, 1:10, FUN="-")) + 1)
n <- outer(1:10, outer(1:10, 2, FUN="^"), FUN="/")