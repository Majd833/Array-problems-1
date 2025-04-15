def leaders(a,a_size):
    currmax=a[a_size-1]
    print(currmax)
    for i in range (a_size-2,-1,-1):
        if currmax<a[i]:
            print(a[i])
            currmax=a[i]
a=[2,6,4,56,87,45,123,17]
leaders(a,len(a))