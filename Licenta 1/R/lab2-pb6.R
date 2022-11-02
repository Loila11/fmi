# Folosind setul de date ChickWeight afisati, cu ajutorul functiei 
# barplot, greutatea medie a gãinilor în raport cu numãrul de zile 
# de la nastere.

weight_age = aggregate(
                formula = weight ~ Time,
                data = ChickWeight,
                FUN = mean
              )

barplot(
  height=weight_age$weight,
  names.arg=weight_age$Time,
  main="Greutatea medie a gainilor in raport cu 
  numarul de zile de la nastere",
  xlab="Varsta",
  ylab="Greutate"
)