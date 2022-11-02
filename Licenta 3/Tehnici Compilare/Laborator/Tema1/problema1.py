
class Automata:
    def __init__(self, input_file):
        file = open(input_file, "r")
        self.Q = file.readline().split()
        self.Vi = file.readline().split()
        self.Ve = file.readline().split()
        self.s = file.readline().split()[0]
        self.F = file.readline().split()

        self.T = {}
        for line in file:
            t = line.split()
            if (t[0], t[1]) in self.T.keys():
                self.T[(t[0], t[1])].append((t[2], t[3]))
            else:
                self.T[(t[0], t[1])] = [(t[2], t[3])]

        file.close()


def LNFA(automata, state, inputString, outputString, visited):
    if (state, inputString, outputString) in visited:
        return
    visited.add((state, inputString, outputString))

    if (state, '.') in automata.T.keys():
        for nextState in automata.T[state, '.']:
            nextOutput = outputString
            if nextState[1] != '.':
                nextOutput += nextState[1]

            LNFA(automata, nextState[0], inputString, nextOutput, visited)

    if not inputString:
        if state in automata.F:
            print(outputString)
        return

    if (state, inputString[0]) in automata.T.keys():
        for nextState in automata.T[state, inputString[0]]:
            nextOutput = outputString
            if nextState[1] != '.':
                nextOutput += nextState[1]

            LNFA(automata, nextState[0], inputString[1:], nextOutput, visited)


def main():
    automata = Automata("automat.txt")
    while True:
        inputString = input("Sirul de intrare:\n")
        print(f"Sirurile de iesire:")
        LNFA(automata, automata.s, inputString, '', set())
        if inputString == "exit":
            break


if __name__ == "__main__":
    main()
