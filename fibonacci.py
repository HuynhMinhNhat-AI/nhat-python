
def fibonacci(n):
  a = [0, 1]
  while len(a) < n:
    next_number = a[-1] + a[-2]
    a.append(next_number)
  return (a)
while True:
 try:
  n = int(input("How many Fibonacci numbers? "))
 except ValueError:
  print("Please type in integer!")
  continue
 result = fibonacci(n)
 print("fibonacci sequence is: ")
 print(result)
 choice = input("Do you want to keep using (Yes/No): ")
 if choice.lower() in ["yes", "y"]:
   print("Continuing the program")
 elif choice.lower() in ["no", "no"]:
   print("Goodbye, I hope to see you again")
   break