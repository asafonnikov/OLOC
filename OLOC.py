enableErrorInvaildSyntax = True


import time


def htd(val):
    if val == "0" or val == "1" or val == "2" or val == "3" or val == "4" or val == "5" or val == "6" or val == "7" or val == "8" or val == "9":
        return(int(val))
    elif val == "a" or val == "A":
        return(10)
    elif val == "b" or val == "B":
        return(11)
    elif val == "c" or val == "C":
        return(12)
    elif val == "d" or val == "D":
        return(13)
    elif val == "e" or val == "E":
        return(14)
    elif val == "f" or val == "F":
        return(15)
    else:
        return(-1)

def condTrue(comm, pc, juby):
    if comm == "c" or comm == "C":
        return(pc + juby)
    if comm == "d" or comm == "D":
        return(pc - juby)

def run(rom, TPS):
    reg = [0, 0, 0, 0, 0, 0]
    pc = 0
    opc = 0
    tpc = 0
    while True:
        opc = pc
        if len(rom) > pc:
            comm = rom[pc]
            print("0x", rom[pc], sep="")
        else:
            return(-1)
        if len(comm) != 4:
            return(pc)
        if comm == "help" or comm == "Help" or comm == "HELP":
            print("Saturn NX Features\nCommand bus: 16-bit\nMaximum PPROM capacity: 131072 bytes\nNumber of registers: 6x8 bit\nMax. number of external devices: 10\n\n0x0Y?X - Copy X to Y\n0x4OXY - Calculate the O with X and Y and write it in register 0\n0x8XVV - Write V to X\n0xCNXY - Go to condition N with X to cell PC+Y\n0xDNXY - Conditional N to X to cell PC-Y\n\nALU operations:\n0 - AND\n1 - OR\n2 - XOR\n3 - NOT\n4 - NAND\n5 - NOR\n6 - XNOR\n7 - NOP\n8 - ADD\n9 - SUB\nA - MUL UPPER\nB - MUL LOWER\nC - SHL\nD - SHR\nE - ASHL\nF - BIT\n\nConditional transitions:\n0 - NEVER\n1 - EQUAL 0\n2 - LESS 0\n3 - LESS OR EQUAL 0\n4 - ALWAYS\n5 - NOT EQUAL 0\n6 - GREATHER OR EQUAL 0\n7 - GREATHER 0")
            continue
        # Copy
        elif comm[0] == "0":
            if htd(comm[1]) < 6 and htd(comm[3]) < 6:
                reg[htd(comm[1])] = reg[htd(comm[3])]
        # Calculate
        elif comm[0] == "4":
            if comm[1] == "0":
                if htd(comm[2]) < 6 and htd(comm[3]) < 6:
                    reg[0] = reg[htd(comm[2])] & reg[htd(comm[3])]
            if comm[1] == "1":
                if htd(comm[2]) < 6 and htd(comm[3]) < 6:
                    reg[0] = reg[htd(comm[2])] | reg[htd(comm[3])]
            if comm[1] == "2":
                if htd(comm[2]) < 6 and htd(comm[3]) < 6:
                     reg[0] = reg[htd(comm[2])] ^ reg[htd(comm[3])]
            if comm[1] == "3":
                if htd(comm[2]) < 6 and htd(comm[3]) < 6:
                   reg[0] = reg[htd(comm[2])] ^ 255
            if comm[1] == "4":
                if htd(comm[2]) < 6 and htd(comm[3]) < 6:
                    reg[0] = (reg[htd(comm[2])] & reg[htd(comm[3])]) ^ 255
            if comm[1] == "5":
                if htd(comm[2]) < 6 and htd(comm[3]) < 6:
                    reg[0] = (reg[htd(comm[2])] | reg[htd(comm[3])]) ^ 255
            if comm[1] == "6":
                if htd(comm[2]) < 6 and htd(comm[3]) < 6:
                    reg[0] = (reg[htd(comm[2])] ^ reg[htd(comm[3])]) ^ 255
            if comm[1] == "7":
                if htd(comm[2]) < 6 and htd(comm[3]) < 6:
                    reg[0] = reg[htd(comm[2])]
            if comm[1] == "8":
                if htd(comm[2]) < 6 and htd(comm[3]) < 6:
                    reg[0] = reg[htd(comm[2])] + reg[htd(comm[3])]
            if comm[1] == "9":
                if htd(comm[2]) < 6 and htd(comm[3]) < 6:
                    reg[0] = reg[htd(comm[2])] - reg[htd(comm[3])]
            if comm[1] == "a" or comm[1] == "A":
                if htd(comm[2]) < 6 and htd(comm[3]) < 6:
                    reg[0] = (reg[htd(comm[2])] * reg[htd(comm[3])]) >> 8
            if comm[1] == "b" or comm[1] == "B":
                if htd(comm[2]) < 6 and htd(comm[3]) < 6:
                    reg[0] = (reg[htd(comm[2])] * reg[htd(comm[3])]) & 255
            if comm[1] == "c" or comm[1] == "C":
                if htd(comm[2]) < 6 and htd(comm[3]) < 6:
                    reg[0] = reg[htd(comm[2])] << reg[htd(comm[3])]
            if comm[1] == "d" or comm[1] == "D":
                if htd(comm[2]) < 6 and htd(comm[3]) < 6:
                    reg[0] = reg[htd(comm[2])] >> reg[htd(comm[3])]
            if comm[1] == "e" or comm[1] == "E":
                if htd(comm[2]) < 6 and htd(comm[3]) < 6:
                    reg[0] = reg[htd(comm[2])] << reg[htd(comm[3])]
            if comm[1] == "f" or comm[1] == "F":
                if htd(comm[2]) < 6 and htd(comm[3]) < 6:
                    reg[0] = int((1 << reg[htd(comm[3])]) & reg[htd(comm[2])] == 0)
        # Immedate
        elif comm[0] == "8":
            if htd(comm[1]) < 6:
                reg[htd(comm[1])] = htd(comm[3]) + (htd(comm[2]) * 16)
        # Condition
        elif comm[0] == "c" or comm[0] == "C" or  comm[0] == "d" or  comm[0] == "D":
            pc -= 1
            if comm[1] == "1":
                if reg[htd(comm[2])] == 0:
                    if htd(comm[2]) < 6 and htd(comm[3]) < 6:
                       pc = condTrue(comm[0], pc, reg[htd(comm[3])])
            elif comm[1] == "2":
                if reg[htd(comm[2])] > 127:
                    if htd(comm[2]) < 6 and htd(comm[3]) < 6:
                       pc = condTrue(comm[0], pc, reg[htd(comm[3])])
            elif comm[1] == "3":
                   if reg[htd(comm[2])] > 127 or reg[htd(comm[2])] == 0:
                       if htd(comm[2]) < 6 and htd(comm[3]) < 6:
                           pc = condTrue(comm[0], pc, reg[htd(comm[3])])
            elif comm[1] == "4":
                if True:
                    if htd(comm[2]) < 6 and htd(comm[3]) < 6:
                       pc = condTrue(comm[0], pc, reg[htd(comm[3])])
            elif comm[1] == "5":
                if reg[htd(comm[2])] != 0:
                    if htd(comm[2]) < 6 and htd(comm[3]) < 6:
                       pc = condTrue(comm[0], pc, reg[htd(comm[3])])
            elif comm[1] == "6":
                if reg[htd(comm[2])] < 128:
                    if htd(comm[2]) < 6 and htd(comm[3]) < 6:
                       pc = condTrue(comm[0], pc, reg[htd(comm[3])])
            elif comm[1] == "7":
                if reg[htd(comm[2])] < 128 and reg[htd(comm[2])] != 0:
                    if htd(comm[2]) < 6 and htd(comm[3]) < 6:
                       pc = condTrue(comm[0], pc, reg[htd(comm[3])])
                       
        # Display info and detect overflows
        for _ in range(6):
            if reg[_] < 0:
                print("Registr", _, "unflow!")
                reg[_] += 255
            if reg[_] > 255:
                print("Registr", _, "overflow!")
                reg[_] -= 255
        print("Registrs:", reg[0], reg[1], reg[2], reg[3], reg[4], reg[5])
        if pc < 0:
            print("PC unflow!")
            pc += 65535
        if pc > 65535:
            print("PC overflow!")
            pc -= 65535
        print("PC:", pc)
        pc += 1
        time.sleep(1 / TPS)
        if pc == opc:
            tpc += 1
        if tpc == (5 * TPS):
            if input("Is too long without yieldind, send 'q' if you wan exit") == "q":
                return(-2)
            else:
                tpc = 0

def chkDev(inp):
    if inp == "r" or inp == "R" or inp == "d" or inp == "D":
        return(True)
    else:
        return(False)

def dth(val):
    if val < 10:
        return(str(val))
    elif val == 10:
        return("A")
    elif val == 11:
        return("B")
    elif val == 12:
        return("C")
    elif val == 13:
        return("D")
    elif val == 14:
        return("E")
    elif val == 15:
        return("F")

def ifCond(symb, couNum, reg0, reg1):
    if htd(reg0) == -1:
        reg0 = "0"
    if symb == "+":
        return("C" + couNum + reg0 + reg1)
    elif symb == "-":
        return("D" + couNum + reg0 + reg1)
    else:
        exit("Syntax error")
        time.sleep(0.1)




prom = []
helpAdress = "N/A"
cali = []



print("OLOC v0.5 compilator for architecture Saturn NX, powered by SNXEE v0.9")
comFile = open(input("File path: "), 'r')
print("Opening file")
f = comFile.readlines()
print("Loading file to mem")
comFile.close()
print("Close file")
print(f"Lines in file: {len(f)}")
for _ in range(len(f)):
    print("Analyze line", _ + 1)
    # Empty line
    if len(f[_]) < 2:
        print("Line", _ + 1, "is too short/empty")
    # # is first symbol
    elif f[_][0] == "#":
        print("Line", _ + 1, "is commentary")
    # No operation command
    elif f[_][0] + f[_][1] + f[_][2] == "nop" or f[_][0] + f[_][1] + f[_][2] == "Nop" or f[_][0] + f[_][1] + f[_][2] == "NOP":
        print("No Operation at line", _ + 1)
        prom.append("c000")
        cali.append(_)
    # Copy command
    elif chkDev(f[_][0]) and htd(f[_][1]) != -1 and f[_][3] == "=" and chkDev(f[_][5]) and htd(f[_][6]) != -1:
        print("Copy command at line", _ + 1)
        prom.append("0" + str(f[_][1]) + "0" + str(f[_][6]))
        cali.append(_)
    # Immedate command
    elif chkDev(f[_][0]) and htd(f[_][1]) != -1 and f[_][3] == "=":
        print("Immedate command at line", _ + 1)
        prom.append("8" + str(f[_][1]) + str(dth(int(int(f[_][5] + f[_][6] + f[_][7]) / 16))) + str(dth(int(f[_][5] + f[_][6] + f[_][7]) & 15)))
        cali.append(_)
    # Calculate command
    elif chkDev(f[_][0]) and htd(f[_][1]) != -1 and chkDev(f[_][6]) and htd(f[_][7]) != -1:
        if f[_][3] + f[_][4] == "&&":
            prom.append("4" + "0" + str(f[_][1]) + str(f[_][7]))
        elif f[_][3] + f[_][4] == "||":
            prom.append("4" + "1" + str(f[_][1]) + str(f[_][7]))
        elif f[_][3] + f[_][4] == "^^":
            prom.append("4" + "2" + str(f[_][1]) + str(f[_][7]))
        elif f[_][3] + f[_][4] == "!!":
            prom.append("4" + "3" + str(f[_][1]) + str(f[_][7]))
        elif f[_][3] + f[_][4] == "!&":
            prom.append("4" + "4" + str(f[_][1]) + str(f[_][7]))
        elif f[_][3] + f[_][4] == "!|":
            prom.append("4" + "5" + str(f[_][1]) + str(f[_][7]))
        elif f[_][3] + f[_][4] == "!^":
            prom.append("4" + "6" + str(f[_][1]) + str(f[_][7]))
        elif f[_][3] + f[_][4] == "++":
            prom.append("4" + "8" + str(f[_][1]) + str(f[_][7]))
        elif f[_][3] + f[_][4] == "--":
            prom.append("4" + "9" + str(f[_][1]) + str(f[_][7]))
        elif f[_][3] + f[_][4] == "U*" or f[_][3] + f[_][4] == "u*":
            prom.append("4" + "A" + str(f[_][1]) + str(f[_][7]))
        elif f[_][3] + f[_][4] == "L*" or f[_][3] + f[_][4] == "l*":
            prom.append("4" + "B" + str(f[_][1]) + str(f[_][7]))
        elif f[_][3] + f[_][4] == ">>":
            prom.append("4" + "C" + str(f[_][1]) + str(f[_][7]))
        elif f[_][3] + f[_][4] == "<<":
            prom.append("4" + "D" + str(f[_][1]) + str(f[_][7]))
        elif f[_][3] + f[_][4] == "><":
            prom.append("4" + "E" + str(f[_][1]) + str(f[_][7]))
        elif f[_][3] + f[_][4] == "%%":
            prom.append("4" + "F" + str(f[_][1]) + str(f[_][7]))
        else:
            print("Invaild operation on line", _ + 1)
            if enableErrorInvaildSyntax == True:
                input("Press enter to continue")
                exit("Invaild operation on line " + str(_ + 1))
            time.sleep(0.1)
            continue
        print("Calculate command at line", _ + 1)
        cali.append(_)
    elif (f[_][0] + f[_][1] == "if" or f[_][0] + f[_][1] == "If" or f[_][0] + f[_][1] == "IF") and chkDev(f[_][12]) and htd(f[_][13]) != -1:
        print("Condition at line", _ + 1)
        if f[_][6] + f[_][7] + f[_][8] + f[_][9] == "ER  " or f[_][6] + f[_][7] + f[_][8] + f[_][9] == "er  ":
            prom.append(ifCond(f[_][11], "0", f[_][4], f[_][13]))
        elif f[_][6] + f[_][7] + f[_][8] + f[_][9] == "== 0":
            prom.append(ifCond(f[_][11], "1", f[_][4], f[_][13]))
        elif f[_][6] + f[_][7] + f[_][8] + f[_][9] == "<= 0":
            prom.append(ifCond(f[_][11], "2", f[_][4], f[_][13]))
        elif f[_][6] + f[_][7] + f[_][8] + f[_][9] == "<< 0":
            prom.append(ifCond(f[_][11], "3", f[_][4], f[_][13]))
        elif f[_][6] + f[_][7] + f[_][8] + f[_][9] == "AYS " or f[_][6] + f[_][7] + f[_][8] + f[_][9] == "ays ":
            prom.append(ifCond(f[_][11], "4", f[_][4], f[_][13]))
        elif f[_][6] + f[_][7] + f[_][8] + f[_][9] == "!= 0":
            prom.append(ifCond(f[_][11], "5", f[_][4], f[_][13]))
        elif f[_][6] + f[_][7] + f[_][8] + f[_][9] == ">> 0":
            prom.append(ifCond(f[_][11], "6", f[_][4], f[_][13]))
        elif f[_][6] + f[_][7] + f[_][8] + f[_][9] == ">= 0":
            prom.append(ifCond(f[_][11], "7", f[_][4], f[_][13]))
        else:
            print("Invaild condition on line", _ + 1)
            if enableErrorInvaildSyntax == True:
                input("Press enter to continue")
                exit("Invaild condition on line " + str(_ + 1))
            time.sleep(0.1)
            continue
        cali.append(_)
    # If unkown
    else:
        print("Invaild syntax on line", _ + 1)
        if enableErrorInvaildSyntax == True:
            input("Press enter to continue")
            exit("Invaild syntax on line " + str(_ + 1))
        time.sleep(0.1)
        continue
    if len(prom) != 0 and len(prom[len(prom) - 1]) != 4:
        print("Unkown error in compilator, please send line", _ + 1, "from your prgramm to", helpAdress)
        input("Press enter to continue")
        exit("Unkown error in compilator")
    elif len(prom) != 0:
        for _2 in range(4):
            if htd(prom[len(prom) - 1][_2]) == -1:
                print("Unkown error in compilator, please send line", _ + 1, "from your prgramm to", helpAdress)
                input("Press enter to continue")
                exit("Unkown error in compilator")
            
        
    

print("Compile complete!")
while True:
    srom = []
    irom = ""
    print("0 - Show machine code")
    print("1 - Run in emulator")
    print("2 - Save")
    print("q - Quit")
    tmp0 = input()
    if tmp0 == "0":
        print(prom)
    elif tmp0 == "1":
        tmp0 = run(prom, float(input("Ticks per second: ")))
        if tmp0 > 0:
            print("Unkown error in compilator, please send line", tmp0, "from your prgramm to", helpAdress)
            input("Press enter to continue")
            exit("Unkown error in compilator")
        elif tmp0 == -2:
            print("Emulator intercupped")
    elif tmp0 == "2":
#        print("0 - Save in .rom/.hdd format (!UNSTABLE!)")
        print("1 - Save in assembly format")
        print("2 - Save in assembly foramt with commentaries")
        tmp0 = input()
        srom = []
        print("Making a list with programm")
        if False:
            print(len(prom), "Instruction in file")
            for _ in range(len(prom)):
                print('Analyze instruction', _)
                srom += str(chr(htd(prom[_][0])) + (chr(htd(prom[_][1]) * 16))) + str(chr(htd(prom[_][2])) + (chr(htd(prom[_][3]) * 16)))
        elif tmp0 == "1":
            for _ in range(len(prom)):
                print('Analyze instruction', _)
                srom.append("0x" + prom[_][0] + prom[_][1] + prom[_][2] + prom[_][3])
        elif tmp0 == "2":
            for _ in range(len(prom)):
                print('Analyze instruction', _)
                srom.append("0x" + prom[_][0] + prom[_][1] + prom[_][2] + prom[_][3] + " # " + f[cali[_]])
        print("List complited")
        print("Convering to string")
        for _ in range(len(srom)):
            irom += srom[_]
            if tmp0 == "":
                irom += "\n"
            print("Converting byte", _)
        buildfile = open(input('Save file name: '), 'w', encoding="utf-8")
        print("File openninng")
        buildfile.write(irom)
        print("Saving data")
        buildfile.close()
        print("Clossing file")
    elif tmp0 == "q":
        exit()
