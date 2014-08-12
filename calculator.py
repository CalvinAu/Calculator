#===============================================================================
# calculator.py
# Calvin Au
# 8/11/14
#===============================================================================
from Tkinter import *

class Calculator:
    '''GUI for the calculator'''
    def __init__(self, master):
        self.master = master #master reachable from outside
        
        self.stringContents = '' #Contains the numbers inputted in string format
        self.displayStr = StringVar(self.stringContents)
        self.display = Label(master, textvariable=self.displayStr, width=25, anchor=E, relief=SUNKEN).grid(row=0, columnspan=4)
        
        self.modContents = '' #Contains expression modifier in string format
        self.displayMod = StringVar(self.modContents)
        self.modShow = Label(master, textvariable=self.displayMod, anchor=E).grid(row=1, column=3, columnspan=4)
        
        self.point  = Button(master, width=3, text='.', command=lambda: self.printNum('.')).grid(row=5, column=1)
        self.zero   = Button(master, width=3, text='0', command=lambda: self.printNum('0')).grid(row=5, column=0)
        self.one    = Button(master, width=3, text='1', command=lambda: self.printNum('1')).grid(row=4, column=0)
        self.two    = Button(master, width=3, text='2', command=lambda: self.printNum('2')).grid(row=4, column=1)
        self.three  = Button(master, width=3, text='3', command=lambda: self.printNum('3')).grid(row=4, column=2)
        self.four   = Button(master, width=3, text='4', command=lambda: self.printNum('4')).grid(row=3, column=0)
        self.five   = Button(master, width=3, text='5', command=lambda: self.printNum('5')).grid(row=3, column=1)
        self.six    = Button(master, width=3, text='6', command=lambda: self.printNum('6')).grid(row=3, column=2)
        self.seven  = Button(master, width=3, text='7', command=lambda: self.printNum('7')).grid(row=2, column=0)
        self.eight  = Button(master, width=3, text='8', command=lambda: self.printNum('8')).grid(row=2, column=1)
        self.nine   = Button(master, width=3, text='9', command=lambda: self.printNum('9')).grid(row=2, column=2)
        
        self.c      = Button(master, width=3, text='C', command=lambda: self.clear()).grid(row=6, column=3)
        self.times  = Button(master, width=3, text='x', command=lambda: self.modify('x')).grid(row=2, column=3)
        self.div    = Button(master, width=3, text='/', command=lambda: self.modify('/')).grid(row=3, column=3)
        self.plus   = Button(master, width=3, text='+', command=lambda: self.modify('+')).grid(row=4, column=3)
        self.minus  = Button(master, width=3, text='-', command=lambda: self.modify('-')).grid(row=5, column=3)
        self.equals = Button(master, width=3, text='=', command=lambda: self.evaluate(self.expression)).grid(row=5, column=2)
        
        #Dictionary containing expression parts to be evaluated
        self.expression = {'left':None, 'modifier':None, 'right':None}

    def printNum(self, num):
        '''Displays the inputted num onto the display''' 
        if self.stringContents.find('0') == 0:
            self.stringContents = '' #leading zeroes chopped off
        
        if num == '.' and '.' in self.stringContents: return #prevent multiple '.'
        self.stringContents += num
        self.displayStr.set(self.stringContents)

    def modify(self, modifier):          
        if self.stringContents == '' and self.expression['left'] != None:
            #Simply change the modifier (code at end)
            pass
        elif self.stringContents == '' and self.expression['left'] == None:
            #Default left expression to 0 and display it on the calculator
            self.expression['left'] = 0
            self.printNum('0')
            self.stringContents = '' #reset the stringContents
        elif self.expression['modifier'] == None or \
            (self.stringContents != '' and self.expression['left'] == None):
            #Store the number into the left
            self.expression['left'] = self.stringContents
            self.stringContents = ''
        elif self.stringContents != '' and self.expression['left'] != None:
            #Evaluate and pass in modifier to be able to
            #string together expressions
            self.evaluate(self.expression, modifier)
            
        self.modContents = modifier
        self.expression['modifier'] = modifier
        self.displayMod.set(self.modContents)

    def evaluate(self, expression, modifier = None):
        '''Evalutes the expression'''
        if self.expression['left'] == None or self.stringContents == '':
            pass #incomplete expression
        else:
            self.expression['right'] = self.stringContents
            self.stringContents = ''
            equals = 0
            if expression['modifier'] == 'x':
                equals = float(expression['left']) * float(expression['right'])
            elif expression['modifier'] == '/':
                equals = float(expression['left']) / float(expression['right'])
            elif expression['modifier'] == '+':
                equals = float(expression['left']) + float(expression['right'])
            else:
                equals = float(expression['left']) - float(expression['right'])
            
            if equals == int(equals):
                equals = int(equals) #Formatting
                
            self.expression['left'] = equals
            self.expression['right'] = None
            if modifier != None: #Makes it possible to string expressions together
                self.expression['modifier'] = modifier
                self.modContents = modifier
            else:
                self.expression['modifier'] = None
                self.modContents = ''
                
            self.displayMod.set(self.modContents)
            self.displayStr.set(str(equals))
            self.stringContents = ''
            
    def clear(self):
        '''Clears the expression'''
        self.expression['left'] = None
        self.expression['right'] = None
        self.expression['modifier'] = None
        self.modContents = ''
        self.stringContents = ''
        self.displayStr.set(self.stringContents)
        self.displayMod.set(self.modContents)
      
root = Tk()
calculator = Calculator(root)
calculator.master.resizable(False, False)
calculator.master.title('Calculator')
root.mainloop()