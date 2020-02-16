# Project Euler #3
# https://projecteuler.net
# Calculate largest prime Factors
# Jan 28 2020


def get_prime(num):
    list = []
    if num == 1:
        return [1]
    else:
        for i in range(2, num+1):
            if num % i==0:
                list.append(i)
                numbers = get_prime(num//i)
                for p in numbers:
                    list.append(p)
                return list

print("Calculating the primes...")

primes = get_prime(600851475143)
primes.sort() # sort for visual enjoyment. Could have used max() for simplicity
print(primes)
print(f'largest: {primes[-1]}')