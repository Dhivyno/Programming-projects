allValues = []
valueNum = []
val = 1
while val != 0:
    val = int(input("Enter a new base value that the number can be split into and 0 if you have entered all values: "))
    if val != 0:
        allValues.append(val)
        valueNum.append("")
allValues.sort()
allValues.reverse()
num = int(input("Enter the number you want to split into the base values: "))

for i in range(len(allValues)):
    valueNum[i] = int(num/(allValues[i]))   #runs through the base values and determines how many of each base value makes up the number
    num -= valueNum[i]*allValues[i]

for i in range(len(allValues)):
    print(valueNum[i], "  ", allValues[i], "'s")
