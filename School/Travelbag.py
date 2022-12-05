# Travelbag
# Skelettkod till uppgiften

from operator import add


travelbag = ["omar", "heaven", "wock", "french neighbours", "lil baby", "bread"]

while True:
   menyval = input("1. Kolla i resväskan\n"
                   "2. Lägg sak i resväskan\n"
                   "3. Ta bort sak i resväskan\n"
                   "4. Avsluta program")

   if menyval == "1":
       print(travelbag)

   elif menyval == "2":
       travelbag.append (input("what do you wish to add?"))
       print(travelbag)
    

   elif menyval == "3":
    travelbag.remove (input("what u remve?="))
    print(travelbag)

   elif menyval == "4":
       break