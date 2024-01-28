def square_meters_to_square_feet(square_meters):
    # 1 square meter is approximately 10.764 square feet
    square_feet = square_meters * 10.764
    return square_feet

def main():
    # Prompt the user to enter the area of the house in square meters
    square_meters = float(input("Enter the area of the house in square meters: "))

    # Convert square meters to square feet
    square_feet = square_meters_to_square_feet(square_meters)

    # Print out the result
    print(f"The area of the house is approximately {square_feet:.2f} square feet.")

if __name__ == "__main__":
    main()
