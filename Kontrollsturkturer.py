from hashlib import new
from random import randint
random_number = randint(1, 100)
print("Jag tänker på ett tal mellan 1 och 100")
guess = int(input("Gissa vilket tal jag tänker på!"))
if guess == random_number:
  print("Snyggt jobbat! Det var rätt!")
else:
  print("Tyvärr, det var fel.")

found = False
while not found:
  guess = int(input("Gissa vilket tal jag tänker på!"))
  if guess == random_number:
    found = True
  else:
    print("Tyvärr. Det var fel.") 