def primesInRange(start, end):
	primes = []
	for i in range(start, end + 1):  # Assumption - range includes start and end numbers
		factors = getFactors(i)
		if len(factors) is 0:
			primes.append(i)
	return primes


def getFactors(number):
	factors = []
	for i in range(2, number // 2 + 1):
		if number % i is 0:
			factors.append(i)
	return factors


if __name__ == "__main__":
	while True:
		option = input("Enter 'prime' or 'range': ")
		if option == "prime":
			number = int(input("Enter number: "))
			factors = getFactors(number)
			if len(factors) is 0:
				print("Prime!")
			else:
				print("Factors of " + str(number) + ":")
				for i in factors:
					print(i)
		elif option == "range":
			numberStart = int(input("Enter start of range: "))
			numberEnd = int(input("Enter end of range: "))
			primes = primesInRange(numberStart, numberEnd)
			if len(primes) is 0:
				print("No prime numbers in range")
			else:
				print("Primes of in range:")
				for i in primes:
					print(i)
		else:
			print("input not recognised")

	"""
	primeNumber = [2, 23, 37, 47, 53, 67, 79, 83, 89, 97, 113, 127, 131, 157, 163, 167, 173, 211, 223, 233, 251, 257, 263, 277, 293, 307, 317, 331, 337, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 439, 443, 449, 457, 467, 479, 487, 491, 499, 503, 509, 541, 547, 557, 563, 577, 587, 593, 607, 613, 631, 647, 653, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 839, 853, 863, 877, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
	for i in primeNumber:
		factors = getFactors(i)
		if len(factors) is 0:
			print("Prime!")
		else:
			print("Factors of " + str(i) + ":")
			for j in factors:
				print(j)
	"""
