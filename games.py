import math
import tkinter
from tkinter import *
from math import *
from random import *
import time

root = Tk()
root.title("Cosmopol")
root.geometry("2000x1000")

my_canvas = Canvas(root, width=1000, height=1000, bg="white")
my_canvas.pack(pady=20)

centerX = 500
centerY = 500


def flip(a):
    period = 5+int(random()*5)
    frames = 200
    maxHeight = 5 / 2
    observeHeight = 5
    coinRelativeSize = 1 / 2
    sizeC = 200
    startHeight = 1
    for x in range(frames):
        height = startHeight + (maxHeight - startHeight) * (-x * (x - frames) / (frames / 2) ** 2)
        my_canvas.delete("all")
        rotSinPos = abs(math.sin(x * period * pi / (2 * frames)))
        rotCosPos = abs(math.cos(x * period * pi / (2 * frames)))
        if math.cos(x * period * math.pi / (2 * frames)) > 0:
            my_canvas.create_oval(centerX - sizeC * height, centerY - sizeC * height + abs(sizeC * height * rotSinPos),
                                  centerX + sizeC * height, centerX + sizeC * height - height * sizeC * abs(rotSinPos),
                                  fill="black")
            my_canvas.create_rectangle(centerX - sizeC / 2 * height,
                                       centerY - height * (sizeC * 3 / 4 - sizeC * 3 / 4 * rotSinPos),
                                       centerX + height * sizeC / 2,
                                       centerY - height * (sizeC / 2 - sizeC / 2 * rotSinPos), fill="red")
            my_canvas.create_rectangle(centerX - height * sizeC / 6,
                                       centerY - height * (sizeC / 2 - sizeC / 2 * rotSinPos),
                                       centerX + height * sizeC / 6,
                                       centerY + height * (sizeC * 3 / 4 - sizeC * 3 / 4 * rotSinPos), fill="red")
        else:
            my_canvas.create_oval(centerX - sizeC * height, centerY - sizeC * height + abs(sizeC * height * rotSinPos),
                                  centerX + sizeC * height, centerX + sizeC * height - height * sizeC * abs(rotSinPos),
                                  fill="red")
            my_canvas.create_rectangle(centerX - height * sizeC / 6,
                                       centerY - height * (sizeC * 3 / 4 - sizeC * 3 / 4 * rotSinPos),
                                       centerX + height * sizeC / 6,
                                       centerY + height * (sizeC * 3 / 4 - sizeC * 3 / 4 * rotSinPos), fill="black")
        root.update()
    if period % 2 == a:
        return 2
    else:
        return 0


def roulette(bet, slots, guess, colour):
    spin = 1
    frames = 100000
    startPos = 0
    for x in range(frames):
        my_canvas.delete("all")
        xRange = my_canvas.winfo_width()
        slotWidth = xRange/slots
        for x in range(slots+1):
            if x == 0:
                my_canvas.create_rectangle((x*slotWidth+startPos)%xRange, centerY-slotWidth, ((x+1)*slotWidth+startPos)%xRange,centerY+slotWidth, fill="green")
            elif x % 2 == 1:
                my_canvas.create_rectangle((x*slotWidth+startPos)%xRange, centerY-slotWidth,((x+1)*slotWidth+startPos)%xRange,centerY+slotWidth, fill="red")
            elif x % 2 == 0:
                my_canvas.create_rectangle((x*slotWidth+startPos)%xRange, centerY-slotWidth, ((x+1)*slotWidth+startPos)%xRange,centerY+slotWidth, fill="black")
        startPos += spin/frames*my_canvas.winfo_width()
        root.update()

    multiplier = 0
    return(multiplier)


def crash(bet, guess):
    # guess = input("Enter your guess: ")
    guess = float(guess)
    crashTime = random() * random() * random() * random() * 20 + 1
    adjust = 1
    scale = 100
    scales = [2, 5, 10, 20, 50, 100]
    scalePointer = 0
    for x in range(1000):

        yRange = 900
        xRange = 100
        xStart = xRange
        deriv = 1
        realHeight = 900
        height = yRange
        my_canvas.delete("all")
        for y in range(x):
            xEnd = xStart + (my_canvas.winfo_width() - xRange) / x
            my_canvas.create_line(xStart, height, xEnd, height - deriv / adjust, fill="red", width="2")
            xStart += (my_canvas.winfo_width() - xRange) / x
            realHeight = realHeight - deriv
            height = height - deriv / adjust
            deriv += 1 / 10
        my_canvas.create_line(xRange / 2, yRange, xRange / 2, 0, fill="green", width="3")

        if realHeight - my_canvas.winfo_width() < -10 * scale:
            scale = 100 * scales[scalePointer]
            scalePointer += 1
        for y in range(int(20)):
            my_canvas.create_line(xRange / 4, yRange - scale * y / adjust, xRange * 3 / 4, yRange - scale * y / adjust,
                                  fill="green", width="2")
            my_canvas.create_text(xRange / 5, yRange - scale * y / adjust, text=int(scale * y) / 1000 + 1, fill="green",
                                  width="10", anchor=tkinter.CENTER)
        if height < yRange / 2:
            adjust = 1 + 1.05 * (yRange / 2 - realHeight) / yRange
        if (realHeight - yRange) / my_canvas.winfo_height() < -crashTime + 1:
            print(f"Your guess: {guess}")
            print(f"Crash point: {crashTime}")
            if guess <= crashTime:
                my_canvas.create_text(500, 500, text=f'{bet * (guess - 1)} $ win! Keep going!', anchor=tkinter.CENTER,
                                      width="10i", fill="blue")
                print(f'{bet * (guess - 1)} $ win! Keep going!')
                return bet * (guess - 1)
            else:
                my_canvas.create_text(500, 500, text="game over", anchor=tkinter.CENTER, width="10i", fill="blue")
                root.update()
                print("Better luck next time!")
            return -bet

        root.update()
        time.sleep(1 / 20)
    if guess>crashTime:
        return(guess)
    else:
        return(0)


def probVis():
    interval = 20
    dSteps = 1000
    d = []
    calcs = 1000000
    for x in range(int(dSteps * 21 / 20)):
        d.append(0)
    for x in range(calcs):
        a = int((random() * random() * random() * 20 + 1) * dSteps / 20)
        d[a] = d[a] + 1
    compare = 0
    index = 0
    totSum = 0
    for x in reversed(range(0, dSteps)):
        totSum += d[x]
        if totSum / calcs * (x / 50 - 1) > compare:
            compare = totSum / calcs * (x / 50 - 1)
            index = x
            print(totSum / calcs)
    print(index * 1 / 50)
    print(compare)
    totSum = 0
    for x in reversed(range(0, dSteps)):
        totSum += d[x]
        my_canvas.create_line(x, 999, x, 999 - totSum / calcs * (x / 50 - 1) * 1000 / compare, fill="green")


#cash = 100
#roulette(25, 3, True)

#root.mainloop()
