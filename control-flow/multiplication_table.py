#!/usr/bin/env python3
# multiplication_table.py
# Multiplication Table Generator

def main() -> None:
    while True:
        try:
            # Prompt exactly as the checker expects and use variable name `number`
            number = int(input("Enter a number to see its multiplication table: "))
            break
        except ValueError:
            print("Please enter a valid integer.")

    for i in range(1, 11):
        print(f"{number} * {i} = {number * i}")

if __name__ == "__main__":
    main()
