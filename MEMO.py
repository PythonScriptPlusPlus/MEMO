from tkinter import *
from random import *

first = ''
second = ''

tk = Tk()

def but(num):
    global first
    global second
    rem = num
    global rem
    if first != '':
        second = num
    if first == '':
        first = num
    if second == num:
        second = ''
        first = num
    if first == num:
        print(1)
    

##########----BACK-END----#########

listP = ['1','2','3','4','5','6','1','2','3','4','5','6']
listN = []

for i in range(0,12):
    num = randint(0,(11-i))
    word = listP.pop(num)
    listN.append(word)


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
B1 = Button(tk, text = '', width = 17, height = 5)         #
B2 = Button(tk, text = '', width = 17, height = 5)         #
B3 = Button(tk, text = '', width = 17, height = 5)         #
B4 = Button(tk, text = '', width = 17, height = 5)         #
############################################################
B5 = Button(tk, text = '', width = 17, height = 5)         #
B6 = Button(tk, text = '', width = 17, height = 5)         #
B7 = Button(tk, text = '', width = 17, height = 5)         #
B8 = Button(tk, text = '', width = 17, height = 5)         #
############################################################
B9 = Button(tk, text = '', width = 17, height = 5)         #
B10 = Button(tk, text = '', width = 17, height = 5)        #
B11 = Button(tk, text = '', width = 17, height = 5)        #
B12 = Button(tk, text = '', width = 17, height = 5)        #
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
