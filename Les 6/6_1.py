def seizoen(maand):
    if maand in [12,1,2]:
        print("winter")
    elif maand in [3,4,5]:
        print("lente")
    elif maand in [6,7,8]:
        print("zomer")
    elif maand in [9,10,11]:
        print("herfst")

seizoen(5)
