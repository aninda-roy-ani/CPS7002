import tkinter as tk
from tkinter import ttk, messagebox
from SystemService import SystemService

class GymManagementGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gym Management System")
        self.root.geometry("800x600")

        self.system_service = SystemService()

        self.setup_main_window()

    def setup_main_window(self):
        # Create main frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Create notebook for different functionalities
        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Add tabs for different functionalities
        self.setup_gym_management_tab()
        self.setup_location_management_tab()
        self.setup_member_management_tab()
        self.setup_appointment_management_tab()
        self.setup_payment_management_tab()
        self.setup_management_dashboard_tab()

    def setup_gym_management_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Gym Management")

        tk.Label(tab, text="Gym ID:").grid(row=0, column=0, padx=5, pady=5)
        self.gym_id_entry = tk.Entry(tab)
        self.gym_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(tab, text="Gym Name:").grid(row=1, column=0, padx=5, pady=5)
        self.gym_name_entry = tk.Entry(tab)
        self.gym_name_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(tab, text="Manager:").grid(row=2, column=0, padx=5, pady=5)
        self.manager_entry = tk.Entry(tab)
        self.manager_entry.grid(row=2, column=1, padx=5, pady=5)

        self.add_gym_button = tk.Button(tab, text="Add Gym", command=self.add_gym)
        self.add_gym_button.grid(row=3, column=0, columnspan=2, pady=10)

    def add_gym(self):
        gym_id = self.gym_id_entry.get()
        gym_name = self.gym_name_entry.get()
        manager = self.manager_entry.get()

        if gym_id and gym_name and manager:
            self.system_service.add_gym(gym_id, gym_name, manager)
            messagebox.showinfo("Success", "Gym added successfully.")
        else:
            messagebox.showerror("Error", "Please fill all fields.")

    def setup_location_management_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Location Management")

        tk.Label(tab, text="Gym ID:").grid(row=0, column=0, padx=5, pady=5)
        self.location_gym_id_entry = tk.Entry(tab)
        self.location_gym_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(tab, text="Location ID:").grid(row=1, column=0, padx=5, pady=5)
        self.location_id_entry = tk.Entry(tab)
        self.location_id_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(tab, text="Location Name:").grid(row=2, column=0, padx=5, pady=5)
        self.location_name_entry = tk.Entry(tab)
        self.location_name_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(tab, text="Attendant:").grid(row=3, column=0, padx=5, pady=5)
        self.attendant_entry = tk.Entry(tab)
        self.attendant_entry.grid(row=3, column=1, padx=5, pady=5)

        self.add_location_button = tk.Button(tab, text="Add Location", command=self.add_location)
        self.add_location_button.grid(row=4, column=0, columnspan=2, pady=10)

    def add_location(self):
        gym_id = self.location_gym_id_entry.get()
        location_id = self.location_id_entry.get()
        location_name = self.location_name_entry.get()
        attendant = self.attendant_entry.get()

        if gym_id and location_id and location_name and attendant:
            if self.system_service.add_location_to_gym(gym_id, location_id, location_name, attendant):
                messagebox.showinfo("Success", "Location added successfully.")
            else:
                messagebox.showerror("Error", "Gym not found.")
        else:
            messagebox.showerror("Error", "Please fill all fields.")

    def setup_member_management_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Member Management")

        # Create GUI components for member management
        # Similar to setup_gym_management_tab

    def setup_appointment_management_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Appointment Management")

        # Create GUI components for appointment management
        # Similar to setup_gym_management_tab

    def setup_payment_management_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Payment Management")

        # Create GUI components for payment management
        # Similar to setup_gym_management_tab

    def setup_management_dashboard_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Management Dashboard")

        # Create GUI components for management dashboard
        # Similar to setup_gym_management_tab

if __name__ == "__main__":
    root = tk.Tk()
    app = GymManagementGUI(root)
    root.mainloop()
