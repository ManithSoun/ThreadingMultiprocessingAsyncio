import multiprocessing 
#import requests

def is_prime(n):
  # Check if the number is prime or not
  if n == 2:
    return True
  if n < 2 or n % 2 == 0:  #0, 1, and even numbers are not prime
    return False
                    #square(n) + 1
  for i in range(3, int(n ** 0.5) + 1, 2): 
    if n % i == 0:
      return False  
     
  return True 

def check_prime_chunk(numbers):
  primes = [number for number in numbers if is_prime(number)]
  return primes

def find_primes_in_range(numbers, chunk_size):
  chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]
  
  with multiprocessing.Pool() as pool:
    result = pool.map(check_prime_chunk, chunks)

  primes = [prime for sub in result for prime in sub]
  return primes