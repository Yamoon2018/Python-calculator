#!/usr/bin/python3

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from numpy import *

class Calculator:

    
    def __init__(self, master):
        
        master.title('My Calculator')
        master.resizable(False, False)
        master.configure(background = '#e1d8b9')
        master.columnconfigure(0 , weight=3)
        master.rowconfigure(0 , weight=3)
        
        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#e1d8b9')
        self.style.configure('TButton', background = '#e1d8b9')
        self.style.configure('TLabel', background = '#e1d8b9')
        self.header_label_style  = self.style.configure('Header.TLabel') 
        
        self.pad_x = 0
        self.pad_y = 0
        #Binding numbers and all signs to Master to use Keybaord for calculation
        master.bind_all('<Escape>', lambda e:self.clear(), '+')
        master.bind('<KP_1>',  lambda e:self.submit(1) , '+')
        master.bind('<KeyPress-1>',  lambda e:self.submit(1) , '+')
        master.bind('<KeyPress-2>',  lambda e:self.submit(2), '+')
        master.bind('<KeyPress-3>',  lambda e:self.submit(3), '+')
        master.bind('<KeyPress-4>',  lambda e:self.submit(4), '+')
        master.bind('<KeyPress-5>',  lambda e:self.submit(5), '+')
        master.bind('<KeyPress-6>',  lambda e:self.submit(6), '+')
        master.bind('<KeyPress-7>',  lambda e:self.submit(7), '+')
        master.bind('<KeyPress-8>',  lambda e:self.submit(8), '+')
        master.bind('<KeyPress-9>',  lambda e:self.submit(9), '+')
        master.bind('<KeyPress-0>',  lambda e:self.submit(0), '+')
        master.bind('<KP_2>',  lambda e:self.submit(2), '+')
        master.bind('<KP_3>',  lambda e:self.submit(3), '+')
        master.bind('<KP_4>',  lambda e:self.submit(4), '+')
        master.bind('<KP_5>',  lambda e:self.submit(5), '+')
        master.bind('<KP_6>',  lambda e:self.submit(6), '+')
        master.bind('<KP_7>',  lambda e:self.submit(7), '+')
        master.bind('<KP_8>',  lambda e:self.submit(8), '+')
        master.bind('<KP_9>',  lambda e:self.submit(9), '+')
        master.bind('<KP_0>',  lambda e:self.submit(0), '+')
        master.bind('<Return>',      lambda e:self.submit('='), '+')
        master.bind('<KP_Enter>',      lambda e:self.submit('='), '+')
        #master.bind('<KP_Add>',  lambda e:self.submit('+'), '+')
        master.bind('<plus>',  lambda e:self.submit('+'), '+')
        master.bind('<KP_Multiply>',  lambda e:self.submit('*'), '+')
        master.bind('<asterisk>',  lambda e:self.submit('*'), '+')
        master.bind('<KP_Subtract>',  lambda e:self.submit('-'), '+')
        master.bind('<minus>',  lambda e:self.submit('-'), '+')
        master.bind('<KP_Divide>',  lambda e:self.submit('/'), '+')
        master.bind('<slash>',  lambda e:self.submit('/'), '+')
        master.bind('<BackSpace>',  lambda e:self.submit('BackSpace'), '+')

        self.result     = StringVar()
        self.result_str = ""
        
        
        #Frame to display calculator screen only
        self.Screeen_frame = ttk.Frame(master)
        self.Screeen_frame.pack()
        
        self.Screen_area = Label(self.Screeen_frame, width=34, height=2, textvariable=self.result, style = self.header_label_style, font = ('Arial', 20, 'bold'), relief=SUNKEN, borderwidth=5)
        self.Screen_area.grid(row =0, column=0, columnspan=2)
        
        #End frame display
        
        #Frame for all calculator buttons
        self.Content_frame = ttk.Frame(master)
        self.Content_frame.pack()
        self.Num_1 = Button(self.Content_frame, text='1', command=lambda :self.submit(1))
        self.Num_2 = Button(self.Content_frame, text='2', command=lambda :self.submit(2) )
        self.Num_3 = Button(self.Content_frame, text='3', command=lambda :self.submit(3) )
        self.Num_4 = Button(self.Content_frame, text='4', command=lambda :self.submit(4) )
        self.Num_5 = Button(self.Content_frame, text='5', command=lambda :self.submit(5) )
        self.Num_6 = Button(self.Content_frame, text='6', command=lambda :self.submit(6) )
        self.Num_7 = Button(self.Content_frame, text='7', command=lambda :self.submit(7) )
        self.Num_8 = Button(self.Content_frame, text='8', command=lambda :self.submit(8) )
        self.Num_9 = Button(self.Content_frame, text='9', command=lambda :self.submit(9) )
        self.Num_0 = Button(self.Content_frame, text='0', command=lambda :self.submit(0) )
        self.Num_C = Button(self.Content_frame, text='C', command= self.clear )
        self.Num_equal = Button(self.Content_frame, text='=',command=lambda :self.submit('=') )
        self.Num_plus = Button(self.Content_frame, text='+',command=lambda :self.submit('+') )
        self.Num_multi = Button(self.Content_frame, text='X',command=lambda :self.submit('*') )
        self.Num_minus = Button(self.Content_frame, text='-',command=lambda :self.submit('-') )
        self.Num_divid = Button(self.Content_frame, text='/',command=lambda :self.submit('/') )
        self.Num_Backspace = Button(self.Content_frame, text='BackSpace',command=lambda :self.submit('BackSpace'))
        self.Num_SQRT      = Button(self.Content_frame, text='SQRT',command=lambda :self.submit('SQRT'))
        
        self.Num_1.grid(row=0, column=0, stick='n', padx = self.pad_x, pady = self.pad_y, ipadx = 16, ipady = 11)
        self.Num_2.grid(row=0, column=1, stick='n', padx = self.pad_x, pady = self.pad_y, ipadx = 16, ipady = 11)
        self.Num_3.grid(row=0, column=2, stick='n',padx = self.pad_x, pady = self.pad_y, ipadx = 16, ipady = 11)
        self.Num_4.grid(row=1, column=0, stick='n',padx = self.pad_x, pady = self.pad_y, ipadx = 16, ipady = 11)
        self.Num_5.grid(row=1, column=1, stick='n', padx = self.pad_x, pady = self.pad_y, ipadx = 16, ipady = 11)
        self.Num_6.grid(row=1, column=2, stick='n', padx = self.pad_x, pady = self.pad_y, ipadx = 16, ipady = 11)
        self.Num_7.grid(row=2, column=0, stick='n', padx = self.pad_x, pady = self.pad_y, ipadx = 16, ipady = 11)
        self.Num_8.grid(row=2, column=1, stick='n', padx = self.pad_x, pady = self.pad_y, ipadx = 16, ipady = 11)
        self.Num_9.grid(row=2, column=2, stick='n',padx = self.pad_x, pady = self.pad_y, ipadx = 16, ipady = 11)
        self.Num_0.grid(row=3, column=1, stick='n',padx = self.pad_x, pady = self.pad_y, ipadx = 16, ipady = 11)
        self.Num_C.grid(row=3, column=0, stick='n', padx = self.pad_x, pady = self.pad_y, ipadx = 16, ipady = 11)
        self.Num_equal.grid(row=3, column=2, stick='n', padx = 0, pady = 0, ipadx = 15, ipady = 11)
        self.Num_plus.grid(row=0, column=3, stick='n',padx = self.pad_x, pady = self.pad_y, ipadx = 16, ipady = 11)
        self.Num_multi.grid(row=1, column=3, stick='n', padx = self.pad_x, pady = self.pad_y, ipadx = 16, ipady = 11)
        self.Num_minus.grid(row=2, column=3, stick='n', padx = self.pad_x, pady = self.pad_y, ipadx = 18, ipady = 11)
        self.Num_divid.grid(row=3, column=3, stick='n',padx = self.pad_x, pady = self.pad_y, ipadx = 18, ipady = 11)
        self.Num_Backspace.grid(row=0, column=4, columnspan=2, stick='n', padx = self.pad_x, pady = self.pad_y,ipadx = 16, ipady = 11)
        self.Num_SQRT.grid(row=1, column=4, columnspan=2, ipadx = 35, ipady = 10,padx = 0, pady = 0, stick='n')
        #End frame for all calculator buttons
        
    #Submit function to do all operation + * / - then save in self.result_str as string, then display it by using self.resulf
    def submit(self,num):
            if (num == '='):
                num = str(eval(self.result_str))
                self.result.set(num)
            elif(num=='BackSpace'):
                self.result_str = self.result_str[0:-1]
                self.result.set(self.result_str)
        
            elif(num == 'SQRT'):
                num = str(eval(self.result_str))
                self.result.set(sqrt(float(eval(num))))
                
            else:
                self.result_str += str(num)                
                self.result.set(self.result_str)
    
    def clear(self):
        self.result.set("")
        self.result_str =""
         
def main():            
    
    root = Tk()
    feedback = Calculator(root)
    root.mainloop()
    
if __name__ == "__main__": main()
