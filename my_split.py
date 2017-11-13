print('hello world !')
s = '..asd....dfdf......asas.....asd..adfs.asd....'

def my_split(s,sep):
    m=0
    n=s.find(sep)
    if n==m:
        print('\'\'')
    else:
        print(s[m:n])

    sepl = len(sep)

    while n != -1:
        m = n + sepl
        n = s.find(sep,m)
        #print('m=',m)
        #print('n=',n)
        if m == n :
            print('\'\'')
        elif n != -1:
            print(s[m:n])
        else:
            if m == len(s):
                print('\'\'')
            else:
                print(s[m:len(s)+1])

sep = '...'

s1=my_split(s,sep)
print(s1)
print(s.split(sep))
