
# medii
area_mean <- mean(rock[,1])
peri_mean <- mean(rock[,2])
shape_mean <- mean(rock[,3])
perm_mean <- mean(rock[,4])

# varianta
variant <- var(rock)

# quartile
q1 <- IQR(rock[,1])
boxplot(rock[,1],
        main = "area")

q2 <- IQR(rock[,2])
boxplot(rock[,2],
        main = "peri")

q3 <- IQR(rock[,3])
boxplot(rock[,3],
        main = "shape")

q4 <- IQR(rock[,4])
boxplot(rock[,4],
        main = "perm")

# boxplot
boxplot(area ~ perm,
        data = rock,
        xlab = "perm",
        ylab = "area",
        main = "area in functie de perm")