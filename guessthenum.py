from tkinter import *
import random
import time

window=Tk()
window.geometry("470x350")
window.configure(bg='#AA98A9')

uparrow=PhotoImage(file="uparpy.png")
downarrow=PhotoImage(file="downarpy.png")
check=PhotoImage(file="checkpy.png")
dice=PhotoImage(file="dicefpy.png")

lbl1=Label(window, text="Guess the number", bg='#AA98A9', fg='white', font=('Comic Sans', 25, "bold"), justify="center")
lbl1.grid(column=0, row=0, columnspan=3)


x=IntVar()
x.set(1)

rad1=Radiobutton(window, text="Easy(0-50)", value=1, var=x, bg='#AA98A9', fg='light green', font=('Comic Sans', 16, "bold"), justify="center")
rad2=Radiobutton(window, text="Normal(0-100)", value=2, var=x, bg='#AA98A9', fg='light blue', font=('Comic Sans', 16, "bold"),justify="center")
rad3=Radiobutton(window, text="Hard(0-150)", value=3, var=x, bg='#AA98A9', fg='red', font=('Comic Sans', 16, "bold"), justify="center")
rad1.grid(column=0, row=1)
rad2.grid(column=1, row=1)
rad3.grid(column=2, row=1)

tries=0

txt =Entry(window, bg='#AA98A9', fg='light blue', font=('Comic Sans', 20, "bold"), justify="center", width=10, state='disabled')
txt.grid(column=1, row=3, columnspan=2)
lblim=Label(window, image=dice, bg='#AA98A9')
lblim.grid(column=0, row=3, rowspan=2)
lbltries=Label(window,text='Tries: '+str(tries),bg='green', fg='white', font=('Comic Sans', 15, "bold"), justify="center", width=8, height=1)
lbltries.grid(column=0, row=7, columnspan=1)
lblvoid=Label(window, text='', width=20, height=3, bg='#AA98A9')
lblvoid.grid(column=0, row=6, columnspan=3)

lblvoid2=Label(window, text='', width=20, height=1, bg='#AA98A9')
lblvoid2.grid(column=0, row=8, columnspan=3)

thinklbl=Label(window, text="", bg='#AA98A9',font=('Comic Sans', 20, "bold"), justify="center", width=8, height=1)
thinklbl.grid(row=9, column=0, columnspan=3)

num = 0
def restart():
  global x, num, tries, a, b
  if int(x.get())==1:
      num = random.randint(0, 50)
  elif int(x.get())==2:
      num = random.randint(0, 100)
  elif int(x.get())==3:
      num = random.randint(0, 150)
  a=0
  thinklbl.configure(fg='black',font=('Comic Sans', 20, "bold"))
  while a<10:
      b=random.randint(1,5)
      if b==1:
          thinklbl.configure(text='.')
          thinklbl.update()
      elif b==2:
          thinklbl.configure(text='..')
          thinklbl.update()
      elif b==3:
          thinklbl.configure(text='....')
          thinklbl.update()
      elif b==4:
          thinklbl.configure(text='...')
          thinklbl.update()
      elif b==5:
          thinklbl.configure(text='......')
          thinklbl.update()
      a = a + 1
      time.sleep(0.2)
  if a==10:
      thinklbl.configure(text="Your number is ready!",font=('Comic Sans', 15, "bold"), fg="white",width=20, justify='center')


  lblim.configure(image=dice)
  tries = 0
  lbltries.configure(text='Tries: ' + str(tries), bg='green', fg='white')
  txt.configure(state='normal')

def exit():
    quit()

exitbtn=Button(window, command=exit, text='EXIT', bg='purple', fg='white', font=('Comic Sans', 15, "bold"), justify="center", width=8, height=1)
exitbtn.grid(row=7, column=2)
restartbtn=Button(window, command=restart, text='START', bg='#3A5EBF', fg='white', font=('Comic Sans', 15, "bold"), justify="center", width=8, height=1)
restartbtn.grid(row=7, column=1)


def updown(*args):
    global gamer, num, lblim, tries, lbltries
    tries=tries+1
    gamer = txt.get()
    txt.delete(0, 'end')
    thinklbl.configure(text='')
    if int(gamer)>num:
        lblim.configure(image=downarrow)
    elif int(gamer)<num:
        lblim.configure(image=uparrow)
    else:
        lblim.configure(image=check)
        txt.configure(state='disabled')
    lbltries.configure(text='Tries: '+ str(tries))
    if int(tries) == 2:
        lbltries.configure(bg="dark green")
    elif int(tries) == 3:
        lbltries.configure(bg="yellow", fg='black')
    elif int(tries) == 4:
        lbltries.configure(bg="orange")
    elif int(tries) >= 5:
        lbltries.configure(bg='red', fg='white')

window.bind("<Return>", updown)
window.mainloop()