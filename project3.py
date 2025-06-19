def celcius_fahrenheit(c):
    return (c * 9/5) + 32
def fahreheit_celcius(f):
   return (f - 32) * 5/9
def cm_inch(cm):
   return cm * 0.3937
def inch_cm(inch):
   return inch / 0.3937
def kg_lb(kg):
   return kg * 2.2
def lb_kg(lb):
   return lb / 2.2
print("Welcome to the units convertion, choose which unit you want to convert")
print("1. Celcius -> Fahrenheit")
print("2. Fahrenheit -> Celcius")
print("3. cm -> inch")
print("4. inch -> cm")
print("5. kg -> lb")
print("6. lb -> kg")
print("7. quit")
choice = input("Choose the convertion (1-7): ")
if choice == "1":
        c = float(input("C: "))
        print("F = ", celcius_fahrenheit(c))
if choice == "2":
    f = float(input("F: "))
    print("C= %.2f" % fahreheit_celcius(f))
  
   
