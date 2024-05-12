#Import all the necessary libraries
from tkinter import *

#Define the tkinter instance
win= Tk()
win.title("MyDietFits")
win.configure(bg="light blue")
#Define the size of the tkinter frame
win.geometry('700x900')

#Define the working of the button

def Open():
   New_Window = Tk()
   New_Window.configure(bg="light blue")
   #edit window here
   win.destroy()
   New_Window.title("ExerciseApp")
   New_Window.geometry('700x900')
   exercise_label = Label(New_Window,text="Exercise",
              font=('Arial',30,'bold'),
              fg='red',
              bg='orange',
              relief=RAISED,
              bd=10,
              compound='bottom')
   exercise_label.place(x=100,y=0)
   
   
   # Exit button, destroys window
   def Close(): 
      New_Window.destroy() 
    
   # Placing Exit button
   exit_button = Button(New_Window, text="Exit", command=Close) 
   exit_button.pack(pady=20)
   exit_button.place(x=0,y=0)


def Open2():
   New_Window2 = Tk()
   New_Window2.configure(bg="light blue")
   
   #edit window here
   win.destroy()
   New_Window2.title("DietApp")
   New_Window2.geometry('700x900')
   diet_label = Label(New_Window2,text="Diet",
              font=('Arial',30,'bold'),
              fg='red',
              bg='orange',
              relief=RAISED,
              bd=10,
              compound='bottom')
   diet_label.place(x=100,y=0)
   
   
   # Exit button, destroys window
   def Close(): 
      New_Window2.destroy() 
    
   # Placing Exit button
   exit_button2 = Button(New_Window2, text="Exit", command=Close) 
   exit_button2.pack(pady=20)
   exit_button2.place(x=0,y=0)
   
   
# Entire section for Exercise Button

#Import the image using PhotoImage function
exercise_btn= PhotoImage(file='mdf-exercise.png')


img_label= Label(image=exercise_btn)


# This puts the image as the button
exercisebutton= Button(win, image=exercise_btn,command= Open)
borderwidth=0
exercisebutton.pack(pady=30)

# Creating Label for Exercise text
exercise_text= Label(win, text= "Exercise",
   font=('Arial',30,'bold'),
   fg='red',
   bg='orange',
   relief=RAISED,
   bd=10,
   compound='bottom')
exercise_text.pack(pady=30)


# Entire section for Diet button

#Import the image using PhotoImage function
diet_btn= PhotoImage(file='mdf-meals.png')

# Create a label for button event
img_label2= Label(image=diet_btn)

# This puts the image as the button
meal= Button(win, image=diet_btn,command= Open2)
borderwidth=0
meal.pack(pady=30)

# Label for Diet text
diet_text= Label(win, text= "Diet",
   font=('Arial',30,'bold'),
   fg='red',
   bg='orange',
   relief=RAISED,
   bd=10,
   compound='bottom')
diet_text.pack(pady=30)



# Defining Exit button for Title Window
def Close(): 
    win.destroy() 
    
# Placing Exit button
exit_button = Button(win, text="Exit", command=Close) 
exit_button.pack(pady=20)
exit_button.place(x=0,y=0)

win.mainloop()
