import random
def hiscore():
    no=random.randint(1,100)
    with open("hiscore.txt","r+") as f:
        f.seek(0)
        content = f.read().strip()
        if content == "":
                f.write(str(no))
        elif int(content) < no:
                f.truncate(0)
                f.seek(0)
                f.write(str(no))
    score = content
    if score == "":
        print("No previous hiscore found.", "\n", "The  new hiscore is",no)
    elif int(content) < no:
        print("The previous hiscore is",score, "\n", "The new hiscore is",no)
    else:
         print(" no change in high score", "\n","The hiscore this time is",no ,"\n","The previous hiscore is",score)
    return score

hiscore()