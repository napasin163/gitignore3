n = input(" Enter Number : ")
n = int(n)
print(" {}! = ".format(n),end="")
for l in range(1,n+1):
    if l<n:
        print("{} x ".format(l),end="")
        l = l+1
    else:
        print("{}".format(l))
        l = l+1
def fac(n):
    if n == 0:
        return 1
    else:
        return n*fac(n-1)
print(" {}! = {} ".format(n,fac(n)))
