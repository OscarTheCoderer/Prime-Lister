def isprime(num):
    for x in range(2,int(num**0.5)+1):
        if num%x==0:
            return False
    return True

file = open("primelist2.txt", "a+")

file = open("primelist2.txt", "r")
linelist = file.readlines()
start = int(linelist[-1].strip()) + 1

file = open("primelist2.txt", "a+")

end = int(input("limit >>> "))
    
primesfound = 0
numberschecked = 0

for x in range(start, end):
    numberschecked = numberschecked + 1
    if isprime(x):
        file.write("%d\n" % x)
        primesfound = primesfound + 1
    if numberschecked % 100000 == 0:
        print("%d / %d numbers tested are prime (%d%%)" % (primesfound, numberschecked, (primesfound/numberschecked)*100))

print("Found %d primes" % primesfound)
file.close()
