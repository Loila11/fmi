# S? presupunem c? Jack Sparrow este convins c? poate prezice c?t aur 
# va g?si pe o insul? folosind urm?toarea ecuatie: ab - 324c + log(a), 
# unde a este aria insulei (?n m2), b este num?rul de copaci de pe 
# insul? iar c reprezint? c?t de beat este pe o scal? de la 1 la 10. 
#Creati o functie numit? Jacks.Money care primeste ca argumente a, b 
# si c si ?ntoarce valoare prezis?.

Jacks.Money <- function(a, b, c) {
  rez = a*b - 324*c + log(a) 
}