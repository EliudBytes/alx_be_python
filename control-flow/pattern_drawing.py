#!/usr/bin/env python3
# pattern_drawing.py
# Draw a square pattern of asterisks using a while loop and a nested for loop.

def main() -> None:
    # Prompt exactly as required by the checker
    while True:
        try:
            size = int(input("Enter the size of the pattern: "))
            if size <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    row = 0
    while row < size:
        for _ in range(size):
            print("*", end="")
        print()  # move to next line after finishing the row
        row += 1

if __name__ == "__main__":
    main()
