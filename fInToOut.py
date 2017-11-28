def InToOut(s):
    q = []
    x = 0
    out = []
    while x < len(s):
        t = None

        if s[x] == '(':
            q.append(s[x])
            x += 1

        elif s[x] == ')':
            while q[len(q) - 1] != '(':
                out.append(str(q.pop()))
            q.pop()
            x += 1
        elif s[x] == '*' or s[x] == '/':
            if len(q) > 0:
                while q[len(q) - 1] == '*' or q[len(q) - 1] == '/' or q[len(q) - 1] == '^':
                    out.append(str(q[len(q) - 1]))
                    q.pop()
                    if len(q) == 0:
                        break
            q.append(s[x])
            x += 1
        elif s[x] == '-' or s[x] == '+':
            if len(q) > 0:
                while q[len(q) - 1] == '*' or q[len(q) - 1] == '/' or q[len(q) - 1] == '-' or q[len(q) - 1] == '+' or q[
                            len(q) - 1] == '^':
                    out.append(str(q[len(q) - 1]))
                    q.pop()
                    if len(q) == 0:
                        break
            q.append(s[x])
            x += 1
        elif s[x] == '^':
            q.append('^')
            x += 1
        elif x < len(s) and '0' <= s[x] <= '9':
            while x < len(s) and '0' <= s[x] <= '9':
                if t:
                    t = t * 10 + int(s[x])
                else:
                    t = int(s[x])
                x += 1

            if t is not None:
                out.append(t)



        else:
            if x < len(s):
                out.append(s[x])
                x += 1
    while len(q) > 0:
        out.append(str(q.pop()))
    return (out)

