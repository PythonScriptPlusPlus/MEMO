from tkinter import *
from random import *

check1 = False
check2 = False
check3 = False
check4 = False
check5 = False
check6 = False
check7 = False
check8 = False
check9 = False
check10 = False
check11 = False
check12 = False
first = ''
second = ''

tk = Tk()


def but1():
    global HidNum1
    global num1
    global first
    global second
    global check1

    if HidNum1 == num1 and check1 == False:
        HidNum1 = ''
        B1['text'] = HidNum1
    else:
        HidNum1 = num1
        B1['text'] = HidNum1
        if first != '':
            second = HidNum1
        else:
            first = HidNum1
        if first != '' and second != '':
            if first == second:
                check1 = True
                first, second = '', ''


def but2():
    global HidNum2
    global num2
    global first
    global second
    global check2

    if HidNum2 == num2 and check2 == False:
        HidNum2 = ''
        B2['text'] = HidNum2
    else:
        HidNum2 = num2
        B2['text'] = HidNum2
        if first != '':
            second = HidNum2
        else:
            first = HidNum2
        if first != '' and second != '':
            if first == second:
                check2 = True
                first, second = '', ''

def but3():
    global HidNum3
    global num3
    global first
    global second
    global check3

    if HidNum3 == num3 and check3 == False:
        HidNum3 = ''
        B3['text'] = HidNum3
    else:
        HidNum3 = num3
        B3['text'] = HidNum3
        if first != '':
            second = HidNum3
        else:
            first = HidNum3
        if first != '' and second != '':
            if first == second:
                check3 = True
                first, second = '', ''

def but4():
    global HidNum4
    global num4
    global first
    global second
    global check4

    if HidNum4 == num4 and check4 == False:
        HidNum4 = ''
        B4['text'] = HidNum4
    else:
        HidNum4 = num4
        B4['text'] = HidNum4
        if first != '':
            second = HidNum4
        else:
            first = HidNum4
        if first != '' and second != '':
            if first == second:
                check4 = True
                first, second = '', ''

def but5():
    global HidNum5
    global num5
    global first
    global second
    global check5

    if HidNum5 == num5 and check5 == False:
        HidNum5 = ''
        B5['text'] = HidNum5
    else:
        HidNum5 = num5
        B5['text'] = HidNum5
        if first != '':
            second = HidNum5
        else:
            first = HidNum5
        if first != '' and second != '':
            if first == second:
                check5= True
                first, second = '', ''

def but6():
    global HidNum6
    global num6
    global first
    global second
    global check6

    if HidNum6 == num6 and check6 == False:
        HidNum6 = ''
        B6['text'] = HidNum6
    else:
        HidNum6 = num6
        B6['text'] = HidNum6
        if first != '':
            second = HidNum6
        else:
            first = HidNum6
        if first != '' and second != '':
            if first == second:
                check6 = True
                first, second = '', ''

def but7():
    global HidNum7
    global num7
    global first
    global second
    global check7

    if HidNum7 == num7 and check7 == False:
        HidNum7 = ''
        B7['text'] = HidNum7
    else:
        HidNum7 = num7
        B7['text'] = HidNum7
        if first != '':
            second = HidNum7
        else:
            first = HidNum7
        if first != '' and second != '':
            if first == second:
                check7 = True
                first, second = '', ''

def but8():
    global HidNum8
    global num8
    global first
    global second
    global check8

    if HidNum8 == num8 and check8 == False:
        HidNum8 = ''
        B8['text'] = HidNum8
    else:
        HidNum8 = num8
        B8['text'] = HidNum8
        if first != '':
            second = HidNum8
        else:
            first = HidNum8
        if first != '' and second != '':
            if first == second:
                check8 = True
                first, second = '', ''

def but9():
    global HidNum9
    global num9
    global first
    global second
    global check9

    if HidNum9 == num9 and check9 == False:
        HidNum9 = ''
        B9['text'] = HidNum9
    else:
        HidNum9 = num9
        B9['text'] = HidNum9
        if first != '':
            second = HidNum9
        else:
            first = HidNum9
        if first != '' and second != '':
            if first == second:
                check9 = True
                first, second = '', ''

def but10():
    global HidNum10
    global num10
    global first
    global second
    global check10

    if HidNum10 == num10 and check10 == False:
        HidNum10 = ''
        B10['text'] = HidNum10
    else:
        HidNum10 = num10
        B10['text'] = HidNum10
        if first != '':
            second = HidNum10
        else:
            first = HidNum10
        if first != '' and second != '':
            if first == second:
                check10 = True
                first, second = '', ''

def but11():
    global HidNum11
    global num11
    global first
    global second
    global check11

    if HidNum11 == num11 and check11 == False:
        HidNum11 = ''
        B11['text'] = HidNum11
    else:
        HidNum11 = num11
        B11['text'] = HidNum11
        if first != '':
            second = HidNum11
        else:
            first = HidNum11
        if first != '' and second != '':
            if first == second:
                check11 = True
                first, second = '', ''

def but12():
    global HidNum12
    global num12
    global first
    global second
    global check12

    if HidNum12 == num12 and check12 == False:
        HidNum12 = ''
        B12['text'] = HidNum12
    else:
        HidNum12 = num12
        B12['text'] = HidNum12
        if first != '':
            second = HidNum12
        else:
            first = HidNum12
        if first != '' and second != '':
            if first == second:
                check12 = True
                first, second = '', ''
##########----BACK-END----#########

listP = ['1','2','3','4','5','6','1','2','3','4','5','6']
listN = []

for i in range(0,12):
    num = randint(0,(11-i))
    word = listP.pop(num)
    listN.append(word)

HidNum1 = ''
HidNum2 = ''
HidNum3 = ''
HidNum4 = ''
HidNum5 = ''
HidNum6 = ''
HidNum7 = ''
HidNum8 = ''
HidNum9 = ''
HidNum10 = ''
HidNum11 = ''
HidNum12 = ''

num1 = listN.pop(0)
num2 = listN.pop(0)
num3 = listN.pop(0)
num4 = listN.pop(0)
num5 = listN.pop(0)
num6 = listN.pop(0)
num7 = listN.pop(0)
num8 = listN.pop(0)
num9 = listN.pop(0)
num10 = listN.pop(0)
num11 = listN.pop(0)
num12 = listN.pop(0)

#########----FRONT-END----#########


############################################################
header = Label(tk, text = 'MEMORY', width = 17, height = 5)#
B1 = Button(tk, text = HidNum1, width = 17,                #
            height = 5, command = but1)                    #
B2 = Button(tk, text = HidNum2, width = 17,                #
            height = 5, command = but2)                    #
B3 = Button(tk, text = HidNum3, width = 17,                #
            height = 5, command = but3)                    #
B4 = Button(tk, text = HidNum4, width = 17,                #
            height = 5, command = but4)                    #
############################################################
B5 = Button(tk, text = HidNum5, width = 17,                #
            height = 5, command = but5)                    #
B6 = Button(tk, text = HidNum6, width = 17,                #
            height = 5, command = but6)                    #
B7 = Button(tk, text = HidNum7, width = 17,                #
            height = 5, command = but7)                    #
B8 = Button(tk, text = HidNum8, width = 17,                #
            height = 5, command = but8)                    #
############################################################
B9 = Button(tk, text = HidNum9, width = 17,                #
            height = 5, command = but9)                    #
B10 = Button(tk, text = HidNum10, width = 17,              #
             height = 5, command = but10)                  #
B11 = Button(tk, text = HidNum11, width = 17,              #
             height = 5, command = but11)                  #
B12 = Button(tk, text = HidNum12, width = 17,              #
             height = 5, command = but12)                  #
############################################################
                                                       ###
                                                    ###
                                                 ###
                                              ###
                                           ###
                                        ###
                                     ###
                                  ###
                               ###
###############################
header.grid(row = 0,          #
            column = 0,       #
            columnspan = 4)   #
###############################
B1.grid(row = 1, column = 0)  #
B2.grid(row = 1, column = 1)  #
B3.grid(row = 1, column = 2)  #
B4.grid(row = 1, column = 3)  #
###############################
B5.grid(row = 2, column = 0)  #
B6.grid(row = 2, column = 1)  #
B7.grid(row = 2, column = 2)  #
B8.grid(row = 2, column = 3)  #
###############################
B9.grid(row = 3, column = 0)  #
B10.grid(row = 3, column = 1) #
B11.grid(row = 3, column = 2) #
B12.grid(row = 3, column = 3) #
###############################

tk.mainloop()
