
def naming(s):
    l = len(s)
    if(l == 0):
        return ""
    d = int(s[0])
    if(int(s) >= int(s[0] * l)):
        return s[0] + naming(s[1:])
    else:
        return naming(str(d-1) + ('9' * (l -1)))
    
if __name__ == '__main__':
    N = int(input())
    for n in range(N):
        s = str(input())
        print("Case #%d: %d"%(n+1, int(naming(s))))

        
    