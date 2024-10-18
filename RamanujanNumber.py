import random
import numpy as numpy

randomNumbers = numpy.arange(30, dtype=numpy.int32)
randomNumbersNew = numpy.delete(randomNumbers, 0)

i = 0
j = 0
k = 0
t = 0
arrayOne = []
arrayTwo = []
firstArray= []
secondArray = []

for i in range(i, len(randomNumbersNew)):
    for j in range(i+1, (len(randomNumbersNew) + 1)):
        firstArray.append(i)
        secondArray.append(j)
        arrayOne.append((pow(i,3) + pow(j,3)))
for k in range(k, len(arrayOne)):
    for l in range(k+1, len(arrayOne)):
        if arrayOne[k] == arrayOne[l]:
            arrayTwo.append(arrayOne[k])
        
p = 0
m = 0

while m < len(firstArray) and p < len(arrayTwo):   
    t = 0
    while t < len(secondArray):
        if arrayTwo[p] == (pow(firstArray[m],3) + pow(secondArray[t], 3)):
            print(firstArray[m],"^3", "+" , secondArray[t],"^3", "=",  arrayTwo[p] )
        t += 1
        m += 1
    m = 0
    p += 1

#Big O --> O(n*2)
