sample(1:12, 3)
sample(1:12, 12)
sample(1:12, 30, replace=TRUE)
p <- 0.3
t <- sample(0:1, 10000, replace=TRUE, prob=c(1-p, p))
hist(t)
n0 <- length(t[t == 0]) / 10000
n1 <- length(t[t == 1]) / 10000

sample(c(0, exp(1), pi), 10000, replace=TRUE, prob=c(2, 20, 5))

#repartitia geometrica
nr <- 10000
d <- rgeom(nr, p)
hist(d, nclass=24, ylim=c(0, 20))

g <- dgeom(0:20, p)
plot(0:20, g, col="green")