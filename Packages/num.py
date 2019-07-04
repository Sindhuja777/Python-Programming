# Function to check whether a given number is prime or not
def isprime(n):
    count=0
    for i in range(1,n):
        if n%i==0:
            count=count+1
    if count==1:
        return True
    else:
        return False