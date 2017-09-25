from sys import argv

def opprecedence(operator):
    if operator in ('+', '-'):
        return 2
    elif operator in ('*', '/'):
        return 3
    elif operator in ('^'):
        return 4
    return 0

def shuntingyard(sexp):
    opstack = []
    output = []
    for char in sexp:
        curprec = opprecedence(char)
        print("Current char: ", char)
        print("Current prec: ", curprec)
        if curprec > 0:
            output.append(" ")
            while len(opstack) > 0:
                topsprec = opprecedence(opstack[len(opstack) - 1])
                if topsprec >= curprec:
                    output.append(opstack.pop())
                    output.append(" ")
                else:
                    break
            opstack.append(char)
        else:
            output.append(char)

        print("Current opstack: ", opstack)
        print("Current output: ", output)

    for op in opstack[::-1]:
        output.append(" ")
        output.append(opstack.pop())

    print("".join(output))


if __name__ == "__main__":
    shuntingyard(argv[1])
