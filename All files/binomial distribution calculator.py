import math
def binomial(num, prob, x):
    sum = 0
    suc = x
    menu = int(input("Enter 0 if equals, 1 if more than and 2 if less than:  "))
    if menu == 0:
        output = math.factorial(num) / (math.factorial(x) * math.factorial(num - x)) * (prob ** x) * ((1 - prob) ** (num - x))
        print(output)
    elif menu == 1:
        for i in range(suc + 1, num + 1):
            sum += math.factorial(num) / (math.factorial(i) * math.factorial(num - i)) * (prob ** i) * ((1 - prob) ** (num - i))
        print(sum)


binomial(3, 0.5, 1)
