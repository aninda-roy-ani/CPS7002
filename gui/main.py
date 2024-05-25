import tkinter as tk
from tkinter import messagebox, ttk
from system_architechture.user import User

# Load existing users
users = User.load_users()

# Initialize main window
root = tk.Tk()
root.title("St Mary's Fitness")
root.geometry("800x600")
root.configure(bg="black")

# Function to clear the main frame
def clear_frame():
    for widget in main_frame.winfo_children():
        widget.destroy()

# Main frame to hold different views
main_frame = tk.Frame(root, bg="black")
main_frame.pack(fill="both", expand=True)

# History stack to manage navigation
history_stack = []

def go_back():
    if history_stack:
        previous_view = history_stack.pop()
        previous_view()

def logout():
    show_login()

def show_signup():
    clear_frame()
    history_stack.append(show_login)
    tk.Label(main_frame, text="Signup", font=("Arial", 24), bg="black", fg="yellow").pack(pady=20)

    tk.Label(main_frame, text="Username", font=("Arial", 14), bg="black", fg="white").pack(pady=5)
    username_entry = tk.Entry(main_frame, font=("Arial", 14))
    username_entry.pack(pady=5)

    tk.Label(main_frame, text="Password", font=("Arial", 14), bg="black", fg="white").pack(pady=5)
    password_entry = tk.Entry(main_frame, show="*", font=("Arial", 14))
    password_entry.pack(pady=5)

    tk.Label(main_frame, text="User Type", font=("Arial", 14), bg="black", fg="white").pack(pady=5)
    user_type_entry = ttk.Combobox(main_frame, values=["Central Manager", "Manager", "Attendant", "Member"], font=("Arial", 14))
    user_type_entry.pack(pady=5)

    def signup_action():
        username = username_entry.get()
        password = password_entry.get()
        user_type = user_type_entry.get()

        if username and password and user_type:
            if username in users:
                messagebox.showerror("Error", "Username already exists")
            else:
                new_user = User(username, password, user_type)
                users[username] = new_user
                User.save_users(users)
                messagebox.showinfo("Success", "Signup successful")
                show_login()
        else:
            messagebox.showerror("Error", "All fields are required")

    tk.Button(main_frame, text="Signup", font=("Arial", 14), command=signup_action, bg="red", fg="white").pack(pady=20)
    tk.Button(main_frame, text="Back to Login", font=("Arial", 14), command=show_login, bg="yellow", fg="black").pack(pady=10)
    tk.Button(main_frame, text="Back", font=("Arial", 14), command=go_back, bg="yellow", fg="black").pack(side="bottom", pady=10)

def show_login():
    clear_frame()
    history_stack.append(show_login)
    tk.Label(main_frame, text="Login", font=("Arial", 24), bg="black", fg="yellow").pack(pady=20)

    tk.Label(main_frame, text="Username", font=("Arial", 14), bg="black", fg="white").pack(pady=5)
    username_entry = tk.Entry(main_frame, font=("Arial", 14))
    username_entry.pack(pady=5)

    tk.Label(main_frame, text="Password", font=("Arial", 14), bg="black", fg="white").pack(pady=5)
    password_entry = tk.Entry(main_frame, show="*", font=("Arial", 14))
    password_entry.pack(pady=5)

    def login_action():
        username = username_entry.get()
        password = password_entry.get()

        if username in users and users[username].get_password() == password:
            user_type = users[username].get_user_type()
            messagebox.showinfo("Success", f"Welcome {user_type}")
            show_dashboard(user_type)
        else:
            messagebox.showerror("Error", "Invalid credentials")

    tk.Button(main_frame, text="Login", font=("Arial", 14), command=login_action, bg="red", fg="white").pack(pady=20)
    tk.Button(main_frame, text="Signup", font=("Arial", 14), command=show_signup, bg="yellow", fg="black").pack(pady=10)
    tk.Button(main_frame, text="Back", font=("Arial", 14), command=go_back, bg="yellow", fg="black").pack(side="bottom", pady=10)

def show_dashboard(user_type):
    clear_frame()
    history_stack.append(lambda: show_dashboard(user_type))
    tk.Label(main_frame, text=f"{user_type} Dashboard", font=("Arial", 24), bg="black", fg="yellow").pack(pady=20)

    if user_type == "Central Manager":
        central_manager_dashboard()
    elif user_type == "Manager":
        manager_dashboard()
    elif user_type == "Attendant":
        attendant_dashboard()
    elif user_type == "Member":
        member_dashboard()

    tk.Button(main_frame, text="Logout", font=("Arial", 14), command=logout, bg="yellow", fg="black").pack(side="bottom", pady=10)
    tk.Button(main_frame, text="Back", font=("Arial", 14), command=go_back, bg="yellow", fg="black").pack(side="bottom", pady=10)

def central_manager_dashboard():
    tk.Label(main_frame, text="Manage Gyms", font=("Arial", 14), bg="black", fg="white").pack(pady=5)
    tk.Button(main_frame, text="Add Gym", font=("Arial", 14), command=add_gym, bg="red", fg="white").pack(pady=5)
    tk.Button(main_frame, text="Modify Gym", font=("Arial", 14), command=modify_gym, bg="red", fg="white").pack(pady=5)
    tk.Button(main_frame, text="Delete Gym", font=("Arial", 14), command=delete_gym, bg="red", fg="white").pack(pady=5)
    tk.Button(main_frame, text="Generate Revenue Chart", font=("Arial", 14), command=generate_revenue_chart, bg="red", fg="white").pack(pady=5)

def manager_dashboard():
    tk.Label(main_frame, text="Manage Workout Zones", font=("Arial", 14), bg="black", fg="white").pack(pady=5)
    tk.Button(main_frame, text="Add Workout Zone", font=("Arial", 14), command=add_workout_zone, bg="red", fg="white").pack(pady=5)
    tk.Button(main_frame, text="Modify Workout Zone", font=("Arial", 14), command=modify_workout_zone, bg="red", fg="white").pack(pady=5)
    tk.Button(main_frame, text="Delete Workout Zone", font=("Arial", 14), command=delete_workout_zone, bg="red", fg="white").pack(pady=5)

def attendant_dashboard():
    tk.Label(main_frame, text="Manage Equipment", font=("Arial", 14), bg="black", fg="white").pack(pady=5)
    tk.Button(main_frame, text="Add Equipment", font=("Arial", 14), command=add_equipment, bg="red", fg="white").pack(pady=5)
    tk.Button(main_frame, text="Delete Equipment", font=("Arial", 14), command=delete_equipment, bg="red", fg="white").pack(pady=5)

    tk.Label(main_frame, text="Manage Schedules", font=("Arial", 14), bg="black", fg="white").pack(pady=5)
    tk.Button(main_frame, text="Add Schedule", font=("Arial", 14), command=add_schedule, bg="red", fg="white").pack(pady=5)
    tk.Button(main_frame, text="Modify Schedule", font=("Arial", 14), command=modify_schedule, bg="red", fg="white").pack(pady=5)
    tk.Button(main_frame, text="Delete Schedule", font=("Arial", 14), command=delete_schedule, bg="red", fg="white").pack(pady=5)

def member_dashboard():
    tk.Label(main_frame, text="Manage Membership Plan", font=("Arial", 14), bg="black", fg="white").pack(pady=5)
    tk.Button(main_frame, text="Select Membership Plan", font=("Arial", 14), command=select_membership_plan, bg="red", fg="white").pack(pady=5)

    tk.Label(main_frame, text="Manage Appointments", font=("Arial", 14), bg="black", fg="white").pack(pady=5)
    tk.Button(main_frame, text="Create Appointment", font=("Arial", 14), command=create_appointment, bg="red", fg="white").pack(pady=5)

def add_gym():
    pass  # Implement add gym functionality

def modify_gym():
    pass  # Implement modify gym functionality

def delete_gym():
    pass  # Implement delete gym functionality

def generate_revenue_chart():
    pass  # Implement revenue chart generation functionality

def add_workout_zone():
    pass  # Implement add workout zone functionality

def modify_workout_zone():
    pass  # Implement modify workout zone functionality

def delete_workout_zone():
    pass  # Implement delete workout zone functionality

def add_equipment():
    pass  # Implement add equipment functionality

def delete_equipment():
    pass  # Implement delete equipment functionality

def add_schedule():
    pass  # Implement add schedule functionality

def modify_schedule():
    pass  # Implement modify schedule functionality

def delete_schedule():
    pass  # Implement delete schedule functionality

def select_membership_plan():
    pass  # Implement select membership plan functionality

def create_appointment():
    pass  # Implement create appointment functionality

# Initialize the application with the login view
show_login()

root.mainloop()
