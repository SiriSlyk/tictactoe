import random


class Spillet:
    def __init__(self):
        self.SPILLBRETT = [["-", "-", "-", ], ["-", "-", "-", ], ["-", "-", "-"]] #[[None, None, None, ], [None, None, None, ], [None, None, None]]
        self.SYMBOL = ["X", "O"]
        self.spillerID = 0

    def plasser(self, x_koor, y_koor):
        if self.SPILLBRETT[x_koor][y_koor] == "-":
            self.SPILLBRETT[x_koor][y_koor] = self.SYMBOL[self.spillerID]
            self.nesteSpiller()
            return True
        return False

    def nesteSpiller(self):
        if self.spillerID == 0:
            self.spillerID = 1
        else:
            self.spillerID = 0

    def skrivBrett(self):
        print("-" * 10)
        print(self.SPILLBRETT[0][0], self.SPILLBRETT[0][1], self.SPILLBRETT[0][2])
        print(self.SPILLBRETT[1][0], self.SPILLBRETT[1][1], self.SPILLBRETT[1][2])
        print(self.SPILLBRETT[2][0], self.SPILLBRETT[2][1], self.SPILLBRETT[2][2])

    def sjekkVinner(self):
        for i in range(3):
            # HORISONTALT
            if self.SPILLBRETT[i][0] == self.SPILLBRETT[i][1] and self.SPILLBRETT[i][0] == self.SPILLBRETT[i][2] and self.SPILLBRETT[i][1] == self.SPILLBRETT[i][2] and self.SPILLBRETT[i][0] != "-":
                return True, self.SPILLBRETT[0][0], [[i, 0], [i, 1], [i, 2]]

            # VERTIKALT
            if self.SPILLBRETT[0][i] == self.SPILLBRETT[1][i] and self.SPILLBRETT[0][i] == self.SPILLBRETT[2][i] and self.SPILLBRETT[1][i] == self.SPILLBRETT[2][i] and self.SPILLBRETT[0][i] != "-":
                return True, self.SPILLBRETT[0][i], [[0, i], [1, i], [2, i]]
            # DIAGONALT
        if self.SPILLBRETT[0][0] == self.SPILLBRETT[1][1] and self.SPILLBRETT[0][0] == self.SPILLBRETT[2][2] and self.SPILLBRETT[1][1] == self.SPILLBRETT[2][2] and self.SPILLBRETT[0][0] != "-":
            return True, self.SPILLBRETT[0][0], [[0, 0], [1, 1], [2, 2]]
        if self.SPILLBRETT[0][2] == self.SPILLBRETT[1][1] and self.SPILLBRETT[0][2] == self.SPILLBRETT[2][0] and self.SPILLBRETT[1][1] == self.SPILLBRETT[2][0] and self.SPILLBRETT[0][2] != "-":
            return True, self.SPILLBRETT[1][1], [[0, 2], [1, 1], [2, 0]]
        return False, None, None


    def sjekkUavgjort(self):
        for i in range(len(self.SPILLBRETT)):
            for j in range(len(self.SPILLBRETT)):
                if self.SPILLBRETT[i][j] == "-":
                    return False
        return True

    def resetSpillet(self):
        self.SPILLBRETT = [["-", "-", "-", ], ["-", "-", "-", ], ["-", "-", "-"]]
        self.spillerID = 0
        #run()

def spilleIgjen():
    svarene = ["ja", "nei"]
    svar = ""
    while svar not in svarene:
        svar = input("Vil dere spillet på nytt(ja/nei):")
        svar.lower()
    if svar == "ja":
        spill.resetSpillet()
        return True
    else:
        return False

def run():
    spill.skrivBrett()
    while True:
        runner = False
        while not runner:
            x = random.randint(0, 2)
            y = random.randint(0, 2)
            runner = spill.plasser(x, y)
        spill.skrivBrett()
        svar, symbol, trengerIkke = spill.sjekkVinner()
        if svar:
            print("_" * 10)
            print(f"{symbol} vant")
            print("_" * 10)
            spill.resetSpillet()
            break
        if spill.sjekkUavgjort():
            print("Det ble uavgjort")
            spilleIgjen()
            break


if __name__ == '__main__':
    spill = Spillet()
    run()
