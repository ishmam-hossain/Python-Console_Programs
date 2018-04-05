from tkinter import *
from django.core.management.color import Style
from textwrap import fill
import tkinter.font as font
from wheel.signatures.djbec import double
import math

# Code starts by making root frame
root = Tk()
root.title('Calculator')

#Font Style
MyFont = font.Font(weight='bold')

#Entry Field
large_font = ('Verdana',20)

txt_in = StringVar()
txt_disp = Entry(root,bg = '#53596F',fg = 'white',
                 textvariable = txt_in, justify = 'right',font=large_font)
txt_disp.pack(side = TOP,fill=X)




# Making frames


topFrame = Frame(root)
topFrame.pack(side = TOP, fill = X)

midFrame = Frame(root)
midFrame.pack(side = TOP, fill = X)

botFrame = Frame(root)
botFrame.pack(side = TOP, fill = X)

totFrame = Frame(root)
totFrame.pack(side = TOP, fill = X)

endFrame = Frame(root)
endFrame.pack(side = TOP, fill = X)



# functions


def printNum(val):
    
    if val == 'c':
        num = ''
    
    else:
        num = txt_in.get()
        num += val
        
    txt_in.set(num)
    

# operation functions goes here

def addition(values):
    res = 0    
    for val in values:
        res += val
    
    txt_in.set(res)
    

def subtract(values):

    num1 = values[0]
    num2 = values[1] 
    
    txt_in.set(num1-num2)
    
    
def multiply(values):

    res = 1   
    for val in values:
        res *= val
           
    txt_in.set(res)
    
def divide(values):
    
    num1 = values[0]
    num2 = values[1] 
    
    if num2 !=0:
        res = num1/num2
        txt_in.set(res)
        
    else:
        txt_in.set('Cannot divide by zero!')
    


def cal_percent(values):
    
    res = (values[0] * values[1]) / 100
           
    txt_in.set(res)


def square():

    res = float(txt_in.get())    
    res = res ** 2   
           
    txt_in.set(res)
    
    
def negate():

    res = float(txt_in.get())
           
    txt_in.set(res * (-1))
        
    
def cal_root():

    res = float(txt_in.get())
           
    txt_in.set(math.sqrt(res))
        

def backspace():
    res = list(txt_in.get())
    res = ''.join(res[:-1])
    
    txt_in.set(str(res))
      

# input processing
def sep_str():
    
    s = txt_in.get()
    
    if '+' in s:
        values = list(map(float, s.split('+')))
        addition(values)
        
    elif '-' in s:
        values = list(map(float, s.split('-')))
        subtract(values)
        
    elif 'x' in s:
        values = list(map(float, s.split('x')))
        multiply(values)    
    
    elif '/' in s:
        values = list(map(float, s.split('/')))
        divide(values) 
        
    elif '%' in s:
        values = list(map(float, s.split('%')))
        cal_percent(values)
          
    elif '²' in s:
        values = list(map(float, s.split('²')))
        square(values)

    elif '√' in s:
        values = list(map(float, s.split('√')))
        root(values) 
        
        
# Button Draw

btn1 = Button(topFrame,width=6,pady = 5, text="1",
              font=MyFont,bd = 5,bg = '#293241', fg = "white",
              command=lambda:printNum('1'))

btn2 = Button(topFrame,width=6,pady = 5, text="2",
              font=MyFont,bd = 5,bg = "#293241", fg = "white",
              command=lambda:printNum('2'))

btn3 = Button(topFrame,width=6,pady = 5, text="3",
              font=MyFont,bd = 5,bg = "#293241", fg = "white",
              command=lambda:printNum('3'))

btn4 = Button(topFrame,width=6,pady = 5, text="4",
              font=MyFont,bd = 5,bg = "#293241", fg = "white",
              command=lambda:printNum('4'))

btnPlus = Button(topFrame,width=6,pady = 5, text="+",
              font=MyFont,bd = 5,bg = "#293241", fg = "white",
              command=lambda:printNum('+'))



btn5 = Button(midFrame,width=6,pady = 5, text="5",
              font=MyFont,bd = 5,bg = '#293241', fg = "white",
              command=lambda:printNum('5'))

btn6 = Button(midFrame,width=6,pady = 5, text="6",
              font=MyFont,bd = 5,bg = "#293241", fg = "white",
              command=lambda:printNum('6'))

btn7 = Button(midFrame,width=6,pady = 5, text="7",
              font=MyFont,bd = 5,bg = "#293241", fg = "white",
              command=lambda:printNum('7'))

btn8 = Button(midFrame,width=6,pady = 5, text="8",
              font=MyFont,bd = 5,bg = "#293241", fg = "white",
              command=lambda:printNum('8'))

btnMinus = Button(midFrame,width=6,pady = 5, text="-",
              font=MyFont,bd = 5,bg = "#293241", fg = "white",
              command=lambda:printNum('-'))



btn9 = Button(botFrame,width=6,pady = 5, text="9",
              font=MyFont,bd = 5,bg = '#293241', fg = "white",
              command=lambda:printNum('9'))

btn0 = Button(botFrame,width=6,pady = 5, text="0",
              font=MyFont,bd = 5,bg = "#293241", fg = "white",
              command=lambda:printNum('0'))

btnC = Button(botFrame,width=6,pady = 5, text="C",
              font=MyFont,bd = 5,bg = "#293241", fg = "white",
              command=lambda:printNum('c'))

btnDot = Button(botFrame,width=6,pady = 5, text=".",
              font=MyFont,bd = 5,bg = "#293241", fg = "white",
              command=lambda:printNum('.'))

btnMul = Button(botFrame,width=6,pady = 5, text="x",
              font=MyFont,bd = 5,bg = "#293241", fg = "white",
              command=lambda:printNum('x'))



#total bottom operator signs
btnPls_mns = Button(totFrame,width=6,pady = 5, text="±",
                    font=MyFont,bd = 5,bg = '#293241', fg = "white",
              command=negate)

btnRoot = Button(totFrame,width=6,pady = 5, text="√x",
                 font=MyFont,bd = 5,bg = "#293241", fg = "white",
              command=cal_root)

btnSquare = Button(totFrame,width=6,pady = 5, text="x²",
                   font=MyFont,bd = 5,bg = "#293241", fg = "white",
              command=square)

btnPercent = Button(totFrame,width=6,pady = 5, text="%",
                    font=MyFont,bd = 5,bg = "#293241", fg = "white",
              command=lambda:printNum('%'))

btnDiv = Button(totFrame,width=6,pady = 5, text="/",
              font=MyFont,bd = 5,bg = "#293241", fg = "white",
              command=lambda:printNum('/'))


btnBackspace = Button(endFrame,width=17,pady = 5, text="<< BackSpace",
              font=MyFont,bd = 5,bg = "#293241", fg = "white",
              command=backspace)


btnEqual = Button(endFrame,width=17,pady = 5, text="=",
              font=MyFont,bd = 5,bg = "#293241", fg = "white",
              command=sep_str)



#± √x  x²
# Packing the buttons
btn1.pack(side = LEFT, fill = X)
btn2.pack(side = LEFT, fill = X)
btn3.pack(side = LEFT, fill = X)
btn4.pack(side = LEFT, fill = X)
btnPlus.pack(side = LEFT, fill = X)

btn5.pack(side = LEFT, fill = X)
btn6.pack(side = LEFT, fill = X)
btn7.pack(side = LEFT, fill = X)
btn8.pack(side = LEFT, fill = X)
btnMinus.pack(side = LEFT, fill = X)

btn9.pack(side = LEFT, fill = X)
btn0.pack(side = LEFT, fill = X)
btnDot.pack(side = LEFT, fill = X)
btnC.pack(side = LEFT, fill = X)
btnMul.pack(side = LEFT, fill = X)

btnPls_mns.pack(side = LEFT, fill = X)
btnRoot.pack(side = LEFT, fill = X)
btnSquare.pack(side = LEFT, fill = X)
btnPercent.pack(side = LEFT, fill = X)
btnDiv.pack(side = LEFT, fill = X)

btnBackspace.pack(side = LEFT, fill = X)
btnEqual.pack(side = LEFT, fill = X)




root.mainloop()



