def sieve(end):
    potentialPrimes = set(range(2, end+1))
    primes = []
    i = list(potentialPrimes)[0]

    while i**2 < end:
        primes.append(i)
        potentialPrimes = potentialPrimes.difference(set(range(i, end+1, i)))
        i = list(potentialPrimes)[0]
    return primes + list(potentialPrimes)

if __name__ == "__main__":
    print('Printing prime numbers smaller than 100:')
    primes = sieve(100)
    print(primes)
    print('{} prime numbers smaller than 100'.format(len(primes)))