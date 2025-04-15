def rotations(a,n,asize):
    for i in range (n):
        rotate(a,asize)
def rotate(a,asize):
    temp=a[0]
    for i in range(asize-1):
        a[i]=a[i+1]
        a[asize-1]=temp
def printarr(a,asize):
    for i in range (asize):
        print("%d"%a[i],end=" ")
    print("\n")
a=[12,13,31,45,76,345876,3]
printarr(a,len(a))
rotations(a,2,len(a))
printarr(a,len(a))