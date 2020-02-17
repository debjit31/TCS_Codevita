def generatePrime(n1, n2):
    flag = 0
    for i in range(n1, n2+1):
        if i == 1:
            continue
        else:
            flag = 1
            for j in range(2, i//2 + 1):
                if i % j == 0:
                    flag = 0
                    break
            if flag == 1:
                primes.append(i)
    print(primes)

def createCombinations():
    for i in range(len(primes)):
        for j in range(len(primes)):
            if i != j:
                new_number = str(primes[i]) + str(primes[j])
                comb.append(new_number)
    
def checkPrime(n):
    flag = 1
    for i in range(2, n//2):
        if n % i == 0:
            flag = 0
            break
    if flag == 1:
        primes_two.append(n)
        
def fibonacciSeries(smallest,largest):
    a = smallest
    b = largest
    n = len(primes_two)
    for i in range(2, n):
        z = a+b
        ##print(z, end=' ')
        a = b
        b = z
    print(z)
        
    
    
    
primes = []
comb = []
primes_two = []
n1 = int(input())
n2 = int(input())
generatePrime(n1, n2)
createCombinations()
for i in comb:
    checkPrime(int(i))
print(primes_two)
print(len(primes_two))
smallest = primes_two[0]
largest = primes_two[-1]
print(smallest, largest)
fibonacciSeries(smallest, largest)
