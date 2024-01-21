def pushAtBottom(myStack: deque, x: int):
    if len(myStack) == 0:
        myStack.append(x)
        return myStack

    temp = []

    while myStack:
        temp.append(myStack[-1])
        myStack.pop()
    myStack.append(x)

    while temp:
        myStack.append(temp[-1])
        temp.pop()

    return myStack