#Considerati setul de date mtcars. Calculati:
#a) Greutatea medie ?n functie de tipul de transmisie
#b) Greutatea medie ?n functie de num?rul de cilindrii
#c) Consumul mediu ?n functie de num?rul de cilindrii si tipul de 
#transmisie

aggregate(formula = wt ~ am,
          FUN = mean,
          data = mtcars)

aggregate(formula = wt ~ cyl,
          FUN = mean,
          data = mtcars)

aggregate(formula = mpg ~ cyl + am,
          FUN = mean,
          data = mtcars)