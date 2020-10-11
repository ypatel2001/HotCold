from tkinter import *
window2 = Tk()
window2.minsize(width=100,height=100)
window2.configure(bg= "lightblue")
window2.title("Temperature Converter")
Label(text = 'Please Choose Which Temperature Converter You Would Like to Use').grid(row=1, column=1, columnspan=2)
photo1= PhotoImage(file='4season.gif')
b = Label( image=photo1)
b.photo = photo1
b.grid(row=5, column=1,columnspan=2)




def normalconvert():
    

    def Calculate():
                   far.set((cel.get()*1.8)+32)
                   print(cel, far)

                   
    window = Toplevel()
    window.minsize(width=240,height=280)
    window.configure(bg= "lightblue")
    window.title("Converter")

    cel = IntVar()
    cel.set(int(0))
    far = IntVar()
    far.set(int(0))

    Label(window,text = 'Celsius to Fahrenheit').grid(row=0, column=1, columnspan=2)
    Entry(window,textvariable = cel).grid(row = 1, column =1, columnspan=2)
    Label(window,text = 'Degrees Celsius').grid(row=2, column=1, columnspan=2)
    Label(window,text = 'is equivalent to').grid(row=3, column=1, columnspan=2)
    Label(window,textvariable = far).grid(row=4, column=1, columnspan=2)
    Label(window,text = 'Degrees Fahrenheit').grid(row=5, column=1, columnspan=2)
    Button(window,text='Calculate',command=Calculate).grid(row=6, column=1, columnspan=2)


    def Calculate1():
                   cel1.set((far1.get()-32)/1.8)
                   print(far1, cel1)

    far1 = IntVar()
    far1.set(int(0))
    cel1 = IntVar()
    cel1.set(int(0))

    Label(window,text = 'Fahrenheit to Celsius').grid(row=0, column=3, columnspan=2)
    Entry(window,textvariable = far1).grid(row = 1, column =3, columnspan=2)
    Label(window,text = 'Degrees Fahrenheit').grid(row=2, column=3, columnspan=2)
    Label(window,text = 'is equivalent to').grid(row=3, column=3, columnspan=2)
    Label(window,textvariable = cel1).grid(row=4, column=3, columnspan=2)
    Label(window,text = 'Degrees Celsius').grid(row=5, column=3, columnspan=2)
    Button(window,text='Calculate',command=Calculate1).grid(row=6, column=3, columnspan=2)

    def Calculate2():
                   kel2.set((far2.get()+459.67)*(5/9))
                   print(far2, kel2)
                   e = open('test1.txt','a')
                   e.write(str(kel2.get()))
                   e.close()

    far2 = IntVar()
    far2.set(int(0))
    kel2 = IntVar()
    kel2.set(int(0))

    Label(window,text = 'Fahrenheit to Kelvin').grid(row=0, column=5, columnspan=2)
    Entry(window,textvariable = far2).grid(row = 1, column = 5, columnspan=2)
    Label(window,text = 'Degrees Fahrenheit').grid(row=2, column=5, columnspan=2)
    Label(window,text = 'is equivalent to').grid(row=3, column=5, columnspan=2)
    Label(window,textvariable = kel2).grid(row=4, column=5, columnspan=2)
    Label(window,text = 'Degrees Kelvin').grid(row=5, column=5, columnspan=2)
    Button(window,text='Calculate',command=Calculate2).grid(row=6, column=5, columnspan=2)

    window.mainloop()

def readwriteconvert():
    
    window1 = Toplevel()
    window1.minsize(width=240,height=280)
    window1.configure(bg= "lightblue")
    window1.title("Converter")

    list1=[]
    with open('test.txt','r') as f:
        for line in f:
            for number in line.split():
                list1.append(number)

    def Calculate():
                   far.set((cel.get()*1.8)+32)
                   print(cel, far)
                   f = open('test1.txt','w')
                   f.write(str(far.get())+" ")
                   f.close()

    cel = IntVar()
    cel.set(int(list1[0]))
    far = IntVar()
    far.set(int(0))


    Label(window1, text = 'Celsius to Fahrenheit').grid(row=0, column=1, columnspan=2)
    Label(window1,text= list1[0]).grid(row = 1, column =1, columnspan=2)
    Label(window1,text = 'Degrees Celsius').grid(row=2, column=1, columnspan=2)
    Label(window1,text = 'is equivalent to').grid(row=3, column=1, columnspan=2)
    Label(window1,textvariable= far).grid(row=4, column=1, columnspan=2)
    Label(window1,text = 'Degrees Fahrenheit').grid(row=5, column=1, columnspan=2)
    Button(window1,text='Calculate',command=Calculate).grid(row=6, column=1, columnspan=2)



    def Calculate1():
                   cel1.set((far1.get()-32)/1.8)
                   print(far1, cel1)
                   e = open('test1.txt','a')
                   e.write(str(cel1.get())+" ")
                   e.close()

    far1 = IntVar()
    far1.set(int(list1[1]))
    cel1 = IntVar()
    cel1.set(int(0))

    Label(window1,text = 'Fahrenheit to Celsius').grid(row=0, column=3, columnspan=2)


    Label(window1,text = list1[1]).grid(row = 1, column =3, columnspan=2)
    Label(window1,text = 'Degrees Fahrenheit').grid(row=2, column=3, columnspan=2)

    Label(window1,text = 'is equivalent to').grid(row=3, column=3, columnspan=2)
    Label(window1,textvariable = cel1).grid(row=4, column=3, columnspan=2)
    Label(window1,text = 'Degrees Celsius').grid(row=5, column=3, columnspan=2)
    Button(window1,text='Calculate',command=Calculate1).grid(row=6, column=3, columnspan=2)

    def Calculate2():
                   kel2.set((far2.get()+459.67)*(5/9))
                   print(far2, kel2)
                   e = open('test1.txt','a')
                   e.write(str(kel2.get()))
                   e.close()

    far2 = IntVar()
    far2.set(int(list1[2]))
    kel2 = IntVar()
    kel2.set(int(0))

    Label(window1,text = 'Fahrenheit to Kelvin').grid(row=0, column=5, columnspan=2)


    Label(window1,text = list1[2]).grid(row = 1, column =5, columnspan=2)
    Label(window1,text = 'Degrees Fahrenheit').grid(row=2, column=5, columnspan=2)

    Label(window1,text = 'is equivalent to').grid(row=3, column=5, columnspan=2)
    Label(window1,textvariable = kel2).grid(row=4, column=5, columnspan=2)
    Label(window1,text = 'Degrees Kelvin').grid(row=5, column=5, columnspan=2)
    Button(window1,text='Calculate',command=Calculate2).grid(row=6, column=5, columnspan=2)

    window1.mainloop()

Button(text='Normal Conversion',command=normalconvert).grid(row=2, column=1, columnspan=2)
Button(text='Read/Write Conversion',command=readwriteconvert).grid(row=3, column=1, columnspan=2)

window2.mainloop()
