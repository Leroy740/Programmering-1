def easy_quiz():
    score=0



    print("welcome to the easy quis")

    ans1 = input("who was in Paris?").lower()
    if ans1 == "jidion":
        print("correct")
        score += 12

    else: print ("incorect")

    B = input("Who took the woook to poland?").lower()

    if B == "⛵🤏":
        print("corect")
        score += 616

    else: print("incorect")

    C = input("who raided the capitol?").lower()
    if C == "americans":
        print("cortect")
        score += 96

    else: print ("inco")

    Ö = input("who asked?").lower()
    if Ö == "no🧍":
        print("corecto")
        score += 0

    else: print("incorect💀")


    print(score)

for _ in range(3):
    easy_quiz()