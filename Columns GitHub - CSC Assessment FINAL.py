import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Create a new instance of tkinter
root = tk.Tk()

#Title 
root.title("Julie's Party Hire")

# Enlarging the window (For better usability)
root.geometry("800x650")  # Set an starting size for the window

# Changing the font for the title
from tkinter import font
title_font = font.Font(family="Party LET", size=45, weight="bold")

# Create the title label
title_label = tk.Label(root, text="Julie's Party Hire", bg="sky blue", fg="black", font=title_font)
title_label.pack()

# Border
root.configure(highlightbackground="white", highlightcolor="white", highlightthickness=4)
# Background colour
root.configure(bg="sky blue")

# Change the font for the customer name label
customer_name_font = font.Font(family="Academy Engraved LET", size=16)

# Label for customer's name
customer_name_label = tk.Label(root, text="Customer's Name:", bg="sky blue", fg="black", font=customer_name_font)
customer_name_label.pack()

# Entry button for customer's name
customer_name_entry = tk.Entry(root)
customer_name_entry.pack()

# Change the font for the item hired label
item_hired_font = font.Font(family="Academy Engraved LET", size=16)

# Label for item hired
item_hired_label = tk.Label(root, text="Item hired:", bg="sky blue", fg="black", font=item_hired_font)
item_hired_label.pack()

# Creating a drop down box with options for items hired
items_hired = ['Table', 'Chair', 'Balloons', 'Back Drop', 'Projector', 'Other']
item_hired_variable = tk.StringVar(root)
item_hired_variable.set(items_hired[0])  # Set the default value
item_hired_dropdown = tk.OptionMenu(root, item_hired_variable, *items_hired)
item_hired_dropdown.pack() 

# Define minimum and maximum amount of things hired. 
MIN_ITEMS_HIRED = 1
MAX_ITEMS_HIRED = 500

# Change the font for the number of items hired label
number_of_items_hired_font = font.Font(family="Academy Engraved LET", size=16)

# Label for number of items hired
number_of_items_hired_label = tk.Label(root, text="Number of items hired (1-500):", bg="sky blue", fg="black", font=number_of_items_hired_font)
number_of_items_hired_label.pack()

# Create a spinbox button for the number of items hired, this will allow the user to use the arrows to reach the number, but they are still able to type the number too. 
number_of_items_hired_spinbox = tk.Spinbox(root, from_=MIN_ITEMS_HIRED, to=MAX_ITEMS_HIRED)
number_of_items_hired_spinbox.pack() 

# Change the font for the receipt number label
receipt_number_font = font.Font(family="Academy Engraved LET", size=16)

# Label for receipt number
receipt_number_label = tk.Label(root, text="Receipt number:", bg="sky blue", fg="black", font=receipt_number_font)
receipt_number_label.pack()

# Text button for receipt number (changing the measurements so it matches up with the other entry boxes)
receipt_number_text = tk.Text(root, height=1.5, width=28)
receipt_number_text.pack()

# Change the font for the saved details
saved_details_font = font.Font(family="Academy Engraved LET", size=16)

frame2 = tk.Frame(root, width=600, height=200)
frame2.pack()
    
# Create the table
cols = ("Customer name:", "Receipt Number", "Item hired", "Quantity")
table = ttk.Treeview(frame2, columns=cols, show='headings')
table.pack()

# Changing the width of the columns
table.column("Customer name:", width=200) 
table.column("Item hired", width=150)  
table.column("Receipt Number", width=200)
table.column("Quantity", width=80) 

# Define column headings 
for col in cols:
    table.heading(col,text=col)

# Define a function to save the customer's details
def save_details():
    customer_name = customer_name_entry.get()
    item_hired = item_hired_variable.get()
    receipt_number = receipt_number_text.get("1.0", "end-1c")

    try:
        number_of_items_hired = int(number_of_items_hired_spinbox.get())

        if len(receipt_number) < 4:
            messagebox.showerror("Invalid Receipt Number", "Receipt number should be at least 4 numbers long.")
        elif number_of_items_hired < MIN_ITEMS_HIRED or number_of_items_hired > MAX_ITEMS_HIRED:
            messagebox.showerror("Invalid Input", "Please enter a number between 1 and 500.")
        else:
            details = (customer_name, receipt_number, item_hired, number_of_items_hired)
            table.insert("", tk.END, values=details)
            with open("Julie's_Party_Hire_details.txt", "a") as file:
                file.write(f"{details}\n")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the 'Number of items hired' field.")

    if not customer_name or not item_hired or not number_of_items_hired or not receipt_number:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

# Change the font for the save button
save_button_font = font.Font(family="Academy Engraved LET", size=16)

# Create a button to save details
save_button = tk.Button(root, text="Save Details", command=save_details, font=save_button_font, fg="lime green")
save_button.pack()

# Define a function to delete the item that has been selected by the user from the table
def delete_details():
    selected_item = table.selection()
    if selected_item:
        table.delete(selected_item)

# Create a button to delete selected item
button_font = font.Font(family="Academy Engraved LET", size=16)

delete_button = tk.Button(root, text="Delete Selected", command=delete_details, font=button_font)
delete_button.configure(font=button_font, fg="dark orange")
delete_button.pack()

# Defining a function to clear all of the fields
def clear_fields():
    customer_name_entry.delete(0, "end")
    item_hired_variable.set(items_hired[0])  # Resetting the item_hired_variable to its starting value which is 'table'. 
    number_of_items_hired_spinbox.delete(0, "end")
    receipt_number_text.delete("1.0", "end")

# Create a custom font for the buttons
button_font = font.Font(family="Academy Engraved LET", size=16)

# Create a button to clear fields
clear_button = tk.Button(root, text="Clear Fields", command=clear_fields)
clear_button.configure(font=button_font, fg="purple")
clear_button.pack()

# Create a quit button to exit the application 
quit_button = tk.Button(root, text="Quit", command=root.destroy)
quit_button.configure(fon=button_font, fg="red")
quit_button.pack()

# Run the main event loop
root.mainloop()