from stack import Stack


def infixToPostfix(infixExpr: str) -> str:
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1
    }
    opStack = Stack()
    postfixList = []
    tokenList = list(infixExpr)
    for token in tokenList:
        if token.isalpha():
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and prec[opStack.peek()] > prec[token]:
                postfixList.append(opStack.pop())
            opStack.push(token)
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return ''.join(postfixList)


if __name__ == '__main__':
    infixExpr = 'C-D*C'
    postfixExpr = infixToPostfix(infixExpr)
    assert ''.join(postfixExpr) == 'CDC*-'
