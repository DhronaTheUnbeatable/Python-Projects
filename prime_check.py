n=int(input('Enter your number here: '))
i=2
if n==1:
    print('your number is not a prime number')
else:
    while i<n:
        if n%i == 0:
            print('your number is not a prime number')
            break
    
        i=i+1

if i == n :
    print('your number is a prime number')
        
