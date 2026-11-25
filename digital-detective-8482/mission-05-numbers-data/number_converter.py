def main():
    try:
        number = int(input("Enter a non-negative whole number: "))
    except ValueError:
        print("Please enter a valid whole number.")
        return

    if number < 0:
        print("Please enter a non-negative number.")
        return

    print("Binary:", bin(number))
    print("Hexadecimal:", hex(number))


if __name__ == "__main__":
    main()
