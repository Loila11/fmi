import afisare

try:
    afisare.afis2col([(2, 3), (45678, 5)], 3)
except Exception as eroare:
    print(eroare)

try:
    afisare.afis2col([(2, 3, 4), (4, 5)], 5)
except Exception as eroare:
    print(eroare)

try:
    afisare.afis2col("ala", "bala")
except Exception as eroare:
    print(eroare)

try:
    afisare.afis2col([(2, 3), (4, 5)], 5)
except Exception as eroare:
    print(eroare)

####################
try:
    afisare.afis3col([(2, 3, 4), (4, 500000, 6)], 3)
except Exception as eroare:
    print(eroare)

try:
    afisare.afis3col([(2, 3, 4), (4, 5, 6, 7)], 5)
except Exception as eroare:
    print(eroare)

try:
    afisare.afis3col([(2, 3, 4), (4, 5, 6)], 'a')
except Exception as eroare:
    print(eroare)

try:
    afisare.afis3col([(2, 3, 4), (4, 5, 6)], 5)
except Exception as eroare:
    print(eroare)
