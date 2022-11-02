caracter_de_bordare = ' '


def afis2col(lt, n):
    if not isinstance(lt, list) or not str(n).isdigit():
        raise Exception("GenericArgumentError")
    for t in lt:
        if len(t) != 2:
            raise Exception("ListArgumentError")
        for el in t:
            dist = (n - len(str(el)))
            if dist < 0:
                raise Exception("ColumnDimError")
        for el in t:
            dist = (n - len(str(el)))
            blank = str(dist * caracter_de_bordare)
            print(str(el) + blank, end='')
        print()


def afis3col(lt, n):
    if not isinstance(lt, list) or not str(n).isdigit():
        raise Exception("GenericArgumentError")
    for t in lt:
        if len(t) != 3:
            raise Exception("ListArgumentError")
        for el in t:
            dist = int((n - len(str(el))) / 2)
            if dist < 0:
                raise Exception("ColumnDimError")
        for el in t:
            dist = int((n - len(str(el))) / 2)
            blank = str(dist * caracter_de_bordare)
            print(blank + str(el) + blank, end='|')
        print()
