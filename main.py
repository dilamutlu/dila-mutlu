print("Merhaba Dünya!")

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

primes = []
count = 0
num = 2

while count < 100:
    if is_prime(num):
        primes.append(num)
        count += 1
    num += 1

print("İlk 100 Asal Sayı Listesi =>")
print(", ".join(map(str, primes)))