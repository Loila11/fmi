START_SYMBOL = '$'
LAMBDA = '_'
END_SYMBOL = '#'


class Production:
    def __init__(self, id, left, right):
        self.id = id
        self.left = left
        self.right = right

    def __repr__(self):
        res = "_" if self.right == "" else self.right
        return str(self.id) + ": " + str(self.left) + "->" + res


class LR0Item:
    def __init__(self, prodId, left, leftDot, rightDot):
        self.prodId = prodId
        self.left = left
        self.leftDot = leftDot
        self.rightDot = rightDot

    def __repr__(self):
        return str(self.prodId) + " " + self.left + "->" + self.leftDot + "." + self.rightDot

    def __eq__(self, o):
        return self.prodId == o.prodId and self.left == o.left and self.leftDot == o.leftDot and self.rightDot == o.rightDot

    def __hash__(self):
        return hash((self.prodId, self.left, self.leftDot, self.rightDot))


class Action:
    def __init__(self, id=-1, type="ERROR"):
        self.id = id
        self.type = type

    def __repr__(self):
        if self.type == "SHIFT":
            return "shift " + str(self.id)
        elif self.type == "REDUCE":
            return "reduce " + str(self.id)
        elif self.type == "ACCEPT":
            return "accept"
        else:
            return "ERROR"


n = 0
S = '#'
allProds = []
terminals = set()
nonterminals = set()

prod = {}
first = {}
follow = {}

stateToId = {}
idToState = {}

transition = {}
actionTable = {}
gotoTable = {}


def isNonTerminal(ch):
    return ord('A') <= ord(ch) <= ord('Z') or ch == START_SYMBOL


def isTerminal(ch):
    return not isNonTerminal(ch)


def hasNonTerminal(str):
    for ch in str:
        if isNonTerminal(ch):
            return True
    return False


def buildTerms(str):
    for ch in str:
        if isTerminal(ch):
            terminals.add(ch)
        else:
            nonterminals.add(ch)


def mergeSets(seta: set, setb: set) -> bool:
    result = False
    for elem in setb:
        if elem not in seta:
            seta.add(elem)
            result = True
    return result


def getFirst(str, fncOfLast):
    res = set()
    nullable = True
    i = 0
    for ch in str:
        currSet = set()
        if i < len(str) - 1:
            if ch in first:
                currSet = first[ch]
        else:
            if ch in fncOfLast:
                currSet = fncOfLast[ch]

        for s in currSet:
            if s != "":
                res.add(s)

        if "" not in currSet:
            nullable = False
            break

        i += 1
    if nullable:
        res.add("")
    return res


def buildFirst():
    for ch in terminals:
        if ch not in first:
            first[ch] = set([])
        first[ch].add(str(ch))

    for p in allProds:
        if not hasNonTerminal(p.right):
            if p.left not in first:
                first[p.left] = set([])
            first[p.left].add(p.right[:1])

    running = True
    while running:
        running = False
        for p in allProds:
            if not hasNonTerminal(p.right):
                continue
            aux = getFirst(p.right, first)

            if p.left not in first:
                first[p.left] = set()
            if mergeSets(first[p.left], aux):
                running = True


def buildFollow():
    follow[S] = set()
    follow[S].add(str(END_SYMBOL))

    running = True
    while running:
        running = False
        for p in allProds:
            for i, ch in enumerate(p.right):
                if isNonTerminal(ch):
                    suff = p.right[i + 1:]
                    aux = getFirst(suff + str(p.left), follow)
                    if ch not in follow:
                        follow[ch] = set()
                    if mergeSets(follow[ch], aux):
                        running = True


def getClosure(s: set):
    que = []
    res = set()
    mergeSets(res, s)

    for it in s:
        que.append(it)

    while len(que) > 0:
        nod = que[0]
        que.pop(0)

        if nod.rightDot == "":
            continue

        ch = nod.rightDot[0]
        if isNonTerminal(ch):
            for p in prod[ch]:
                item = LR0Item(p.id, p.left, "", p.right)
                if item not in res:
                    res.add(item)
                    que.append(item)

    return res


def getNextState(state, ch):
    nxt = set()
    for it in state:
        if it.rightDot[0:1] == str(ch):
            newIt = LR0Item(it.prodId, it.left, it.leftDot + str(ch), it.rightDot[1:])
            nxt.add(newIt)

    return getClosure(nxt)


def buildTransTable():
    added = LR0Item(0, str(START_SYMBOL), "", str(S))
    auxset = set()
    auxset.add(added)
    state1 = getClosure(auxset)
    cnt = 1
    idToState[cnt] = state1
    stateToId[tuple(state1)] = cnt
    cnt += 1

    que = [state1]

    while len(que) > 0:
        nod = que[0]
        que.pop(0)

        symbols = terminals.copy()
        mergeSets(symbols, nonterminals)

        for ch in symbols:
            nxt = getNextState(nod, ch)
            if len(nxt) == 0:
                continue

            frz = tuple(nxt)
            if frz not in stateToId:
                idToState[cnt] = nxt
                stateToId[frz] = cnt
                cnt += 1
                que.append(nxt)

            auxdict = transition.get(stateToId.get(tuple(nod)))
            if auxdict is None:
                auxdict = {}
            auxdict.update({ch: stateToId.get(tuple(nxt))})
            transition.update({stateToId.get(tuple(nod)): auxdict})


def addAction(id, ch, act):
    if id in actionTable and ch in actionTable.get(id) and actionTable.get(id).get(ch).id != act.id and actionTable.get(
            id).get(ch).type != act.type:
        return True
    else:
        current = actionTable.get(id)
        if current is None:
            actionTable.update({id: {ch: act}})
        else:
            actionTable.get(id).update({ch: act})
        return False


def buildActionGoto():
    for it in idToState:
        currId = it
        state = idToState[it]

        for item in state:
            if item.rightDot != "" and isTerminal(item.rightDot[0]):
                act = Action(transition[currId][item.rightDot[0]], "SHIFT")
                fail = addAction(currId, item.rightDot[0], act)
                if fail:
                    return False
            elif item.prodId != 0 and item.rightDot == "":
                act = Action(item.prodId, "REDUCE")
                left = allProds[item.prodId].left

                for str in follow[left]:
                    if str == "":
                        continue
                    act = Action(item.prodId, "REDUCE")
                    fail = addAction(currId, str[0], act)
                    if fail:
                        return False
            elif item.prodId == 0 and item.rightDot == "":
                act = Action(-1, "ACCEPT")
                fail = addAction(currId, END_SYMBOL, act)
                if fail:
                    return False

        for nonterm in nonterminals:
            if transition.get(currId) is not None and nonterm in transition.get(currId):
                aux = {nonterm: transition.get(currId)[nonterm]}
                if gotoTable.get(currId) is None:
                    gotoTable.update({currId: aux})
                else:
                    gotoTable[currId].update(aux)
    return True


def printActionTable():
    for it in idToState:
        currId = it
        for ch in terminals:
            aux = actionTable.get(currId)
            if aux is not None:
                print("action[" + str(currId) + "][" + str(ch) + "] = " + str(aux.get(ch)))
    print()


def runWord(str):
    str += END_SYMBOL
    stk = []
    usedProds = []
    stk.append(1)
    while True:
        currState = stk[-1]
        currChar = str[0]

        act = actionTable.get(currState).get(currChar)
        if act is None:
            return False, list(reversed(usedProds))
        if act.type == "ACCEPT":
            return True, list(reversed(usedProds))
        elif act.type == "SHIFT":
            stk.append(act.id)
            str = str[1:]
        elif act.type == "REDUCE":
            p = allProds[act.id]
            length = len(p.right)
            for _ in range(length):
                stk.pop(-1)

            if gotoTable.get(stk[-1]).get(p.left) is None:
                return False, list(reversed(usedProds))

            stk.append(gotoTable[stk[-1]][p.left])
            usedProds.append(p.id)


if __name__ == '__main__':
    f = open("input.in", "r")
    n, S = f.readline().strip().split(" ")
    n = int(n)
    firstprod = Production(0, str(START_SYMBOL), str(S))

    allProds.append(firstprod)
    prod[firstprod.left] = [firstprod]

    buildTerms(str(START_SYMBOL))
    buildTerms(str(END_SYMBOL))

    for i in range(n):
        auxleft, auxright = f.readline().strip().split(" ")

        p = Production(i + 1, auxleft, auxright)
        p.right = p.right.replace(LAMBDA, "")

        allProds.append(p)
        if p.left not in prod:
            prod.update({p.left: []})
        prod[p.left].append(p)

        buildTerms(str(p.left))
        buildTerms(str(p.right))

    buildFirst()
    buildFollow()
    buildTransTable()

    print(first)
    print(follow)

    isSLR = buildActionGoto()
    if not isSLR:
        print("GRAMATICA NU ESTE SLR\n")
        exit()

    print("GRAMATICA ESTE SLR1\n")

    printActionTable()

    nrWords = int(f.readline().strip())
    for _ in range(nrWords):
        w = f.readline().strip()
        w = w.replace(LAMBDA, "")

        result, usedProds = runWord(w)
        if w == "":
            w = "LAMBDA"
        if result:
            print("Cuvantul: " + w + " este in gramatica!")
            for idx in usedProds:
                print(allProds[idx])
            print()
        else:
            print("Cuvantul: " + w + " nu este in gramatica!")
