import random
import string

def password_generator():
    print("--- PASSWORD GENERATOR ---")
    
    try:
        length = int(input("Password chi lambi (length) kiti havi? (Udaharan: 8, 12): "))
        if length < 4:
            print("Surakshit password sathi lambi kimaan 4 taka.")
            return
    except ValueError:
        print("Chukiche input! Krupaya fakt number taka.")
        return

    print("\nPassword chi complexity (kathinya patali) nivda:")
    print("1. Sadha (Fakt Akshare - Letters)")
    print("2. Madhyam (Akshare ani Ank - Letters + Numbers)")
    print("3. Majboot / Strong (Akshare, Ank ani Chinhe - Letters + Numbers + Symbols)")

    choice = input("Tumcha option nivda (1/2/3): ")

    if choice == '1':
        characters = string.ascii_letters
    elif choice == '2':
        characters = string.ascii_letters + string.digits
    elif choice == '3':
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Chukicha option! Default 'Strong' password tayar karat aahe.")
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"\nTumcha navin Password: {password}")

if __name__ == "__main__":
    password_generator()