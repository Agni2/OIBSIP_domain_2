def get_valid_input(msg, expected_type=float, min_val=0.1, max_val=300.0):
    while True:
        try:
            user_input = expected_type(input(msg))
            if min_val <= user_input <= max_val:
                return user_input
            else:
                print(f"Value must be between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calc_bmi(w, h):
    return w / (h * h)

def determine_bmi_status(bmi_val):
    if bmi_val < 16:
        return "Severe underweight"
    elif bmi_val < 18.5:
        return "Underweight"
    elif bmi_val < 25:
        return "Healthy weight"
    elif bmi_val < 30:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("===== BMI Calculator =====\n(Using metric units)\n")
    weight = get_valid_input("Weight in kg (10–300): ", min_val=10, max_val=300)
    height = get_valid_input("Height in m (0.5–2.5): ", min_val=0.5, max_val=2.5)
    bmi = calc_bmi(weight, height)
    category = determine_bmi_status(bmi)

    print(f"\nBMI: {bmi:.1f}")
    print(f"Category: {category}")

    if bmi < 18.5:
        print("Note: Underweight may be linked to nutritional issues.")
    elif bmi >= 25:
        print("Note: Higher BMI can increase health risks.")

if __name__ == '__main__':
    main()
