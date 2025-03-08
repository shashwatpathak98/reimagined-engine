class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        upper_limit = right + 1
        array_primes = [True] * upper_limit

        array_primes[0] = array_primes[1] = False

        for i in range(2, int(upper_limit**0.5) + 1):
            if array_primes[i]:
                for j in range(i * i, upper_limit , i ):
                    array_primes[j] = False
        primes =  [ i for i in range(left , right+1) if array_primes[i]]
        if len(primes) < 2:
            return [-1,-1]

        return min(zip(primes , primes[1:]) , key=lambda pair: pair[1] - pair[0])             



        