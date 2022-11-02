# Sã presupunem cã Jack Sparrow este convins cã poate prezice cât aur 
# va gãsi pe o insulã folosind urmãtoarea ecuatie: ab - 324c + log(a), 
# unde a este aria insulei (în m2), b este numãrul de copaci de pe 
# insulã iar c reprezintã cât de beat este pe o scalã de la 1 la 10. 
#Creati o functie numitã Jacks.Money care primeste ca argumente a, b 
# si c si întoarce valoare prezisã.

Jacks.Money <- function(a, b, c) {
  rez = a*b - 324*c + log(a) 
}