#Body mass index (BMI) is a measure of body fat based on height and weight that applies to adult men and women
#BMI is a reliable indicator of body fatness for most people. It is used to screen for weight categories that may lead to health -
#problems. This calculator provides BMI and the corresponding weight category.
#What's normal BMI for a woman?
#18.5—24.9
#Adult BMI Calculator
#BMI	       Weight Status
#==============================
#Below 18.5	     Underweight
#18.5—24.9	     Healthy Weight
#25.0—29.9	     Overweight
#30.0 an Above   Obesity
#VERSION_2.0

height = float(input("Your height in metres: "))
weight = int(input("Your weight in kilograms: "))
bmi = round(weight / (height*height) , 1)
if bmi <= 18.5:
    print("Your BMI is" , bmi , "which means you are a bit underweight.")
elif bmi > 18.5 and bmi < 25:
    print("Your BMI is" , bmi , "which means you are fit and healthy.")
elif bmi > 25 and bmi < 30:
    print("Your BMI is" , bmi , "which means you are a bit overweight.")
elif bmi > 30:
    print("Your BMI is" , bmi , "which means you are a bit obese.")
else:
    print("Invalid Input.")