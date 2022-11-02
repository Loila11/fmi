#Considerati setul de date mtcars. Calculati:
#a) Greutatea medie în functie de tipul de transmisie
#b) Greutatea medie în functie de numãrul de cilindrii
#c) Consumul mediu în functie de numãrul de cilindrii si tipul de 
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