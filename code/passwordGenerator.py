import random
import string


def generate_password(length=12, use_upper=True, use_digits=True, use_special=True):
    if length < 1:
        return "Error: Password length must be at least 1."

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_upper else ""
    digits = string.digits if use_digits else ""
    special = string.punctuation if use_special else ""

    all_chars = lower + upper + digits + special

    if not all_chars:
        return "Error: At least one character type must be selected."

    password = [random.choice(lower)]
    if use_upper:
        password.append(random.choice(upper))
    if use_digits:
        password.append(random.choice(digits))
    if use_special:
        password.append(random.choice(special))

    if len(password) > length:
        pass

    remaining_length = length - len(password)
    for _ in range(remaining_length):
        password.append(random.choice(all_chars))

    random.shuffle(password)

    return "".join(password[:length])


def get_yes_no(prompt):
    while True:
        try:
            choice = input(prompt + " (y/n): ").strip().lower()
            if choice in ['y', 'yes']:
                return True
            if choice in ['n', 'no']:
                return False
            print("Please enter 'y' or 'n'.")
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled or not supported. Defaulting to 'Yes'.")
            return True


def main():
    print("Secure Password Generator")

    while True:
        try:
            length_input = input("Enter password length (default 12): ").strip()
            if not length_input:
                length = 12
            else:
                length = int(length_input)
                if length <= 0:
                    print("Please enter a positive number.")
                    continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled or not supported. Defaulting to length 12.")
            length = 12
            break

        break

    use_upper = get_yes_no("Include uppercase letters?")
    use_digits = get_yes_no("Include numbers?")
    use_special = get_yes_no("Include special characters?")

    password = generate_password(length, use_upper, use_digits, use_special)
    print(f"\nGenerated Password: {password}")


if __name__ == "__main__":
    main()