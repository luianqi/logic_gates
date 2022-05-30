import pygame
import time
import itertools

pygame.init()

width = 1022
height = 766

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
yellow = (255, 241, 13)
gray = (190, 190, 190)

gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption("logic gates")
clock = pygame.time.Clock()

exitgame = False
gates = []
outputGateNumber = 0
truthTableInputs = []
truthTableTypes = []
tableHeaders = False
createPreSetDone = False
currentBoxPosition = -200
currentGateMoving = " "


def messageDisplay(text, x, y, size):
    large_text = pygame.font.Font("freesansbold.ttf", size)
    TextSurf, TextRect = textObjects(text, large_text)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)


def textObjects(text, font):
    textsurface = font.render(text, True, black)
    return textsurface, textsurface.get_rect()


def mouseMoving(x, y, mouseDown):
    clickStatus = (pygame.mouse.get_pressed())[0]
    (xPos, yPos) = pygame.mouse.get_pos()
    if not mouseDown:
        if (x - 25) < xPos < (x + 25) and (y - 25) < yPos < (y + 25):
            if clickStatus == 1:
                mouseDown = True
                return xPos, yPos, mouseDown
            else:
                return x, y, mouseDown
        else:
            return x, y, mouseDown
    elif mouseDown:
        if clickStatus == 1:
            return xPos, yPos, mouseDown
        else:
            mouseDown = False
            return x, y, mouseDown


def buttonClick(x, y):
    clickStatus = (pygame.mouse.get_pressed())[0]
    (xPos, yPos) = pygame.mouse.get_pos()
    if (x) < xPos < (x + 150) and (y) < yPos < (y + 30):
        if clickStatus == 1:
            return True


def gateClick(xStart, yStart, nmX):
    (xPos, yPos) = pygame.mouse.get_pos()
    if (xStart - 20) < xPos < (xStart + 20) and (yStart - 20) < yPos < (
            yStart + 20
    ):
        if ((pygame.mouse.get_pressed())[0]) == 1:
            if nmX == 1:
                nmX = 0
            elif nmX == 0:
                nmX = 1
            time.sleep(0.075)
    return nmX


class Not(object):
    """not gate"""

    def __init__(self):
        self.nm1 = 1
        self.nm2 = 1
        self.nm1Connected = False
        self.nm2Connected = False
        self.connected = False
        self.output = False
        self.x = 30
        self.y = 80
        self.Not = pygame.image.load("pics/not.png")
        self.mouseDown = False

        self.xStart = self.x
        self.yStart = self.y + 60

        self.xEnd = self.x + 200
        self.yEnd = self.y + 60

    def position(self, currentGateMoving):
        if currentGateMoving == "not" or currentGateMoving == " ":
            self.x, self.y, self.mouseDown = mouseMoving(
                self.x, self.y, self.mouseDown
            )
        if self.mouseDown:
            currentGateMoving = "not"
        elif (self.mouseDown == False) and (currentGateMoving == "not"):
            currentGateMoving = " "
        gameDisplay.blit(self.Not, (self.x, self.y))
        return currentGateMoving

    def numbersatpoints(self):
        if self.nm1 == 1:
            self.nm2 = 0
        elif self.nm1 == 0:
            self.nm2 = 1

        self.xStart = self.x
        self.yStart = self.y + 60
        self.xEnd = self.x + 200
        self.yEnd = self.y + 60

        messageDisplay(str(self.nm1), self.xStart, self.yStart, 30)
        messageDisplay(str(self.nm2), self.xEnd, self.yEnd, 30)

    def click(self):
        self.nm1 = gateClick(self.xStart, self.yStart, self.nm1)


class And(object):
    """and gate"""

    def __init__(self):
        self.nm1 = 0
        self.nm2 = 1
        self.nm3 = 0
        self.nm1Connected = False
        self.nm2Connected = False
        self.nm3Connected = False
        self.connected = False
        self.output = False
        self.x = 30
        self.y = 210
        self.And = pygame.image.load("pics/and.png")
        self.mouseDown = False

        self.x1Start = self.x
        self.y1Start = self.y + 30

        self.x2Start = self.x
        self.y2Start = self.y + 90

        self.xEnd = self.x + 200
        self.yEnd = self.y + 60

    def position(self, currentGateMoving):
        if currentGateMoving == "and" or currentGateMoving == " ":
            self.x, self.y, self.mouseDown = mouseMoving(
                self.x, self.y, self.mouseDown
            )
        if self.mouseDown:
            currentGateMoving = "and"
        elif (self.mouseDown == False) and (currentGateMoving == "and"):
            currentGateMoving = " "
        gameDisplay.blit(self.And, (self.x, self.y))
        return currentGateMoving

    def numbersatpoints(self):
        if self.nm1 == 1 and self.nm2 == 1:
            self.nm3 = 1
        else:
            self.nm3 = 0

        self.x1Start = self.x
        self.y1Start = self.y + 30
        self.x2Start = self.x
        self.y2Start = self.y + 190
        self.xEnd = self.x + 200
        self.yEnd = self.y + 60

        messageDisplay(str(self.nm1), self.x1Start, self.y1Start, 30)
        messageDisplay(str(self.nm2), self.x2Start, self.y2Start, 30)
        messageDisplay(str(self.nm3), self.xEnd, self.yEnd, 30)

    def click(self):
        self.nm1 = gateClick(self.x1Start, self.y1Start, self.nm1)
        self.nm2 = gateClick(self.x2Start, self.y2Start, self.nm2)


class Or(object):
    """or gate"""

    def __init__(self):
        self.nm1 = 0
        self.nm2 = 1
        self.nm3 = 1
        self.nm1Connected = False
        self.nm2Connected = False
        self.nm3Connected = False
        self.connected = False
        self.output = False
        self.x = 30
        self.y = 410
        self.Or = pygame.image.load("pics/or.png")
        self.mouseDown = False

        self.x1Start = self.x
        self.y1Start = self.y + 30

        self.x2Start = self.x
        self.y2Start = self.y + 90

        self.xEnd = self.x + 200
        self.yEnd = self.y + 60

    def position(self, currentGateMoving):
        if currentGateMoving == "or" or currentGateMoving == " ":
            self.x, self.y, self.mouseDown = mouseMoving(
                self.x, self.y, self.mouseDown
            )
        if self.mouseDown:
            currentGateMoving = "or"
        elif (self.mouseDown == False) and (currentGateMoving == "or"):
            currentGateMoving = " "
        gameDisplay.blit(self.Or, (self.x, self.y))
        return currentGateMoving

    def numbersatpoints(self):
        if self.nm1 == 1 or self.nm2 == 1:
            self.nm3 = 1
        else:
            self.nm3 = 0

        self.x1Start = self.x
        self.y1Start = self.y + 30
        self.x2Start = self.x
        self.y2Start = self.y + 155
        self.xEnd = self.x + 200
        self.yEnd = self.y + 60

        messageDisplay(str(self.nm1), self.x1Start, self.y1Start, 30)
        messageDisplay(str(self.nm2), self.x2Start, self.y2Start, 30)
        messageDisplay(str(self.nm3), self.xEnd, self.yEnd, 30)

    def click(self):
        self.nm1 = gateClick(self.x1Start, self.y1Start, self.nm1)
        self.nm2 = gateClick(self.x2Start, self.y2Start, self.nm2)


class Xor(object):
    """xor gate"""

    def __init__(self):
        self.nm1 = 0
        self.nm2 = 1
        self.nm3 = 1
        self.nm1Connected = False
        self.nm2Connected = False
        self.nm3Connected = False
        self.connected = False
        self.output = False
        self.x = 30
        self.y = 580
        self.Xor = pygame.image.load("pics/xor.png")
        self.mouseDown = False

        self.x1Start = self.x
        self.y1Start = self.y + 30

        self.x2Start = self.x
        self.y2Start = self.y + 90

        self.xEnd = self.x + 200
        self.yEnd = self.y + 60

    def position(self, currentGateMoving):
        if currentGateMoving == "xor" or currentGateMoving == " ":
            self.x, self.y, self.mouseDown = mouseMoving(
                self.x, self.y, self.mouseDown
            )
        if self.mouseDown:
            currentGateMoving = "xor"
        elif (self.mouseDown == False) and (currentGateMoving == "xor"):
            currentGateMoving = " "
        gameDisplay.blit(self.Xor, (self.x, self.y))
        return currentGateMoving

    def numbersatpoints(self):
        if self.nm1 == 1 or self.nm2 == 1:
            self.nm3 = 1
            if self.nm1 == 1 and self.nm2 == 1:
                self.nm3 = 0
        else:
            self.nm3 = 0

        self.x1Start = self.x
        self.y1Start = self.y + 30
        self.x2Start = self.x
        self.y2Start = self.y + 130
        self.xEnd = self.x + 200
        self.yEnd = self.y + 60

        messageDisplay(str(self.nm1), self.x1Start, self.y1Start, 30)
        messageDisplay(str(self.nm2), self.x2Start, self.y2Start, 30)
        messageDisplay(str(self.nm3), self.xEnd, self.yEnd, 30)

    def click(self):
        self.nm1 = gateClick(self.x1Start, self.y1Start, self.nm1)
        self.nm2 = gateClick(self.x2Start, self.y2Start, self.nm2)


def connectionCheck(gate1, gate2):
    if gate1.__class__.__name__ == "Not" and gate2.__class__.__name__ == "Not":
        if (
                gate2.xStart - 10 < gate1.xEnd < gate2.xStart + 10
                and gate2.yStart - 10 < gate1.yEnd < gate2.yStart + 10
        ):
            gate2.nm1 = gate1.nm2
            gate1.nm2Connected = True
            gate2.nm1Connected = True
            xDifference = gate1.xEnd - gate2.xStart
            yDifference = gate1.yEnd - gate2.yStart
            gate2.x = gate2.x + xDifference
            gate2.y = gate2.y + yDifference
    elif gate1.__class__.__name__ == "Not":
        if (
                gate2.x1Start - 10 < gate1.xEnd < gate2.x1Start + 10
                and gate2.y1Start - 10 < gate1.yEnd < gate2.y1Start + 10
        ):
            gate2.nm1 = gate1.nm2
            gate1.nm2Connected = True
            gate2.nm1Connected = True
            xDifference = gate1.xEnd - gate2.x1Start
            yDifference = gate1.yEnd - gate2.y1Start
            gate2.x = gate2.x + xDifference
            gate2.y = gate2.y + yDifference
        if (
                gate2.x2Start - 10 < gate1.xEnd < gate2.x2Start + 10
                and gate2.y2Start - 10 < gate1.yEnd < gate2.y2Start + 10
        ):
            gate2.nm2 = gate1.nm2
            gate1.nm2Connected = True
            gate2.nm2Connected = True
            xDifference = gate1.xEnd - gate2.x2Start
            yDifference = gate1.yEnd - gate2.y2Start
            gate2.x = gate2.x + xDifference
            gate2.y = gate2.y + yDifference
    elif gate2.__class__.__name__ == "Not":
        if (
                gate2.xStart - 10 < gate1.xEnd < gate2.xStart + 10
                and gate2.yStart - 10 < gate1.yEnd < gate2.yStart + 10
        ):
            gate2.nm1 = gate1.nm3
            gate1.nm3Connected = True
            gate2.nm1Connected = True
            xDifference = gate1.xEnd - gate2.xStart
            yDifference = gate1.yEnd - gate2.yStart
            gate2.x = gate2.x + xDifference
            gate2.y = gate2.y + yDifference
    else:
        if (
                gate2.x1Start - 10 < gate1.xEnd < gate2.x1Start + 10
                and gate2.y1Start - 10 < gate1.yEnd < gate2.y1Start + 10
        ):
            gate2.nm1 = gate1.nm3
            gate1.nm3Connected = True
            gate2.nm1Connected = True
            xDifference = gate1.xEnd - gate2.x1Start
            yDifference = gate1.yEnd - gate2.y1Start
            gate2.x = gate2.x + xDifference
            gate2.y = gate2.y + yDifference
        if (
                gate2.x2Start - 10 < gate1.xEnd < gate2.x2Start + 10
                and gate2.y2Start - 10 < gate1.yEnd < gate2.y2Start + 10
        ):
            gate2.nm2 = gate1.nm3
            gate1.nm3Connected = True
            gate2.nm2Connected = True
            xDifference = gate1.xEnd - gate2.x2Start
            yDifference = gate1.yEnd - gate2.y2Start
            gate2.x = gate2.x + xDifference
            gate2.y = gate2.y + yDifference
    return (gate1, gate2)


def outputNumberRight(gates, outputGateNumber):
    currentBiggestX = 0
    for gate in gates:
        if gate.connected:
            if gate.xEnd > currentBiggestX:
                currentBiggestX = gate.xEnd
                if gate.__class__.__name__ == "Not":
                    outputGateNumber = gate.nm2
                    gate.output = True
                else:
                    outputGateNumber = gate.nm3
                    gate.output = True
    return gates, outputGateNumber


def tableCreation(gates, truthTableInputs, truthTableTypes):
    truthTableInputs = []
    truthTableTypes = []
    alphabet = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    alphabetCount = 0
    tempGates = []
    for i in gates:
        if i.connected:
            tempGates.append(i)
    tempGates = gateOrdering(tempGates)
    for i in tempGates:
        if not i.nm1Connected:
            truthTableInputs.append(i.nm1)
            truthTableTypes.append(alphabet[alphabetCount])
            alphabetCount = alphabetCount + 1
        if not i.nm2Connected:
            if not (i.output == True and i.__class__.__name__ == "Not"):
                truthTableInputs.append(i.nm2)
                truthTableTypes.append(alphabet[alphabetCount])
                alphabetCount = alphabetCount + 1
        if not (i.__class__.__name__ == "Not"):
            if not i.nm3Connected:
                if not (i.output == True):
                    truthTableInputs.append(i.nm3)
                    truthTableTypes.append(alphabet[alphabetCount])
                    alphabetCount = alphabetCount + 1
    return truthTableInputs, truthTableTypes


def deleteFile(file):
    file.seek(0)
    file.truncate()


def gatesReset(gates):
    gates[0].x = 30
    gates[0].y = 210
    gates[1].x = 30
    gates[1].y = 410
    gates[2].x = 30
    gates[2].y = 80
    gates[3].x = 30
    gates[3].y = 580
    for i in range(len(gates))[4::]:
        gates[i].x = -300
        gates[i].y = 1000


def preSetGates(gates):
    num_lines = sum(1 for line in open("Pre-set.txt"))
    preMadeGates = open("Pre-set.txt", "r+")
    boxPosition = 20
    currentLineNumber = 0
    allLines = preMadeGates.readlines()
    lineNumber = 0
    andCount = 0
    orCount = 0
    notCount = 0
    xorCount = 0
    global currentBoxPosition
    pygame.draw.rect(gameDisplay, gray, (320, currentBoxPosition, 150, 30), 0)
    for i in range(num_lines):
        pygame.draw.rect(gameDisplay, black, (320, boxPosition, 150, 30), 4)
        currentLineSplitted = allLines[lineNumber].split()
        messageDisplay(str(currentLineSplitted[0]), 390, boxPosition + 15, 19)

        if buttonClick(320, boxPosition):
            currentBoxPosition = boxPosition
            positionInLine = 1
            gates.append(And())
            gates.append(Or())
            gates.append(Not())
            gates.append(Xor())
            gatesReset(gates)

            for gate in currentLineSplitted[1::3]:
                if gate == "and" or gate == "And":
                    gates[andCount].x = int(
                        currentLineSplitted[positionInLine + 1]
                    )
                    gates[andCount].y = int(
                        currentLineSplitted[positionInLine + 2]
                    )
                    andCount = andCount + 4
                if gate == "or" or gate == "Or":
                    gates[orCount + 1].x = int(
                        currentLineSplitted[positionInLine + 1]
                    )
                    gates[orCount + 1].y = int(
                        currentLineSplitted[positionInLine + 2]
                    )
                    orCount = orCount + 4
                if gate == "not" or gate == "Not":
                    gates[notCount + 2].x = int(
                        currentLineSplitted[positionInLine + 1]
                    )
                    gates[notCount + 2].y = int(
                        currentLineSplitted[positionInLine + 2]
                    )
                    notCount = notCount + 4
                if gate == "xor" or gate == "Xor":
                    gates[xorCount + 3].x = int(
                        currentLineSplitted[positionInLine + 1]
                    )
                    gates[xorCount + 3].y = int(
                        currentLineSplitted[positionInLine + 2]
                    )
                    xorCount = xorCount + 4
                positionInLine = positionInLine + 3

        if (pygame.mouse.get_pressed())[2] == 1:
            (xPos, yPos) = pygame.mouse.get_pos()
            if (320) < xPos < (470) and (boxPosition) < yPos < (
                    boxPosition + 30
            ):
                file = open("Pre-set.txt", "r+")
                lines = file.readlines()
                print(lines)
                print(lineNumber)
                lines.pop(lineNumber)
                deleteFile(file)
                for item in lines:
                    file.write(item)
                return
        boxPosition = boxPosition + 30
        lineNumber = lineNumber + 1
    if len(gates) > 7:
        gates = gates[0:8]


def createPreSet(gates):
    truthtable = open("Pre-set.txt", "a")
    count = 0
    if len(gates) > 8:
        gates = gates[0:8]
        gameDisplay.fill(white)
        messageDisplay(
            "you can't have more than 2 gates of the same type being added into the pre-sets",
            500,
            300,
            25,
        )
        pygame.display.update()
        time.sleep(1.5)
        return gates
    for gate in gates:
        if gate.connected:
            count = count + 1
    if count < 2:
        messageDisplay(
            "you have to have 2 or more gates connected", 600, 300, 25
        )
        pygame.display.update()
        time.sleep(1.5)
        return gates
    truthtable.write("user_Pre-set")
    for gate in gates:
        if gate.connected:
            truthtable.write(
                " "
                + gate.__class__.__name__
                + " "
                + str(gate.x)
                + " "
                + str(gate.y)
            )
    truthtable.write("\n")
    return gates


def gateOrdering(gates):
    for i in range(len(gates)):
        for j in range(len(gates) - 1 - i):
            if gates[j].x > gates[j + 1].x:
                gates[j], gates[j + 1] = gates[j + 1], gates[j]
    return gates


def helpScreen():
    pygame.draw.polygon(
        gameDisplay,
        gray,
        (
            (330, 600),
            (400, 500),
            (400, 570),
            (530, 570),
            (530, 630),
            (400, 630),
            (400, 700),
        ),
    )
    pygame.draw.polygon(
        gameDisplay,
        gray,
        (
            (770, 100),
            (830, 170),
            (790, 170),
            (790, 300),
            (750, 300),
            (750, 170),
            (710, 170),
        ),
    )
    pygame.draw.polygon(
        gameDisplay,
        gray,
        (
            (400, 130),
            (460, 200),
            (420, 200),
            (420, 385),
            (380, 385),
            (380, 200),
            (340, 200),
        ),
    )
    messageDisplay("This is where the gates are stored", 755, 580, 15)
    messageDisplay(
        "click and hold on the top corner to move them", 755, 600, 15
    )
    messageDisplay(
        "click on the input number to change that number", 755, 620, 15
    )
    messageDisplay("press R to reset and M to create more gates", 755, 640, 15)
    messageDisplay(
        "M will only work if you have moved all the gates out of the starting area",
        755,
        660,
        15,
    )
    messageDisplay(
        "This is where the truth table will be displayed", 755, 315, 15
    )
    messageDisplay("when at least two gates are connected", 755, 335, 15)
    messageDisplay(
        "press c to create a complete truth table in a file called truthTable",
        755,
        355,
        15,
    )
    messageDisplay(
        "to create it you have to exit the program for it to save to the file",
        755,
        375,
        15,
    )
    messageDisplay("This is where the pre-set gates are", 460, 400, 15)
    messageDisplay(
        "you can left click on the gates to select them", 460, 420, 15
    )
    messageDisplay(
        "right click to remove them and press x to create your own",
        460,
        440,
        15,
    )


gates.append(And())
gates.append(Or())
gates.append(Not())
gates.append(Xor())

while not (exitgame):
    gameDisplay.fill(white)
    pygame.draw.line(gameDisplay, black, (250, 0), (250, 800), 8)
    preSetGates(gates)
    for gate in gates:
        currentGateMoving = gate.position(currentGateMoving)
        gate.numbersatpoints()
        gate.click()

    for firstGate in gates:
        for secondGate in gates:
            firstGate, secondGate = connectionCheck(firstGate, secondGate)

    gates, outputGateNumber = outputNumberRight(gates, outputGateNumber)

    for gate in gates:
        if gate.__class__.__name__ == "Not":
            if gate.nm1Connected == True or gate.nm2Connected == True:
                gate.connected = True
            else:
                gate.connected = False
        else:
            if (
                    gate.nm1Connected == True
                    or gate.nm2Connected == True
                    or gate.nm3Connected == True
            ):
                gate.connected = True
            else:
                gate.connected = False

    numberOfOutputs = 0
    for gate in gates:
        if gate.connected:
            if gate.__class__.__name__ == "Not":
                if not gate.nm2Connected:
                    numberOfOutputs = numberOfOutputs + 1
            else:
                if not gate.nm3Connected:
                    numberOfOutputs = numberOfOutputs + 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                gatesReset(gates)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                gateSamePlace = 0
                for i in range(len(gates))[::4]:
                    if not (gates[i].x == 30 and gates[i].y == 210):
                        if not (
                                gates[i + 1].x == 30 and gates[i + 1].y == 410
                        ):
                            if not (
                                    gates[i + 2].x == 30 and gates[i + 2].y == 80
                            ):
                                if not (
                                        gates[i + 3].x == 30
                                        and gates[i + 3].y == 580
                                ):
                                    gateSamePlace = gateSamePlace + 1
                if gateSamePlace >= (len(gates)) / 4:
                    gates.append(And())
                    gates.append(Or())
                    gates.append(Not())
                    gates.append(Xor())
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                if (not (createPreSetDone) == True) and (numberOfOutputs == 1):
                    gates = createPreSet(gates)
                    createPreSetDone = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                if numberOfOutputs == 1:
                    truthtable = open("truthTable.txt", "w")
                    totalinputs = 0
                    inputsArray = []
                    inputstypeArray = []
                    deleteFile(truthtable)
                    for i in gates:
                        if i.connected == True:
                            if i.__class__.__name__ == "Not":
                                i.nm1 = 0
                                i.nm2 = 0
                                if i.nm1Connected == False:
                                    inputsArray.append(i)
                                    inputstypeArray.append(1)
                            else:
                                i.nm1 = 0
                                i.nm2 = 0
                                i.nm3 = 0
                                if i.nm1Connected == False:
                                    inputsArray.append(i)
                                    inputstypeArray.append(1)
                                if i.nm2Connected == False:
                                    inputsArray.append(i)
                                    inputstypeArray.append(2)
                    pretruthtable = list(
                        itertools.product([0, 1], repeat=(len(inputsArray)))
                    )
                    for i in range(len(pretruthtable)):
                        for leninputarray in range(len(inputsArray)):
                            if inputstypeArray[leninputarray] == 1:
                                inputsArray[leninputarray].nm1 = pretruthtable[
                                    i
                                ][leninputarray]
                            if inputstypeArray[leninputarray] == 2:
                                inputsArray[leninputarray].nm2 = pretruthtable[
                                    i
                                ][leninputarray]

                        gameDisplay.fill(white)
                        for gate in gates:
                            currentGateMoving = gate.position(
                                currentGateMoving
                            )
                            gate.numbersatpoints()
                            gate.click()
                            pygame.display.update()

                        for firstGate in gates:
                            for secondGate in gates:
                                firstGate, secondGate = connectionCheck(
                                    firstGate, secondGate
                                )

                        gameDisplay.fill(white)
                        for gate in gates:
                            currentGateMoving = gate.position(
                                currentGateMoving
                            )
                            gate.numbersatpoints()
                            gate.click()
                            pygame.display.update()
                        clock.tick(5)
                        pygame.display.update()

                        truthTableInputs, truthTableTypes = tableCreation(
                            gates, truthTableInputs, truthTableTypes
                        )
                        gates, outputGateNumber = outputNumberRight(
                            gates, outputGateNumber
                        )
                        print(truthTableTypes)
                        print(truthTableInputs, "  //   Q:", outputGateNumber)
                        if tableHeaders == False:
                            for item in truthTableTypes:
                                truthtable.write((str(item)) + "    ,    ")
                            tableHeaders = True
                        truthtable.write("\n")
                        for item in truthTableInputs:
                            truthtable.write(str(item) + "    ,    ")
                        truthtable.write("      Q: " + str(outputGateNumber))
                        truthtable.write("\n")

                else:
                    if numberOfOutputs > 1:
                        gameDisplay.fill(white)
                        messageDisplay(
                            "you can only have one circuit at a time when creating a truth table",
                            511,
                            300,
                            20,
                        )
                        pygame.display.update()
                        time.sleep(3.5)
                    elif numberOfOutputs < 1:
                        gameDisplay.fill(white)
                        messageDisplay(
                            "you need to have at least one logic circuit to create a truth table",
                            511,
                            300,
                            20,
                        )
                        pygame.display.update()
                        time.sleep(3.5)

    truthTableInputs, truthTableTypes = tableCreation(
        gates, truthTableInputs, truthTableTypes
    )
    if numberOfOutputs == 1:
        messageDisplay((str(truthTableInputs)), 770, 60, 20)
        messageDisplay((" Q: " + str(outputGateNumber)), 770, 80, 20)
        messageDisplay(str(truthTableTypes), 770, 40, 20)
    else:
        messageDisplay("too many circuits or too few", 770, 60, 20)

    pygame.draw.rect(gameDisplay, red, (860, 723, 150, 30), 0)
    messageDisplay("HELP", 935, 740, 30)
    if buttonClick(860, 723) == True:
        helpScreen()

    for i in gates:
        if i.__class__.__name__ == "Not":
            i.nm1Connected = False
            i.nm2Connected = False
        else:
            i.nm1Connected = False
            i.nm2Connected = False
            i.nm3Connected = False
        i.output = False

    outputGateNumber = 0
    truthTableInputs = []
    truthTableTypes = []

    pygame.display.update()
    clock.tick(60)
