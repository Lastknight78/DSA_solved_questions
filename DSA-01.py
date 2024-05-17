def balance_check(s):
    sets = set('({[')
    stack = []
    accepted = [('(',')'),('[',']'),('{','}')]
    if len(s) % 2 != 0:
        return False
    for i in s:
        if i in sets:
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            else:
                last = stack.pop()
                if (last,i) not in accepted:
                    return False
    return len(stack) == 0
