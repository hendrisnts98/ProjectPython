print(30*"=")
print("Kalkulator Sederhana")
print(30*"=" + "\n")

angka_1 = float(input("Input = "))
operator = input("Operator(+,-,x,/) = ")
angka_2 = float(input("input = "))

if operator == "+":
    hasil = angka_1 + angka_2
    print(f"Output {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"Output {hasil}")
elif operator == "x":
    hasil = angka_1 * angka_2
    print(f"Output {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"Output {hasil}")
else:
    print("Error! NotFound di Operator")