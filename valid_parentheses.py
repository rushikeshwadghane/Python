"""Practice example defining or demonstrating `valid_parenthesis`."""


def valid_parenthesis(s:str) -> str:
    par = {
        '}':'{',
        ']':'[',
        ')':'('
    }
    stack  = []
    for i in s:
        if i in par:
            c = stack.pop()
            if par[i] != c:
                return False
        else:
            stack.append(i)

    return len(stack) == 0

print(valid_parenthesis('{[{()}]}'))
