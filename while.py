numbers = []
num = 0

while num >= 0:
    num = int(input("Masukkan angka (negatif untuk berhenti): "))
    if num >= 0:
        numbers.append(num)

print("Angka yang dikumpulkan:", numbers)
