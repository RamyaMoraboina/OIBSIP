height = float(input("enter the height in cm:"))
weight = float(input("enter the weight in kg:"))

BMI = weight/(height/100)**2

print("your body mass index is:",BMI)

if BMI <= 18.5:
    print("you are underweight.")
elif BMI <=24.9:
    print("Awesome,you are healthy.")
elif BMI <=29.9:
    print("you are over weight.")
else:
    print("You are obese.")