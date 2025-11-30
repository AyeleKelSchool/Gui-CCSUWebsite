
from tkinter import *
from PIL import ImageTk, Image
import pandas as pd



# -------------------------
# Window setup
# -------------------------
root = Tk()
root.title('CCSU App')
root.geometry("600x600")
root.resizable(False, False)

root.configure(bg='light steel blue')

# -------------------------
# Make white in logo transparent and show it
# -------------------------
img = Image.open('logo1.PNG')
# Pillow>=10 changed ANTIALIAS; this keeps it compatible
try:
    img = img.resize((100, 100), Image.Resampling.LANCZOS)
except AttributeError:
    img = img.resize((100, 100), Image.ANTIALIAS)

img = img.convert("RGBA")
data = img.getdata()

newData = []
for item in data:
    r,g,a, b = item
    if item[:3] == (255, 255, 255):
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

img.putdata(newData)
img.save("transparent.png")
logo = Image.open("transparent.png")
logo = ImageTk.PhotoImage(logo)
logoLabel = Label(root, image=logo, bg='light steel blue')
logoLabel.place(x=1, y=1)

data_file = pd.read_csv('midterm_exam.csv')

lb = Label(root, justify="left", bg="light steel blue", anchor="w")
lb.place(x=130, y=150)

def calender():
    df = pd.DataFrame(data_file, columns=['CalendarDate'])
    selected_rows = df[~df['CalendarDate'].isnull()]
    lb.config(text=selected_rows.to_string(index=False), bg="light steel blue")
    lb.place(x=124, y=190)

def building():
    df = pd.DataFrame(data_file, columns=['Buildings'])
    selected_rows = df[~df['Buildings'].isnull()]
    lb.config(text=selected_rows.to_string(index=False), bg="light steel blue")
    lb.place(x=130, y=150)

def faculty():
    df = pd.DataFrame(data_file, columns=['FacultyName'])
    selected_rows = df[~df['FacultyName'].isnull()]
    lb.config(text=selected_rows.to_string(index=False), bg="light steel blue")
    lb.place(x=145, y=160)

# list of the school of business adn MIS department
school_of_business = [
"School of Business Departments:\n"
        " - Accounting\n"
        " - Finance\n"
        " - Management & Organization\n"
        " - Marketing\n"
        " - Management Information Systems (MIS)\n"
        " - Business Analytics"
]
def school_business():
    for i in school_of_business:
        lb.config(text=i, fg= 'black')
        lb.place(x=140, y=190)
# mis
mis_department = [
    "MIS Department Core Courses:\n"
    " - Intro to MIS\n"
    " - Database Management\n"
    " - Systems Analysis & Design\n"
    " - Business Analytics / Data Visualization\n"
    " - Networks & Information Security\n"
    " - Project Management\n"
    " - Python for Business Applications"
]

def mis_list():
    for l in mis_department:
        lb.config(text=l, fg= 'black')
        lb.place(x=140, y=190)

#button
button1 = Button(root, text='Calender', command=calender, bg="blue" ,fg= 'white')
button1.place(x=50, y=110)
button2 = Button(root, text='Buildings', command = building, bg="blue", fg='white')
button2.place(x=150, y=110)
button3 = Button(root, text='Faculty' , command = faculty, bg="blue" ,fg= 'white')
button3.place(x=250, y=110)

button4 = Button(root, text='School of Business' , command= school_business, bg="blue" ,fg= 'white')
button4.place(x=50, y=160)

button5 = Button(root, text='MIS Department' ,  bg="blue" , command= mis_list ,fg= 'white')
button5.place(x=250, y=160)
mainloop()
