def isBalanced(s):
    opens = ['(','[','{']
    pairs_map = {
                    ")":"(",
                    "]":"[",
                    "}":"{"
        }

    stack = []
    
    for i in s:
        if i in opens:
            stack.append(i)
        else:
            if len(stack) < 1:
                return 'NO'
            if pairs_map[i] != stack[-1]:
                return 'NO'
            
            stack.pop()
    
    if len(stack) == 0:
        return 'YES'
    else:
        return 'NO'
