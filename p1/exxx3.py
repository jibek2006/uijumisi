
num1 =float(input("Birinchi sonni kiriting: "))
num2 =float(input("Ikkinchi sonni kiriting: "))
num3 =float(input("Uchinchisini kiriting: "))


sonlar = num1**2 + num2**2

if num3 != 0: 
    result = sonlar/ num3
    print(f"result: {result}")
else:
    print("Uchinchi son 0  mas")
