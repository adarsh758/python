name = input("Enter your name: ")
age = int(input("Enter your age: "))
height_cm = float(input("Enter your height(cm): "))
weight = float(input("Enter your weight(kg): "))

height_m = height_cm/100
BMI = weight / (height_m ** 2)


# BMI Category
if BMI < 18.5:
    bmi_result = "Underweight"
elif BMI <= 24.9:
    bmi_result = "Normal"
elif BMI <= 29.9:
    bmi_result = "Overweight"
else:
    bmi_result = "Obese"

# Warnings
extra_note = ""

if age < 18 and BMI > 25:
    extra_note = " (Warning: High BMI for your age)"
elif age > 60 and BMI < 18:
    extra_note = " (Caution: Low BMI at at age)"

# Output
print(f"""
===== BMI RESULT =====
Name: {name}
Age: {age}
Height: {height_cm} cm 
Weight: {weight} kg

BMI: {BMI:.2f} → {bmi_result}{extra_note}
""")

