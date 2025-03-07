class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        MAX = right + 1
        is_prime = [True] * MAX
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(MAX **0.5) + 1):
            if is_prime[i]:
                for j in range(i*i , MAX , i):
                    is_prime[j] = False

        primes = [ i for i in range(left , right+1) if is_prime[i]]
        if len(primes) < 2:
            return [-1,-1]
        
        return min(zip(primes , primes[1:]) , key=lambda pair: pair[1] - pair[0])


        