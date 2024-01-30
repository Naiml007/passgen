# password_generator.py
import sys
from password_functions import generate_basic_password, generate_advanced_password

def main():
    header = "Password Generator"
    footer = "Made by naimur"

    print("=" * len(header))
    print(header)
    print("=" * len(header))

    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        password_length = int(sys.argv[1])
    else:
        password_length = int(input("Enter the password length: "))

    print("\nChoose password type:")
    print("1. Basic password")
    print("2. Advanced password")

    option = input("Enter your choice (1 or 2): ")

    if option == "1":
        password = generate_basic_password(password_length)
    elif option == "2":
        password = generate_advanced_password(password_length)
    else:
        print("Invalid option. Exiting.")
        return

    print(f"\nGenerated Password: {password}")
    
    print("\n" + "=" * len(footer))
    print(footer)
    print("=" * len(footer))

if __name__ == "__main__":
    main()
