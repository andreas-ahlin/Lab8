# Syntaxkontroll

from LinkedQFileLab8 import LinkedQ


class Syntaxfel(Exception):
    pass


def readMolekyl(q):
    readAtom(q)
    if q.peek() == ".":
        q.dequeue()
    else:
        readNum(q)


def readAtom(q):
    readBLetter(q)
    readSLetter(q)


def readBLetter(q):
    char = q.dequeue()
    if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        return
    raise Syntaxfel("Saknad stor bokstav vid radslutet " + char)


def readSLetter(q):

    if not q.peek() in '0123456789.':
        q.dequeue()  # Skippar ifall det bara matas in stor bokstav
    return
    # if char in 'abcdefghijklmnopqrstuvwxyz':
    #     return
    # raise Syntaxfel("Saknad liten bokstav vid radslutet " + char)


def readNum(q):
    char = q.dequeue()
    if char in '123456789':  # kollar om det kommer en nolla
        # Om det första siffran är 1 måste den följas av något annat
        if char == '1' and not q.peek() in '0123456789':
            raise Syntaxfel("För litet tal vid radslutet")

        while q.peek() in '0123456789':
            q.dequeue()
        return
    elif char == '.':
        return

    raise Syntaxfel("För litet tal vid radslutet ")


def printQueue(q):
    while not q.isEmpty():
        char = q.dequeue()
        print(char, end=" ")
    print()


def storeMolekyl(molekyl):
    q = LinkedQ()
    molekyl = [*molekyl]
    for char in molekyl:
        q.enqueue(char)
    q.enqueue(".")
    return q


def kollaMolekyl(Molekyl):
    q = storeMolekyl(Molekyl)

    try:
        readMolekyl(q)
        return "Formeln är syntaktiskt korrekt"
    except Syntaxfel as fel:
        resMol = ''
        while q.peek() != '.':
            resMol = resMol+q.dequeue()
        return str(fel) + str(resMol)


def main():
    molekyl = str(input(""))
    while molekyl != '#':
        resultat = kollaMolekyl(molekyl)
        print(resultat)
        molekyl = str(input(""))


if __name__ == "__main__":
    main()
