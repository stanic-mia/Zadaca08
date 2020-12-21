
brojA = int(input("Unesite prvi broj: "))
brojB = int(input("Unesite drugi broj: "))
operacija = input("Unesite računsku operaciju (+, -, *, /): ")





if operacija == "+":
    print("Rezultat zbrajanja je: " + str(brojA + brojB))
elif operacija == "-":
    print("Rezultat oduzimanja je: " + str(brojA - brojB))
elif operacija == "*":
    print("Rezultat množenja je: " + str(brojA * brojB))
elif operacija == "/":
    print("Rezultat dijeljenja je: " + str(brojA / brojB))
else:
    print("Ne prepoznajem ovu računsku operaciju.")