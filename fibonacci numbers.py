sum=0
a=1
n=int(input("enter the how many numbers of the fibinocci series : "))
i=0
if n == 1 :
    print("0")
else : 
    print(sum)
    while i < (n-1) :
        k=sum
        sum=sum+a
        print(sum)
        a=k
        i=i+1
