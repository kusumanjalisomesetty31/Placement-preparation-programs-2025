n=int(input("Enter the number"))
num=n
rem=0
pro=1
sum=0
t=len(str(n))
while(n>0):
    rem=n%10
    pro=rem**t
    n=n//10
    sum=sum+pro
if sum==num:
    print("The num is armstrong number")
else:
    print("Number is not armstrong number")
    
    
    
    

    
    





