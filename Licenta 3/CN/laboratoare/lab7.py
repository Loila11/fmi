import numpy as np


# ======================================================================================================================
# Metoda substitutiei ascendente.
# ======================================================================================================================
def subs_asc(a, b):
    """ (Optional) Verifica daca matricea este patratica + compatibilitatea cu vectorul b. """
    assert a.shape[0] == a.shape[1], 'Matricea introduse nu este patratica!'
    assert a.shape[0] == b.shape[0], 'Matricea introdusa si vectorul b nu se potrivesc!'

    """ Initializarea vectorului solutiei numerice. """
    n = b.shape[0]
    x_num = np.zeros(shape=n)

    """ Determinarea solutiei numerice. """
    x_num[0] = b[0] / a[0, 0]  # Scrie prima componenta a solutiei
    for k in range(1, n):
        s = np.dot(a[k, :k], x_num[:k])
        x_num[k] = (b[k] - s) / a[k, k]

    return x_num


def subs_desc_fast(a, b):
    ''' (Opțional) Verifică dacă matricea este patratică + compatibilitatea cu vectorul 0. '''

    assert a.shape[0] == a.shape[1], 'Matricea introdusă nu este pătratică.'
    assert a.shape[0] == b.shape[0], 'Matricea introdusă și vectorul b nu se potrivesc.'

    ''' Inițializarea vectorului soluției numerice. '''

    n = b.shape[0] - 1
    x_num = np.zeros(shape=n + 1)

    ''' Determinarea soluției numerice. '''
    x_num[n] = b[n] / a[n, n]  # Scrie ultima componentă a soluției

    for k in range(n - 1, -1, -1):
        s = np.dot(a[k, k + 1:], x_num[k + 1:])

        x_num[k] = (b[k] - s) / a[k, k]

    return x_num


def subs_asc_fast(a, b):
    ''' (Opțional) Verifică dacă matricea este patratică + compatibilitatea cu vectorul 0. '''

    assert a.shape[0] == a.shape[1], 'Matricea introdusă nu este pătratică.'
    assert a.shape[0] == b.shape[0], 'Matricea introdusă și vectorul b nu se potrivesc.'

    ''' Inițializarea vectorului soluției numerice. '''

    n = b.shape[0] - 1
    x_num = np.zeros(shape=n + 1)

    ''' Determinarea soluției numerice. '''
    x_num[0] = b[0] / a[0, 0]  # Scrie ultima componentă a soluției

    for k in range(1, n + 1):
        s = np.dot(a[k, :k], x_num[:k])

        x_num[k] = (b[k] - s) / a[k, k]

    return x_num


def fact_lu_meg_part(a, b):
    ''' (Opțional) Verifică dacă matricea este patratică + compatibilitatea cu vectorul 0. '''

    assert a.shape[0] == a.shape[1], 'Matricea introdusă nu este pătratică.'
    assert a.shape[0] == b.shape[0], 'Matricea introdusă și vectorul b nu se potrivesc.'

    n = b.shape[0] - 1  # Cu '1' mai puțin pentru că în numpy plecăm de la 0

    w = np.array(range(n + 1))  # retinem pozitiile liniilor după interschimbare
    L = np.identity(n + 1)  # inițializăm matricea inferior trunghiulară cu matricea identitate
    U = np.array(a)  # inițializăm matricea superior trunghiulară cu matricea sistemului

    for k in range(n):
        ''' Aflăm poziția pivotului de pe coloana k + compatibilitate sistem'''
        if not U[k:, k].any():  # Verifică dacă sunt zero-uri în vectorul de sub pivot (inclusiv)
            raise AssertionError('Sistem incompatibil sau sistem compatibil nedeterminat.')
        else:
            p = np.argmax(np.abs(U[k:, k]))  # Poziția primului element cu valoarea absoluta cea mai mare
            p += k

        ''' Schimbă linia 'k' cu 'p' dacă pivotul nu se află pe diagonala principală. '''
        if k != p:
            U[[p, k], :] = U[[k, p], :]
            w[[p, k]] = w[[k, p]]
            if k > 0:
                L[[k, p], :k] = L[[p, k], :k]

        ''' Zero pe coloana sub poziția pivotului. '''
        for j in range(k + 1, n + 1):  # k + 1, k + 2, ..., n - 1, n
            m = U[j, k] / U[k, k]
            L[j, k] = m
            U[j, :] -= m * U[k, :]

    ''' Verificare de compatibilitate '''
    if U[n, n] == 0:
        raise AssertionError('Sistem incompatibil sau sistem compatibil nedeterminat.')

    ''' Schimbăm pozițiile elementelor din b pentru a corespunde cu indicii din w.'''
    b_new = np.array(b[w])
    # print(L)
    # print(U)
    # print(b)

    ''' Găsește soluția folosind metoda substituției ascendente pentru L * y_num = b.'''
    y_num = subs_asc_fast(L, b_new)

    ''' Găsește soluția folosind metoda substituției descendente pentru U * x_num = y_num.'''
    x_num = subs_desc_fast(U, y_num)

    # print(y_num)

    return x_num


# TODO: Pentru o matrice A ca input returneaza L, P si U

def main():
    A = np.array([
        [0., -10., -3., -10.],
        [7., 7., -9., 3.],
        [-2., -3., -8., 1.],
        [-1., -8., -5., -2.]
    ])

    b = np.array([-161., 38., -76., -104.])

    print('Soluție: {}'.format(fact_lu_meg_part(A, b)))
    print('Verificare: {}'.format(np.matmul(A, fact_lu_meg_part(A, b))))


if __name__ == "__main__":
    main()
