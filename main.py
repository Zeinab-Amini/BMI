# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
Bmi = round(weight / height ** 2)

if Bmi < 18.5:
    print(f"Your bmi is {Bmi}, you are underweight")
elif Bmi > 25:
    print(f"Your bmi is {Bmi}, you have a normal weight.")
elif Bmi > 30:
    print(f"Your bmi is {Bmi}, you are slightly overweight. ")
elif Bmi > 35:
    print(f"Your bmi is {Bmi}, you are obese")
else:
    print(f"Your bmi is {Bmi}, you are clinically obese. ")