import tkinter as tk
from tkinter import ttk

# Main window setup
root = tk.Tk()
root.title("Attendance Tracker")
root.geometry("600x500")  # Adjusted size

# Header section
header_frame = tk.Frame(root, bg="navy", height=50)
header_frame.pack(fill=tk.X)

header_label = tk.Label(header_frame, text="Attendance Tracker", bg="navy", fg="white", font=("Arial", 20))
header_label.pack(pady=10)

# Student data for each class
students_data = {
    "IT A": ["23ITR001 JEEVASRUTHI S", "23ITR002 KANIMOZHI S", "23ITR003 KRITHIKA S"],
    "IT B": ["23ITR004 KAVIYA B", "23IT4005 MOWNISHA A", "23ITR006 MYHTILI M"],
    "IT C": ["23ITR007 MEGAVARSHINI M", "23ITR008 PREMISHA T", "23ITR009 PRIYANKA K"]
}

# Dropdown section for Class, Section, and Subject
dropdown_frame = tk.Frame(root, pady=20)
dropdown_frame.pack()

# Class Dropdown
class_label = tk.Label(dropdown_frame, text="Class:")
class_label.grid(row=0, column=0, padx=10)
class_options = list(students_data.keys())
class_dropdown = ttk.Combobox(dropdown_frame, values=class_options, state="readonly")
class_dropdown.grid(row=0, column=1)

# Section Dropdown
sec_label = tk.Label(dropdown_frame, text="Session:")
sec_label.grid(row=0, column=2, padx=10)
section_options = ["FN", "AN", "SC"]
sec_dropdown = ttk.Combobox(dropdown_frame, values=section_options, state="readonly")
sec_dropdown.grid(row=0, column=3)

# Subject Dropdown
subject_label = tk.Label(dropdown_frame, text="Subject:")
subject_label.grid(row=0, column=4, padx=10)
subject_options = ["ITC", "MES", "DSUJ", "PYTHON", "CO"]
subject_dropdown = ttk.Combobox(dropdown_frame, values=subject_options, state="readonly")
subject_dropdown.grid(row=0, column=5)

# Attendance table frame
table_frame = tk.Frame(root, padx=20, pady=10)
table_frame.pack()

# Function to update the attendance table based on the selected class
def update_table():
    for widget in table_frame.winfo_children():
        widget.destroy()

    # Header for the table
    tk.Label(table_frame, text="Name", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5)
    tk.Label(table_frame, text="Attendance", font=("Arial", 12)).grid(row=0, column=1, padx=5, pady=5)

    selected_class = class_dropdown.get()
    if selected_class in students_data:
        names = students_data[selected_class]
        attendance_vars.clear()

        for i, name in enumerate(names):
            # Student Name
            tk.Label(table_frame, text=name).grid(row=i+1, column=0, padx=10, pady=5)

            # Attendance Checkbox
            var = tk.BooleanVar()
            chk = tk.Checkbutton(table_frame, variable=var)
            chk.grid(row=i+1, column=1)

            # Store attendance status for later use
            attendance_vars.append((name, var))

class_dropdown.bind("<<ComboboxSelected>>", lambda e: update_table())

attendance_vars = []

# Placeholder submit button (functionality can be added later)
submit_button = tk.Button(root, text="Submit Attendance", bg="navy", fg="white")
submit_button.pack(pady=20)

root.mainloop()
