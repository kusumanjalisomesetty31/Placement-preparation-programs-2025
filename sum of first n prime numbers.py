def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
def  sum_of_primes(num):
    n=2
    primes=[]
    while(len(primes)<num):
        if(is_prime(n)):
            primes.append(n)
        n=n+1
    return sum(primes)
print("enter the value of n")
N=int(input())
print(sum_of_primes(N))