prime_factors = []
prompt = int(input("What number would you like to prime factorise:  "))
answer = str("The prime factorisation of "+str(prompt)+" is ")
prime_factors.append(prompt)
def breakdown(num):
	for i in range(2, num+1):
		if num % i == 0:
			prime_factors.append(i)
			prime_factors.append(int(num/i))
			prime_factors.remove(num)
			break

while prime_factors[len(prime_factors)-1] != 1:
	breakdown(prime_factors[len(prime_factors)-1])

for i in range(len(prime_factors)-1):
	answer += str(prime_factors[i])+"*"
answer += "1"
print(answer)
