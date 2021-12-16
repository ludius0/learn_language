from tkinter import *
from tkinter import messagebox
import sqlite3


### Set window
root = Tk()
root.title("Simple program with database")
root.geometry("350x420")

### Set database
database = sqlite3.connect("adresses_database.db")
i = database.cursor()

try:
	i.execute("""CREATE TABLE addresses (
                    first_name text,
                    last_name text,
                    address text,
                    city text,
                    state text,
                    zip_code integer
                    )""")
except Exception as e:
	pass


### Create functions
def submit():
    # Set database
    database = sqlite3.connect("adresses_database.db")
    i = database.cursor()
    
    i.execute("INSERT INTO addresses VALUES (:first_name, :last_name, :address, :city, :state, :zip_code)",
		    {
			"first_name": first_name.get(),
		    	"last_name": last_name.get(),
	    		"address": address.get(),
    			"city": city.get(),
                        "state": state.get(),
			"zip_code": zip_code.get()
		    })


    # Commit and close database
    database.commit()
    database.close()

    
    # Clear Entry
    first_name.delete(0, END)
    last_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zip_code.delete(0, END)

def show():
    # Set database
    database = sqlite3.connect("adresses_database.db")
    i = database.cursor()
    # save database into "records"
    i.execute("SELECT *, oid FROM addresses")
    records = i.fetchall()
    # Show database in pop up info message box
    messagebox.showinfo("Database", records)

    # Commit and close database
    database.commit()
    database.close()

def delete():
    # Set database
    database = sqlite3.connect("adresses_database.db")
    i = database.cursor()
    # Delete adress with associated ID and clear Entry
    i.execute("DELETE from addresses WHERE oid =" + delete_id.get())
    delete_id.delete(0, END)

    # Commit and close database
    database.commit()
    database.close()



### Create Labels
first_name_label = Label(root, text="First Name:").grid(row=0, column=0, padx=10)
second_name_label = Label(root, text="Second Name:").grid(row=1, column=0, pady=10)
adress_label = Label(root, text="Address:").grid(row=2, column=0, pady=10)
city_label = Label(root, text="City:").grid(row=3, column=0, pady=10)
state_label = Label(root, text="State/Counry:").grid(row=4, column=0, pady=10)
zip_code_label = Label(root, text="Zip code:").grid(row=5, column=0, pady=10)
delete_id_labeů = Label(root, text="Remove selected ID adress:").grid(row=8, column=0, pady=10)


### Create Entry
first_name = Entry(root, width=10)
last_name = Entry(root, width=10)
address = Entry(root, width=10)
city = Entry(root, width=10)
state = Entry(root, width=10)
zip_code = Entry(root, width=10)
delete_id = Entry(root, width=10)

# For some reason I couldn't write .grid() next to Entry() to make it work
first_name.grid(row=0, column=1, padx=20, pady=(10, 0))
last_name.grid(row=1, column=1)
address.grid(row=2, column=1)
city.grid(row=3, column=1)
state.grid(row=4, column=1)
zip_code.grid(row=5, column=1)
delete_id.grid(row=8, column=1)


### Create buttons
submit_database = Button(root, text="Submit to database", command=submit).grid(row=6, column=0, padx=10, pady=10, columnspan=2, ipadx=100)
show_database = Button(root, text="Show database", command=show).grid(row=7, column=0, padx=10, pady=10, columnspan=2, ipadx=100)
delete_database = Button(root, text="Delete from database", command=delete).grid(row=9, column=0, padx=10, pady=10, columnspan=2, ipadx=100)


### Close database and create window loop
database.commit()
database.close()
root.mainloop()
