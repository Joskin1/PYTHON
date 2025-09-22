weight = float(input("Enter your weight: "))
unit =  input("Kilogram or POunds.... (K or P): ").upper()

if unit == "K":
    weight = weight * 2.20462
    unit = "Lbs"
    print(f"Your weight is {round(weight, 2)} {unit}")
elif unit == "P":
    weight = weight / 2.20462
    unit = "Kg"
    print(f"Your weight is {round(weight, 2)} {unit}")
else:
    print("Invalid unit")