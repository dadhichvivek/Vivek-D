a=input("Enter a name ")
i=0
l=len(a)
while(l>i):
    l=l-1
    if(a[i]!=a[l]):
        print("Not palindrome")
        break
    else:
        i=i+1
    print("Palindrome")
    break
