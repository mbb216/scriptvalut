def calculate_bmi(weight, height):
    # BMI calculation
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    # Interpret BMI categories
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

def main():
    # User input for weight and height
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    # Calculate BMI
    bmi = calculate_bmi(weight, height)

    # Output the BMI and interpretation
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Interpretation: {interpret_bmi(bmi)}")

if __name__ == "__main__":
    main()
