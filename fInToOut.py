def inToOut(s):
    q = []
    x = 0
    out = []

    while x < len(s):
        t = None
        m = None
        k = 0

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
        elif x < len(s) and ('0' <= s[x] <= '9' or s[x] == '.'):

            while x < len(s) and '0' <= s[x] <= '9':
                if t:
                    t = t * 10 + float(int(s[x]))
                else:
                    t = float(int(s[x]))
                x += 1
            try:
                if s[x] == '.' :

                    x+=1
                    try:
                         while '0' <= s[x] <= '9':
                            k+=1
                            if m != None:
                                m = m  + (int(s[x])/(10**k))

                            else:
                                m = float(int (s[x])/(10))
                            x += 1
                    except:
                        pass
            except:
                pass


            if t is not None and m is not None:
                out.append(t+m)
            elif m is None:
                out.append(t)



        else:
            if x < len(s):
                out.append(s[x])
                x += 1
    while len(q) > 0:
        out.append(str(q.pop()))
    return out
