def calculator():
    print("--- SIMPLE CALCULATOR ---")
    
    try:
        num1 = float(input("Pahila number taka: "))
        num2 = float(input("Dusra number taka: "))
    except ValueError:
        print("Chukiche input! Krupaya fakt numbers taka.")
        return

    print("\nOperation nivda:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Option taka (1/2/3/4 kinva +, -, *, /): ")

    if choice in ('1', '+'):
        print(f"Uttar: {num1} + {num2} = {num1 + num2}")
    elif choice in ('2', '-'):
        print(f"Uttar: {num1} - {num2} = {num1 - num2}")
    elif choice in ('3', '*'):
        print(f"Uttar: {num1} * {num2} = {num1 * num2}")
    elif choice in ('4', '/'):
        if num2 == 0:
            print("Error: 0 ne bhag deta yet nahi.")
        else:
            print(f"Uttar: {num1} / {num2} = {num1 / num2}")
    else:
        print("Chukicha option nivdla aahe.")

if __name__ == "__main__":
    calculator()