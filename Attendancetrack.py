import tkinter as tk
from tkinter import ttk, messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
# Main window setup
root = tk.Tk()
root.title("Attendance Tracker")
root.geometry("600x500")

# Email configuration
SENDER_EMAIL = "kanisenthil252006@gmail.com"  # Replace with your email
APP_PASSWORD = "oknx vcdf vazg ldcb"  # Replace with your app password

# Student data for each class with email addresses
students_data = {
    "IT A": {
        "23ITR001 JEEVASHRUTHI S": "jeevasruthis.23it@kongu.edu",
        "23ITR002 KANIMOZHI S": "kanimozhis.23it@kongu.edu",
        "23ITR003 KRITHIKA S": "krithikas.23it@kongu.edu"
    },
    "IT B": {
        "23ITR004 KAVIYA B": "kaviyab.23it@kongu.edu",
        "23ITR005 MOWNISHA A": "mownishaa.23it@kongu.edu",
        "23ITR006 MYTHILI M": "mythilim.23it@kongu.edu"
    },
    "IT C": {
        "23ITR007 MEGAVARSHINI V": "megavarshiniv.23it@kongu.edu",
        "23ITR008 PREMISHA T": "premishat.23it@kongu.edu",
        "23ITR009 PRIYANKA B": "priyankab.23it@kongu.edu"
    }
}

# Header section
header_frame = tk.Frame(root, bg="navy", height=50)
header_frame.pack(fill=tk.X)

header_label = tk.Label(header_frame, text="Attendance Tracker", bg="navy", fg="white", font=("Arial", 20))
header_label.pack(pady=10)

# Dropdown section for Class, Section, and Subject
dropdown_frame = tk.Frame(root, pady=20)
dropdown_frame.pack()

# Class Dropdown
class_label = tk.Label(dropdown_frame, text="Class:")
class_label.grid(row=0, column=0, padx=10)
class_options = list(students_data.keys())
class_dropdown = ttk.Combobox(dropdown_frame, values=class_options, state="readonly")
class_dropdown.grid(row=0, column=1)
class_dropdown.set("Select Class")

# Section Dropdown
sec_label = tk.Label(dropdown_frame, text="Session:")
sec_label.grid(row=0, column=2, padx=10)
section_options = ["FN", "AN", "SC"]
sec_dropdown = ttk.Combobox(dropdown_frame, values=section_options, state="readonly")
sec_dropdown.grid(row=0, column=3)
sec_dropdown.set("Select Session")

# Subject Dropdown
subject_label = tk.Label(dropdown_frame, text="Subject:")
subject_label.grid(row=0, column=4, padx=10)
subject_options = ["ITC", "MES", "DSUJ", "PYTHON", "CO"]
subject_dropdown = ttk.Combobox(dropdown_frame, values=subject_options, state="readonly")
subject_dropdown.grid(row=0, column=5)
subject_dropdown.set("Select Subject")

# Attendance table frame
table_frame = tk.Frame(root, padx=20, pady=10)
table_frame.pack()

# Function to update the attendance table based on the selected class
def update_table():
    for widget in table_frame.winfo_children():
        widget.destroy()

    tk.Label(table_frame, text="Name", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5)
    tk.Label(table_frame, text="Attendance", font=("Arial", 12)).grid(row=0, column=1, padx=5, pady=5)

    selected_class = class_dropdown.get()
    if selected_class in students_data:
        names = students_data[selected_class]
        attendance_vars.clear()

        for i, (name, email) in enumerate(names.items()):
            tk.Label(table_frame, text=name).grid(row=i+1, column=0, padx=10, pady=5)
            var = tk.BooleanVar()
            chk = tk.Checkbutton(table_frame, variable=var)
            chk.grid(row=i+1, column=1)
            attendance_vars.append((name, email, var))

class_dropdown.bind("<<ComboboxSelected>>", lambda e: update_table())

attendance_vars = []

# Function to send attendance emails
def send_email(name, email, status, session, subject):
    try:
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = email
        msg['Subject'] = f"Attendance Notification for {name}"
        body = (f"Dear {name},\n\n"
                f"Your attendance status for the subject '{subject}' during the {session} session is: {status}.\n\n"
                "Regards,\nAttendance Tracker")
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(SENDER_EMAIL, APP_PASSWORD)
            server.sendmail(SENDER_EMAIL, email, msg.as_string())
        print(f"Email sent successfully to {name} ({email})!")
    except Exception as e:
        print(f"Failed to send email to {name} ({email}):", e)

def submit_attendance():
    selected_class = class_dropdown.get()
    session = sec_dropdown.get()
    subject = subject_dropdown.get()
    
    if not selected_class or not session or not subject:
        messagebox.showwarning("Warning", "Please select Class, Session, and Subject!")
        return

    # Send individual emails with a delay
    for name, email, var in attendance_vars:
        status = "Present" if var.get() else "Absent"
        send_email(name, email, status, session, subject)
        time.sleep(2)  # Adds a 2-second delay between emails to avoid limits
    
    messagebox.showinfo("Success", "Attendance submitted and emails sent!")
submit_button = tk.Button(root, text="Submit Attendance", command=submit_attendance, bg="navy", fg="white")
submit_button.pack(pady=20)

root.mainloop()

