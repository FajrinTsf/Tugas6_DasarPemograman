print("----- Program Grade Nilai-----")
nama = input("Masukkan nama anda: ")
nilai = int(input("Inputkan nilai (0-100): "))

if nilai >= 90:
    grade = "A"
    predicate = "With Compliments"
elif nilai >= 80:
    grade = "B"
    predicate = "Very Satisfy"
elif nilai >= 70:
    grade = "C"
    predicate = "Satisfying"
elif nilai >= 60:
    grade = "D"
    predicate = "Not Satisfactory"
elif nilai >= 0:
    grade = "E"
    predicate = "Not Pass"

print(nama, "Mendapat Nilai", grade, "dengan Predikat", predicate)
print("================================================")
