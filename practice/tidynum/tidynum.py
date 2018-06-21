# https://code.google.com/codejam/contest/3264486/dashboard#s=p1

def naming(s):
    l = len(s)
    if(l == 0):
        return ""
    d = int(s[0])
    if(int(s) >= int(s[0] * l)):
        return s[0] + naming(s[1:])
    else:
        return (str(d-1) + ('9' * (l -1)))
    

def itr(s):
    l = len(s)
    if(l<2): return s
    op = ""
    for i in range(l):
        d = int(s[i])
        d55 =(l - i ) * s[i]
        if(s[i:] >= d55):
            op += s[i]
        else:
            op += (str(d-1) + ('9' * (l - i - 1)) )
            break;
    return op
        
    
if __name__ == '__main__':
    N = int(input())
    for n in range(N):
        s = str(input())
        print("Case #%d: %d"%(n+1, int(itr(s))))

        
    