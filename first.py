# Since: 80 ÷ (1.75 x 1.75) = 26.122448979591837
height = input("what is your heght: ")
weight = input("what is your weight: ")
bmi = int(weight) / float(height) ** 2   
print(bmi)

if bmi < 18 :
  print('your not a proper WEIGHT' )
elif bmi < 29:
  print("your normal weight")
elif bmi > 30:
  print("your obese")


