weight=eval(input("enter weight in pounds:"))
feets=eval(input("enter feets:"))
inches=eval(input("enter inches:"))
height=12*feets+inches
kilograms_per_pound=0.45359237
meters_per_inch=0.0254
weightInKilograms=weight*kilograms_per_pound
heightInMeters=height*meters_per_inch
bmi=weightInKilograms/(heightInMeters**2)
if bmi<18.5:
        print("BMI is",bmi,"\n",
              "You are Underweight")
elif bmi<25:
        print("BMI is",bmi,"\n",
              "You are Normal")
elif bmi<30:
        print("BMI is",bmi,"\n",
              "You are Overweight")
else:
        print("BMI is",bmi,"\n",
              "You are Obese")
