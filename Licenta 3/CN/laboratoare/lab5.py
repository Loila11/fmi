import numpy as np


# ======================================================================================================================
# Metoda substitutiei descendente, functionala, dar nu rapida.
# ======================================================================================================================

def subs_desc_slow(a, b):
    """ (Optional) Verifica daca matricea este patratica + compatibilitatea cu vectorul b. """
    assert a.shape[0] == a.shape[1], 'Matricea introduse nu este patratica!'
    assert a.shape[0] == b.shape[0], 'Matricea introdusa si vectorul b nu se potrivesc!'

    """ Initializarea vectorului solutiei numerice. """
    n = b.shape[0] - 1
    x_num = np.zeros(shape=n+1)

    """ Determinarea solutiei numerice. """
    x_num[n] = b[n] / a[n, n]  # Scrie ultima componenta a solutiei
    for k in range(n-1, -1, -1):
        s = 0.
        for j in range(k+1, n+1, 1):  # Gaseseste s-ul corespunzator fiecarei componente x[k]
            s += a[k, j] * x_num[j]

        x_num[k] = (b[k] - s) / a[k, k]

    return x_num


# ======================================================================================================================
# Metoda substitutiei descendente, mai rapida.
# ======================================================================================================================
def subs_desc_fast(a, b):
    """ (Optional) Verifica daca matricea este patratica + compatibilitatea cu vectorul b. """
    assert a.shape[0] == a.shape[1], 'Matricea introduse nu este patratica!'
    assert a.shape[0] == b.shape[0], 'Matricea introdusa si vectorul b nu se potrivesc!'

    """ Initializarea vectorului solutiei numerice. """
    n = b.shape[0] - 1
    x_num = np.zeros(shape=n+1)

    """ Determinarea solutiei numerice. """
    x_num[n] = b[n] / a[n, n]  # Scrie ultima componenta a solutiei
    for k in range(n-1, -1, -1):
        s = np.dot(a[k, k+1:], x_num[k+1:])
        x_num[k] = (b[k] - s) / a[k, k]

    return x_num


# ======================================================================================================================
# Metoda de eliminare Gauss fara pivotare.
# ======================================================================================================================
def meg_fara_pivotare(a, b):
    """ (Optional) Verifica daca matricea este patratica + compatibilitatea cu vectorul b. """
    assert a.shape[0] == a.shape[1], 'Matricea introduse nu este patratica!'
    assert a.shape[0] == b.shape[0], 'Matricea introdusa si vectorul b nu se potrivesc!'
    a_ext = np.concatenate((a, b[:, None]), axis=1)

    n = a.shape[0] - 1  # Cu '1' mai putin pentru ca in numpy plecam de la 0

    for k in range(n):
        """Aflam pozitia pivotului de pe colona k + compatibilitate sistem. """
        if not a_ext[k:, k].any():  # Verifica daca sunt zero-uri in vectorul de sub pivot (inclusiv)
            raise AssertionError('Sistem incompatibil sau sistem compatibil nedeterminat')
        else:
            p = np.argmin(a_ext[k:, k] == 0)  # Pozitia primului element nenul
            p += k  # Q: Ce dimensiune are vectorul in care cautam?

        """ Schimba linia 'k' cu 'p' daca pivotul nu se afla pe diagonala principala. """
        if k != p:
            a_ext[[p, k], :] = a_ext[[k, p], :]

        """ Zero pe coloana sub pozitia pivotului. """
        for j in range(k+1, n+1):  # k+1, k+2, ..., n-1, n
            m = a_ext[j, k] / a_ext[k, k]
            a_ext[j, :] -= m * a_ext[k, :]

    """ Verificare de compatibilitate"""
    if a_ext[n, n] == 0:
        raise AssertionError('Sistem incompatibil sau sistem compatibil nedeterminat')

    """ Gaseste solutia folosind metoda substitutiei descendente. """
    x_num = subs_desc_fast(a_ext[:, :-1], a_ext[:, -1])

    return x_num


# ======================================================================================================================
# Metoda de eliminare Gauss cu pivotare partiala.
# ======================================================================================================================
def meg_pivotare_partiala(a, b):
    """ (Optional) Verifica daca matricea este patratica + compatibilitatea cu vectorul b. """
    assert a.shape[0] == a.shape[1], 'Matricea introduse nu este patratica!'
    assert a.shape[0] == b.shape[0], 'Matricea introdusa si vectorul b nu se potrivesc!'
    a_ext = np.concatenate((a, b[:, None]), axis=1)

    n = a.shape[0] - 1  # Cu '1' mai putin pentru ca in numpy plecam de la 0

    for k in range(n):
        """Aflam pozitia pivotului de pe colona k + compatibilitate sistem. """
        if not a_ext[k:, k].any():  # Verifica daca sunt zero-uri in vectorul de sub pivot (inclusiv)
            raise AssertionError('Sistem incompatibil sau sistem compatibil nedeterminat')
        else:
            p = np.argmax(np.abs(a_ext[k:, k]))  # Pozitia primului element nenul
            p += k  # Q: Ce dimensiune are vectorul in care cautam?

        """ Schimba linia 'k' cu 'p' daca pivotul nu se afla pe diagonala principala. """
        if k != p:
            a_ext[[p, k], :] = a_ext[[k, p], :]

        """ Zero pe coloana sub pozitia pivotului. """
        for j in range(k+1, n+1):  # k+1, k+2, ..., n-1, n
            m = a_ext[j, k] / a_ext[k, k]
            a_ext[j, :] -= m * a_ext[k, :]

    """ Verificare de compatibilitate"""
    if a_ext[n, n] == 0:
        raise AssertionError('Sistem incompatibil sau sistem compatibil nedeterminat')

    """ Gaseste solutia folosind metoda substitutiei descendente. """
    x_num = subs_desc_fast(a_ext[:, :-1], a_ext[:, -1])

    return x_num


# ======================================================================================================================
# Calculul inversei
# ======================================================================================================================
def calculeaza_inversa(a):
    """ Initializeaza o matrice pentru stocarea solutiei -> O sa fie inversa """
    inversa = np.zeros_like(a)

    """ Genereaza matricea de vectori din dreapta egalului cu matricea identitate """
    n = a.shape[0]
    ident = np.eye(n)

    """ Afla fiecare vector coloana din inversa folosind una dintre metodele de eliminare Gauss """
    for i in range(n):
        inversa[:, i] = meg_pivotare_partiala(a, ident[:, i])

    """ Returneaza inversa """
    return inversa


# ======================================================================================================================
# Date
# ======================================================================================================================
def main():
    A = np.array([
        [1., 2., 3.],
        [0., 1., 2.],
        [0., 0., 2.]
    ])

    x_sol = np.array([1., 1., 1.])

    b_ = np.matmul(A, x_sol)

    # subs_desc_slow(A, b_)
    # subs_desc_fast(A, b_)

    A_gauss = np.array([
        [2., 3., 0.],
        [3., 4., 2.],
        [1., 3., 1.]
    ])

    x_gauss = np.array([1., 2., 3.])
    b_gauss = np.matmul(A_gauss, x_gauss)

    # meg_fara_pivotare(A_gauss, b_gauss)


    # Solutia corecta este [1. 1.]
    eps = 10**(-20)  # 1e-20
    a_test = np.array([
        [eps, 1.],
        [1., 1.]
    ])

    b_test = np.array([1., 2.])

    x_sol_test = meg_fara_pivotare(a_test, b_test)
    # print(x_sol_test)

    b = np.array([
        [0., -9., -8., 9.],
        [8., 2., -6., 8.],
        [3., -3., -10., -7.],
        [9., -2., -10., 7.]
    ])

    x = calculeaza_inversa(b)
    print(x)
    # print(np.dot(b, x))


if __name__ == '__main__':
    main()
