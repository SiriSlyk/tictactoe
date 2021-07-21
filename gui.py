import tkinter
from tkinter import messagebox

import main
from main import *

spill = Spillet()

WIDTH = 600
HEIGTH = 600

#RGB FARGER
RED = "#%02x%02x%02x" % (255, 64, 0)
GREEN = "#%02x%02x%02x" % (52, 235, 67)
BLUE = "#%02x%02x%02x" % (78, 221, 237)

FARGER = [RED, GREEN, BLUE]
navnFarger= ["Rød", "Grønn"]



class GUI:
    def __init__(self):
        self.hovedvindu = tkinter.Tk()
        self.hovedvindu.title("Tic Tac Toe")
        self.lerret = tkinter.Canvas(self.hovedvindu, width=WIDTH, height=HEIGTH)
        self.lerret.create_rectangle(0, 0, WIDTH, HEIGTH)  # , fill="gray")
        self.lerret.pack()
        self.teller = 0

        # Lager rutene:
        for i in range(3):
            self.lerret.create_line(HEIGTH / 3 * i, 0, HEIGTH / 3 * i, HEIGTH)

        for i in range(3):
            self.lerret.create_line(0, WIDTH / 3 * i, WIDTH, WIDTH / 3 * i)

        # Actions:
        self.lerret.bind("<Button>", self.klikk_rute)

        # MAINLOOP

        tkinter.mainloop()

    def spillePaaNytt(self, melding):
        messageSvar = tkinter.messagebox.askquestion("Melding", f"{melding} Vil dere spille en gang til?")
        if messageSvar == "yes":
            spill.resetSpillet()
            self.lerret.create_rectangle(0, 0, WIDTH, HEIGTH, fill="white")
            for i in range(3):
                self.lerret.create_line(HEIGTH / 3 * i, 0, HEIGTH / 3 * i, HEIGTH)

            for i in range(3):
                self.lerret.create_line(0, WIDTH / 3 * i, WIDTH, WIDTH / 3 * i)
        else:
            self.hovedvindu.destroy()



    def klikk_rute(self, hendelse):
        tallx = int(hendelse.x / 200)
        tally = int(hendelse.y / 200)

        if spill.plasser(tallx, tally):
            print(f"{tallx}, {tally}")
            self.lerret.create_rectangle(200 * tallx, 200 * tally, 200 * (tallx + 1), 200 * (tally + 1), fill=FARGER[spill.spillerID])
            svar, symbol, hvorMatrix = spill.sjekkVinner()
            if svar:
                print(f"{symbol} vant!")
                for i in hvorMatrix:
                    self.lerret.create_rectangle(200 * i[0], 200 * i[1], 200 * (i[0] + 1), 200 * (i[1] + 1), fill=FARGER[2])
                self.spillePaaNytt(f"{navnFarger[spill.spillerID]} vant!")

            if spill.sjekkUavgjort():
                self.spillePaaNytt("Det ble uavgjort!")



        else:
            print("Denne plassen er allerde tatt")


if __name__ == '__main__':
    gui = GUI()
