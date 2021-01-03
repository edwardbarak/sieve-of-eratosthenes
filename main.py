def sieve(end):
    potentialPrimes = set(range(2, end+1))
    primes = []
    i = next(iter(potentialPrimes))

    while i**2 < end:
        primes.append(i)
        potentialPrimes = potentialPrimes.difference(set(range(i, end+1, i)))
        i = next(iter(potentialPrimes))
    return primes + list(potentialPrimes)

if __name__ == "__main__":
    print('Printing prime numbers smaller than 100:')
    primes = sieve(100)
    print(primes)
    print('{} prime numbers smaller than 100'.format(len(primes)))