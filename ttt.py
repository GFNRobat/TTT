feld = [["---","---","---",],["---","---","---",],["---","---","---",]]
spieler = "X"
done = 0

def check():
    global done
    for i in range(3):
        if feld[i][0] == feld[i][1] == feld[i][2] == "-X-":
            done = 1
        elif feld[0][i] == feld[1][i] == feld[2][i] == "-X-":
            done = 1
        elif feld[0][0] == feld[1][1] == feld[2][2] == "-X-":
            done = 1
        elif feld[0][2] == feld[1][1] == feld[2][0] == "-X-":
            done = 1
        elif feld[i][0] == feld[i][1] == feld[i][2] == "-O-":
            done = 1
        elif feld[0][i] == feld[1][i] == feld[2][i] == "-O-":
            done = 1
        elif feld[0][0] == feld[1][1] == feld[2][2] == "-O-":
            done = 1
        elif feld[0][2] == feld[1][1] == feld[2][0] == "-O-":
            done = 1

def pos():
    zahl = int(input("Spieler " + spieler + " ist an der Reihe\n"))
    if zahl > 0 and zahl < 10:
        y = int(zahl/3)
        x = zahl%3
        if x != 0:
           x -= 1
        else:
            x = 2
            y -= 1   
    else:
        print("Bitte Zahl zwischen 1 und 9 eingeben.") 
    if feld[y][x] == "---":
        feld[y][x] = "-" + spieler + "-"
    else:
        print("Feld belegt...bitte anderes Feld wählen")
        pos()

def reihe():
    global spieler
    if spieler == "X":
        spieler = "O"
    else:
        spieler = "X"

def play():
    count = 0
    while True:
        if count == 9:
            print("DRAW")
            break
        for row in feld:
            print(*row, sep="  |\t")
        pos()
        count += 1
        check()
        if done == 1:
            print("Spieler " + spieler + " gewinnt.")
            break
        reihe()

play()

        
