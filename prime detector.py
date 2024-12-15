from math import sqrt

def is_prime(eded: int) -> bool:
    if eded == 1 or not eded % 2:
        return 0
    counter = 0
    for i in range(3, int(sqrt(eded))+1, 2):
        counter += 1
        if not eded % i:
            print(f"{counter} cehd")
            return False
    print(f"{counter} cehd")
    return True

while True:
    eded = int(input("Eded: "))
    res = is_prime(eded)
    print("Eded sadedir" if res else "Eded sade deyil")