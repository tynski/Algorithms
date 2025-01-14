def is_prime(number):
    if number <= 1:
        return False
    for i in range(2,int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

def generate_prime_array(n):
    primes_array = []
    i = 1
    while n:
        if is_prime(i):
            primes_array.append(i)
            n -= 1
        i += 1
    return primes_array
