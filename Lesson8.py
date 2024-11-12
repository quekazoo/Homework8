def add_one():
    chislo = input("Введите число: ")
    number = int(''.join(map(str, chislo)))
    number += 1
    return [int(chislo) for chislo in str(number)]
print(add_one())