import random
x = random.randint(1,100)

while True:
  print("guess the number between 1 and 100\n")
  y = input()

  if y.isdigit():
    if int(y) == x:
      print("correctamondo!\n")
      break

    elif int(y) < x:
      print("too low\n")

    elif int(y) > x:
      print("too high\n")
