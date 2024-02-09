class Prime:
    def __init__(self, n):
        self.n = n

    def isPrime(self, n):
        if n > 1:
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True
        return False

    def filterPrimes(self):
        return list(filter(lambda x: self.isPrime(x), self.n))

a = input()
b = list(map(int, a.split()))
prime_f = Prime(b)
print(prime_f.filterPrimes())
