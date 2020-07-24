# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

#__author__ = "admin"
#__date__ = "$Jun 18, 2020 8:54:37 PM$"

from Tkinter import *
import sqlite3

root = Tk()
root.title("Split Expenses")
root.geometry("800x700")

my_menu = Menu(root)
root.config(menu=my_menu)


#create a databse or coonect to it
#conn = sqlite3.connect('data_db')

#Create a cursor
#c = conn.cursor()

class Database1:
    print_record=''
    def query(self):
        #create a databse or coonect to it
        conn = sqlite3.connect('data_db')

        #Create a cursor
        c = conn.cursor()

        #Query the database:
        c.execute("SELECT *,oid FROM data_name")
        records=c.fetchall()  

        #loop through the records
        for record in records:
            self.print_record+= str(record[0]) +" " + str(record[1]) + "\n"
        #commit changes
        conn.commit()

        #close connection44
        conn.close()
        global frame1
        global l1
        frame1 = LabelFrame(root,text="List Frame",padx=20,pady=10)
        frame1.place(x=500,y=120,width=200,height=250)

        l1 = Label(frame1,text=self.print_record)
        l1.grid(row=1,column=0,columnspan=2)
    
    def hide(self):
        frame1.destroy()
        #l1.grid_forget()


adi = Database1()
adi.query()

#create table
'''c.execute("""CREATE TABLE data_name (
    name_of_person text,
    pay integer,
    due integer,
    detail text
    )""")'''
    




def submit():
    #create a databse or coonect to it
    conn = sqlite3.connect('data_db')

    #Create a cursor
    c = conn.cursor()
    
    #Insert into tables:
    for i in range(len(list_name)):
        c.execute("INSERT INTO data_name VALUES (:f_name, :pay, :due, :detail)",
        {
            'f_name' : list_name[i].get(),
            'pay' : 0,
            'due': 0,
            'detail': ""
        })
    #commit changes
    conn.commit()

    #close connection44
    conn.close()
    adi.query()
#---------------------------------------------------------------------------------------------------------------------------
list_name = []

def generateEntry():
    #frame is initialized here
    frame.place(x=20,y=150,width=400,height=400)
    
    l1 = Label(frame,text="Enter Everyones name: ")
    l1.grid(row=1,column=0,columnspan=2)
    
    b = Button(frame,text="Save Data",command=submit)
    b.grid(row=1,column=3,padx=10)
    len_people = no_of_people.get()
    for i in range(len_people):
       name_label = Label(frame,text="Name :-")
       name_label.grid(row = 2+i,column=1,padx=10,pady=10)
       e =  Entry(frame,borderwidth=4)
       e.grid(row=2+i,column=2,padx=10,pady=10)
       list_name.append(e)


def hide_frame():
    frame.destroy()
    label1.grid_remove()
    no_of_people_entry.grid_remove()
    detailsBtn.grid_remove()
    
def submitPayDetail():
    #create a databse or coonect to it
    conn = sqlite3.connect('data_db')

    #Create a cursor
    d = conn.cursor()
    d.execute("""SELECT * FROM data_name WHERE name_of_person = :name""",{'name':str(name_entry.get())})
    record = (d.fetchone())
    
    amount = int(pay_amount_entry.get())+int(str(record[1]))
    
    c = conn.cursor()
    c.execute(""" UPDATE data_name SET
        pay = :pay ,
        detail = :details 
        
        WHERE name_of_person = :name""",
        {
            'pay': amount,
            'details': str(record[3])+","+pay_detail_entry.get(),
            'name': name_entry.get(),
            })

    #commit changes
    conn.commit()

    #close connection
    conn.close()
    adi.hide()
    adi.query()
    
    
def payDetail():
    hide_frame()
    global name_entry
    global pay_amount_entry
    global pay_detail_entry
    #pay_frame is initialized here
    pay_frame.place(x=20,y=150,width=400,height=300)
    name_entry_label = Label(pay_frame,text="Enter Payer Name:-")
    name_entry_label.grid(row=2,column=1,padx=10,pady=10)
    
    name_entry = Entry(pay_frame,width=20,borderwidth=3)
    name_entry.grid(row=2,column=2,padx=10,pady=10)
    
    pay_amount_label = Label(pay_frame,text="Payment Amount:-")
    pay_amount_label.grid(row=3,column=1,padx=10,pady=10)
    
    pay_amount_entry = Entry(pay_frame,borderwidth=3)
    pay_amount_entry.grid(row=3,column=2,padx=10,pady=10)
    
    pay_detail_label = Label(pay_frame,text="Payment Details:-")
    pay_detail_label.grid(row=4,column=1,padx=10,pady=10)
    
    pay_detail_entry = Entry(pay_frame,borderwidth=3)
    pay_detail_entry.grid(row=4,column=2,padx=10,pady=10)
    
    submit_pay_detail_btn = Button(pay_frame,text="Submit",command=submitPayDetail)
    submit_pay_detail_btn.grid(row=5,column=1,columnspan=2,padx=10,pady=10)
    
def expenseDetail():
    hide_frame()
    adi.hide()
    expense_frame.place(x=20,y=150,width=600,height=300)
    list_detail = xyz()
    updateDueAmount(due_detail)
    for i in range(len(list_detail)):
        for j in range(len(list_detail[0])):
           e = Entry(expense_frame,width=15,fg='blue',font=('Arial',10,'bold'))
           e.grid(row=i,column=j)
           e.insert(END,list_detail[i][j])

def updateDueAmount(due_detail_xyz):
    conn = sqlite3.connect('data_db')
    
    c = conn.cursor()
    
    for key,value in due_detail_xyz.items():
        a = key
        b= value
        c.execute(""" UPDATE data_name SET
            due = :due 
            WHERE name_of_person = :name""",
            {
                'name': a,
                'due': b,
                
                })

    #commit changes
    conn.commit()

    #close connection
    conn.close()
    

def xyz():
    conn = sqlite3.connect('data_db')
    #Create a cursor
    c = conn.cursor()
    global due_detail
    #Query the database:
    c.execute("SELECT oid,* FROM data_name")
    records=c.fetchall()  
    total_amount = 0
    list_detail = []
    
    due_detail = {}
    a = ('Serial No.','Name','Pay','Due','Detail')
    list_detail.append(a)
    #loop through the records
    for record in records:
        list_detail.append(record)
        total_amount+= int(str(record[2]))
    due_amount = total_amount/(len(list_detail)-1)
    for record in records:
        due_detail[str(record[1])] = int(str(record[2]))-due_amount
    
    #commit changes
    conn.commit()
    #close connection44
    conn.close()
    return list_detail

def calculate():
    import operator # For sorting my dictionary
    a = xyz()
    bills = due_detail

    transactions = 0
    while sorted(bills.items(), key=operator.itemgetter(1),reverse=True)[0][1]>0.001:
        transactions+=1
        sorted_bills = sorted(bills.items(), key=operator.itemgetter(1),reverse=True)

        diff_highest_lowest = sorted_bills[0][1]+sorted_bills[-1][1] # Note that array[-1] is the last element of an array (for us: lowest value)
        if diff_highest_lowest > 0: # In this case the lowest amount can't fill the highest amount
            print(sorted_bills[-1][0] + " pays " + sorted_bills[0][0]+ ": " + str(abs(sorted_bills[-1][1]))) # Pay everything you have
            bills[sorted_bills[-1][0]]=0 # The lowest bill is done paying!
            bills[sorted_bills[0][0]] = diff_highest_lowest # The person with the most amount of money still needs to receive money
        else: # The highest amount gets completely paid off. 
            print(sorted_bills[-1][0] + " pays " + sorted_bills[0][0]+ ": " + str(abs(sorted_bills[0][1])))
            bills[sorted_bills[-1][0]]=diff_highest_lowest # The lowest person still has to pay
            bills[sorted_bills[0][0]]=0 # The richest person got all of his money

    print("Amount of transactions: " + str(transactions))

def truncte():
    conn = sqlite3.connect('data_db')
    #Create a cursor
    c = conn.cursor()
    #Query the database:
    c.execute("DELETE FROM data_name")
    conn.commit()
    conn.close()
    
# Main Window Layout-------------------------------------------------------------------------------------------------------

pay_menu = Menu(my_menu)
my_menu.add_cascade(label="Pay",menu=pay_menu)
pay_menu.add_cascade(label="Payment Detail",command=payDetail)
pay_menu.add_cascade(label="Expenses Details",command = expenseDetail)

debt_menu = Menu(my_menu)
my_menu.add_cascade(label="Debt Calculator",menu=debt_menu)
debt_menu.add_cascade(label="Calculation",command=calculate)

frame = LabelFrame(root,text="Entry Frame",padx=20,pady=10)
pay_frame = LabelFrame(root,text="Payment Details",padx=20,pady=20)
expense_frame = LabelFrame(root,text="Expense Details",padx=20,pady=10)

label = Label(root,text="Welcome")
label.grid(row=0,column=2)

button = Button(root,text="Clear Database",command=truncte)
button.grid(row=0,column=3)

label1 = Label(root,text="Enter No. of Peoples")
label1.grid(row=5,column=1,padx=10,pady=10)

no_of_people = IntVar()

no_of_people_entry = Entry(root,textvariable=no_of_people,width=10,borderwidth=4)
no_of_people_entry.grid(row=5,column=2,padx=10,pady=10)

detailsBtn = Button(root,text="Click To enter details of Peoples",command=generateEntry)
detailsBtn.grid(row=6,column=1,columnspan=2,padx=10,pady=10)

# --------------------------------------------------------------------------------------------------------------------------
root.mainloop()

