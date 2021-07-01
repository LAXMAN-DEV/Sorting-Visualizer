from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
from sorted_engine.bubble_sort import bubble
from sorted_engine.selection_sort import selection
from sorted_engine.merge_sort import merge_sort


root=Tk()
root.title('Visual Sorting 1.0')
root.maxsize(900,600)
root.config(bg='black')
select_al=StringVar()
val=[]

def bardata(val,coloredarray):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width/(len(val)+1)
    offset = 30
    spacing = 10
    normalizedData = [i/max(val) for i in val]
    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        x1 = (i + 1) * x_width + offset
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=coloredarray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(val[i]))

    root.update_idletasks()


#for generating bar graph wrt values
def Generate():
    global val


    try:
        minVal=int(minbox.get())
    except:
        minVal=1
    try:
        maxVal=int(maxbox.get())
    except:
        maxVal=10
    try:
        size=int(inputbox.get())
    except:
        size=10
    if minVal<0:
        minVal = 0
    if maxVal>100:
        maxVal = 100
    if size>30 or size<3: 
        size=25
    if minVal>maxVal : 
        minVal,maxVal=maxVal,minVal
    val =[]
    for _ in range(size):
        val.append(random.randrange(minVal,maxVal+1))
    bardata(val,['red' for i in range (len(val))])

#for start button
def start_algo():
    global val

    if not val:return

    if al_menu.get()=='Selection Sort':
        selection(val,bardata,speed_scale.get())
    
    elif al_menu.get()=='Bubble Sort':
        bubble(val,bardata,speed_scale.get())

    elif al_menu.get()=='Merge Sort':
        bubble(val,bardata,speed_scale.get())
    
    
#UI FRAME
uif=Frame(root, width=600,height=200,bg='grey')
uif.grid(row=0,column=0,padx=10,pady=5)
canvas=Canvas(root,width=600,height=380,bg='light blue')
canvas.grid(row=1,column=0,padx=10,pady=5)

#UI AREA
#1
Label(uif,text="ALGORITHM",bg='grey').grid(row=0,column=0,padx=5,pady=5,sticky=W)
al_menu=ttk.Combobox(uif,textvariable=select_al,values=['Bubble Sort','Selection Sort','Merge Sort'])
al_menu.grid(row=0,column=1,padx=5,pady=5)
al_menu.current(0)

#speed
Label(uif,text="SELECT EXECUTION SPEED(s)",bg='grey').grid(row=0,column=4,padx=5,pady=5,sticky=W)
speed_scale=Scale(uif,from_=0.1,to=2.0,length=100,digits=2,resolution=0.2,orient=HORIZONTAL)
speed_scale.grid(row=0,column=5,padx=5,pady=5)

Button(uif,text="START",command=start_algo).grid(row=0,column=2,padx=5,pady=5)

Button(uif,text="GENERATE",command=Generate).grid(row=0,column=3,padx=5,pady=5)

#UI AREA
#2
Label(uif,text="SIZE",bg='grey').grid(row=1,column=0,padx=5,pady=5,sticky=W)
inputbox=Entry(uif)
inputbox.grid(row=1,column=1,padx=5,pady=5,sticky=W)

Label(uif,text="MIN VALUE",bg='grey').grid(row=1,column=2,padx=5,pady=5,sticky=W)
minbox=Entry(uif)
minbox.grid(row=1,column=3,padx=5,pady=5,sticky=W)

Label(uif,text="MAX VALUE",bg='grey').grid(row=1,column=4,padx=5,pady=5,sticky=W)
maxbox=Entry(uif)
maxbox.grid(row=1,column=5,padx=5,pady=5,sticky=W)




root.resizable(False,False)
root.mainloop()
