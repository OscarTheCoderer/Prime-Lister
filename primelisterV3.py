import math

# Read, list and reformat testprime file
print("OPENING FILE /testlist.txt")
file = open("testlist.txt", "r")
print("FILE OPEN")
print("LISTING FILE /testlist.txt")
testprimes = file.readlines()
file.close()
print("FILE LISTED")
print("FORMATING FILE LIST /testprimes")
for x in range(0,len(testprimes)):
    testprimes[x] = int(testprimes[x].strip())
print("FILE FORMATED")
biggesttestprime = testprimes[-1]
print("HIGHEST TEST PRIME /%d" % biggesttestprime)

# Prime test
def isprime(num):
    sqrt = math.ceil(math.sqrt(num))
    for prime in testprimes:
        if prime > sqrt:
            break
        elif num % prime == 0:
            return False
    if sqrt > biggesttestprime:
        for testnum in range(biggesttestprime, sqrt):
            if prime % testnum == 0:
                return False
    return True

# open file for writing
file = open("primelist.txt", "r")
start = int(file.readlines()[-1]) + 1
file.close()
file = open("primelist.txt", "a+")

# set variables
primesfound = 0
numchecked = 0

# don't test even numbers
if start % 2 == 0:
	start = start + 1
testnum = start

# test and write infinately
print("TESTING NUMBERS")
while True:
	if isprime(testnum):
		file.write("%d\n" % testnum)
		primesfound = primesfound + 1
	numchecked = numchecked + 2
	testnum = testnum + 2
	if numchecked % 25000 == 0:
		print("%d / %d numbers were prime (%d%%)" % (primesfound, numchecked, (primesfound/numchecked) * 100)) # report number of primes found every 1,000,000 numbers tested
