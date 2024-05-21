import tkinter as tk
from tkinter import ttk
from datetime import datetime

# Define the main application class
class GymApp:
    def __init__(self, root):
        self.root = root
        self.root.title("St Mary's Fitness Management System")
        self.root.geometry("1000x700")

        # Setup style
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TLabel', background='#f0f0f0', font=('Helvetica', 12))
        self.style.configure('TButton', font=('Helvetica', 12))
        self.style.configure('Header.TLabel', font=('Helvetica', 16, 'bold'))

        self.create_widgets()

    def create_widgets(self):
        # Tabs
        self.tab_control = ttk.Notebook(self.root)

        # Gym Locations Tab
        self.gym_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.gym_tab, text='Gym Locations')

        # Workout Zones Tab
        self.zones_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.zones_tab, text='Workout Zones')

        # Members Tab
        self.members_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.members_tab, text='Members')

        # Appointments Tab
        self.appointments_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.appointments_tab, text='Appointments')

        # Payments Tab
        self.payments_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.payments_tab, text='Payments')

        # Subscriptions Tab
        self.subscriptions_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.subscriptions_tab, text='Subscriptions')

        # Attendance Tracking Tab
        self.attendance_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.attendance_tab, text='Attendance Tracking')

        # Staff Management Dashboard Tab
        self.staff_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.staff_tab, text='Staff Management Dashboard')

        self.tab_control.pack(expand=1, fill='both')

        self.create_gym_tab()
        self.create_zones_tab()
        self.create_members_tab()
        self.create_appointments_tab()
        self.create_payments_tab()
        self.create_subscriptions_tab()
        self.create_attendance_tab()
        self.create_staff_tab()

    def create_gym_tab(self):
        header = ttk.Label(self.gym_tab, text="Gym Locations Management", style='Header.TLabel')
        header.grid(column=0, row=0, columnspan=2, pady=10)

        gym_id_label = ttk.Label(self.gym_tab, text="Gym ID:")
        gym_id_label.grid(column=0, row=1, padx=10, pady=5, sticky='E')
        self.gym_id_entry = ttk.Entry(self.gym_tab)
        self.gym_id_entry.grid(column=1, row=1, padx=10, pady=5)

        city_label = ttk.Label(self.gym_tab, text="City:")
        city_label.grid(column=0, row=2, padx=10, pady=5, sticky='E')
        self.city_entry = ttk.Entry(self.gym_tab)
        self.city_entry.grid(column=1, row=2, padx=10, pady=5)

        manager_label = ttk.Label(self.gym_tab, text="Manager:")
        manager_label.grid(column=0, row=3, padx=10, pady=5, sticky='E')
        self.manager_entry = ttk.Entry(self.gym_tab)
        self.manager_entry.grid(column=1, row=3, padx=10, pady=5)

        add_gym_button = ttk.Button(self.gym_tab, text="Add Gym", command=self.add_gym)
        add_gym_button.grid(column=1, row=4, padx=10, pady=10)

        self.gyms_treeview = ttk.Treeview(self.gym_tab, columns=('ID', 'City', 'Manager'), show='headings')
        self.gyms_treeview.heading('ID', text='Gym ID')
        self.gyms_treeview.heading('City', text='City')
        self.gyms_treeview.heading('Manager', text='Manager')
        self.gyms_treeview.grid(column=0, row=5, columnspan=2, padx=10, pady=10, sticky='nsew')

        self.gym_tab.grid_columnconfigure(1, weight=1)
        self.gym_tab.grid_rowconfigure(5, weight=1)

    def create_zones_tab(self):
        header = ttk.Label(self.zones_tab, text="Workout Zones Management", style='Header.TLabel')
        header.grid(column=0, row=0, columnspan=2, pady=10)

        zone_id_label = ttk.Label(self.zones_tab, text="Zone ID:")
        zone_id_label.grid(column=0, row=1, padx=10, pady=5, sticky='E')
        self.zone_id_entry = ttk.Entry(self.zones_tab)
        self.zone_id_entry.grid(column=1, row=1, padx=10, pady=5)

        exercise_label = ttk.Label(self.zones_tab, text="Exercise Type:")
        exercise_label.grid(column=0, row=2, padx=10, pady=5, sticky='E')
        self.exercise_entry = ttk.Entry(self.zones_tab)
        self.exercise_entry.grid(column=1, row=2, padx=10, pady=5)

        attendant_label = ttk.Label(self.zones_tab, text="Attendant:")
        attendant_label.grid(column=0, row=3, padx=10, pady=5, sticky='E')
        self.attendant_entry = ttk.Entry(self.zones_tab)
        self.attendant_entry.grid(column=1, row=3, padx=10, pady=5)

        add_zone_button = ttk.Button(self.zones_tab, text="Add Zone", command=self.add_zone)
        add_zone_button.grid(column=1, row=4, padx=10, pady=10)

        self.zones_treeview = ttk.Treeview(self.zones_tab, columns=('ID', 'Exercise', 'Attendant'), show='headings')
        self.zones_treeview.heading('ID', text='Zone ID')
        self.zones_treeview.heading('Exercise', text='Exercise Type')
        self.zones_treeview.heading('Attendant', text='Attendant')
        self.zones_treeview.grid(column=0, row=5, columnspan=2, padx=10, pady=10, sticky='nsew')

        self.zones_tab.grid_columnconfigure(1, weight=1)
        self.zones_tab.grid_rowconfigure(5, weight=1)

    def create_members_tab(self):
        header = ttk.Label(self.members_tab, text="Members Management", style='Header.TLabel')
        header.grid(column=0, row=0, columnspan=2, pady=10)

        member_id_label = ttk.Label(self.members_tab, text="Member ID:")
        member_id_label.grid(column=0, row=1, padx=10, pady=5, sticky='E')
        self.member_id_entry = ttk.Entry(self.members_tab)
        self.member_id_entry.grid(column=1, row=1, padx=10, pady=5)

        name_label = ttk.Label(self.members_tab, text="Name:")
        name_label.grid(column=0, row=2, padx=10, pady=5, sticky='E')
        self.name_entry = ttk.Entry(self.members_tab)
        self.name_entry.grid(column=1, row=2, padx=10, pady=5)

        age_label = ttk.Label(self.members_tab, text="Age:")
        age_label.grid(column=0, row=3, padx=10, pady=5, sticky='E')
        self.age_entry = ttk.Entry(self.members_tab)
        self.age_entry.grid(column=1, row=3, padx=10, pady=5)

        health_info_label = ttk.Label(self.members_tab, text="Health Info:")
        health_info_label.grid(column=0, row=4, padx=10, pady=5, sticky='E')
        self.health_info_entry = ttk.Entry(self.members_tab)
        self.health_info_entry.grid(column=1, row=4, padx=10, pady=5)

        membership_status_label = ttk.Label(self.members_tab, text="Membership Status:")
        membership_status_label.grid(column=0, row=5, padx=10, pady=5, sticky='E')
        self.membership_status_combobox = ttk.Combobox(self.members_tab, values=["Regular", "Premium", "Trial"])
        self.membership_status_combobox.grid(column=1, row=5, padx=10, pady=5)

        add_member_button = ttk.Button(self.members_tab, text="Add Member", command=self.add_member)
        add_member_button.grid(column=1, row=6, padx=10, pady=10)

        self.members_treeview = ttk.Treeview(self.members_tab, columns=('ID', 'Name', 'Age', 'Health', 'Status'), show='headings')
        self.members_treeview.heading('ID', text='Member ID')
        self.members_treeview.heading('Name', text='Name')
        self.members_treeview.heading('Age', text='Age')
        self.members_treeview.heading('Health', text='Health Info')
        self.members_treeview.heading('Status', text='Membership Status')
        self.members_treeview.grid(column=0, row=7, columnspan=2, padx=10, pady=10, sticky='nsew')

        self.members_tab.grid_columnconfigure(1, weight=1)
        self.members_tab.grid_rowconfigure(7, weight=1)

    def create_appointments_tab(self):
        header = ttk.Label(self.appointments_tab, text="Appointments Management", style='Header.TLabel')
        header.grid(column=0, row=0, columnspan=2, pady=10)

        appointment_id_label = ttk.Label(self.appointments_tab, text="Appointment ID:")
        appointment_id_label.grid(column=0, row=1, padx=10, pady=5, sticky='E')
        self.appointment_id_entry = ttk.Entry(self.appointments_tab)
        self.appointment_id_entry.grid(column=1, row=1, padx=10, pady=5)

        member_label = ttk.Label(self.appointments_tab, text="Member:")
        member_label.grid(column=0, row=2, padx=10, pady=5, sticky='E')
        self.member_entry = ttk.Entry(self.appointments_tab)
        self.member_entry.grid(column=1, row=2, padx=10, pady=5)

        trainer_label = ttk.Label(self.appointments_tab, text="Trainer:")
        trainer_label.grid(column=0, row=3, padx=10, pady=5, sticky='E')
        self.trainer_entry = ttk.Entry(self.appointments_tab)
        self.trainer_entry.grid(column=1, row=3, padx=10, pady=5)

        datetime_label = ttk.Label(self.appointments_tab, text="Date and Time:")
        datetime_label.grid(column=0, row=4, padx=10, pady=5, sticky='E')
        self.datetime_entry = ttk.Entry(self.appointments_tab)
        self.datetime_entry.grid(column=1, row=4, padx=10, pady=5)

        session_type_label = ttk.Label(self.appointments_tab, text="Session Type:")
        session_type_label.grid(column=0, row=5, padx=10, pady=5, sticky='E')
        self.session_type_entry = ttk.Entry(self.appointments_tab)
        self.session_type_entry.grid(column=1, row=5, padx=10, pady=5)

        add_appointment_button = ttk.Button(self.appointments_tab, text="Add Appointment", command=self.add_appointment)
        add_appointment_button.grid(column=1, row=6, padx=10, pady=10)

        self.appointments_treeview = ttk.Treeview(self.appointments_tab, columns=('ID', 'Member', 'Trainer', 'DateTime', 'Session'), show='headings')
        self.appointments_treeview.heading('ID', text='Appointment ID')
        self.appointments_treeview.heading('Member', text='Member')
        self.appointments_treeview.heading('Trainer', text='Trainer')
        self.appointments_treeview.heading('DateTime', text='Date and Time')
        self.appointments_treeview.heading('Session', text='Session Type')
        self.appointments_treeview.grid(column=0, row=7, columnspan=2, padx=10, pady=10, sticky='nsew')

        self.appointments_tab.grid_columnconfigure(1, weight=1)
        self.appointments_tab.grid_rowconfigure(7, weight=1)

    def create_payments_tab(self):
        header = ttk.Label(self.payments_tab, text="Payments Management", style='Header.TLabel')
        header.grid(column=0, row=0, columnspan=2, pady=10)

        payment_id_label = ttk.Label(self.payments_tab, text="Payment ID:")
        payment_id_label.grid(column=0, row=1, padx=10, pady=5, sticky='E')
        self.payment_id_entry = ttk.Entry(self.payments_tab)
        self.payment_id_entry.grid(column=1, row=1, padx=10, pady=5)

        member_label = ttk.Label(self.payments_tab, text="Member:")
        member_label.grid(column=0, row=2, padx=10, pady=5, sticky='E')
        self.payment_member_entry = ttk.Entry(self.payments_tab)
        self.payment_member_entry.grid(column=1, row=2, padx=10, pady=5)

        amount_label = ttk.Label(self.payments_tab, text="Amount:")
        amount_label.grid(column=0, row=3, padx=10, pady=5, sticky='E')
        self.amount_entry = ttk.Entry(self.payments_tab)
        self.amount_entry.grid(column=1, row=3, padx=10, pady=5)

        payment_date_label = ttk.Label(self.payments_tab, text="Payment Date:")
        payment_date_label.grid(column=0, row=4, padx=10, pady=5, sticky='E')
        self.payment_date_entry = ttk.Entry(self.payments_tab)
        self.payment_date_entry.grid(column=1, row=4, padx=10, pady=5)

        payment_method_label = ttk.Label(self.payments_tab, text="Payment Method:")
        payment_method_label.grid(column=0, row=5, padx=10, pady=5, sticky='E')
        self.payment_method_entry = ttk.Entry(self.payments_tab)
        self.payment_method_entry.grid(column=1, row=5, padx=10, pady=5)

        add_payment_button = ttk.Button(self.payments_tab, text="Add Payment", command=self.add_payment)
        add_payment_button.grid(column=1, row=6, padx=10, pady=10)

        self.payments_treeview = ttk.Treeview(self.payments_tab, columns=('ID', 'Member', 'Amount', 'Date', 'Method'), show='headings')
        self.payments_treeview.heading('ID', text='Payment ID')
        self.payments_treeview.heading('Member', text='Member')
        self.payments_treeview.heading('Amount', text='Amount')
        self.payments_treeview.heading('Date', text='Payment Date')
        self.payments_treeview.heading('Method', text='Payment Method')
        self.payments_treeview.grid(column=0, row=7, columnspan=2, padx=10, pady=10, sticky='nsew')

        self.payments_tab.grid_columnconfigure(1, weight=1)
        self.payments_tab.grid_rowconfigure(7, weight=1)

    def create_subscriptions_tab(self):
        header = ttk.Label(self.subscriptions_tab, text="Subscriptions Management", style='Header.TLabel')
        header.grid(column=0, row=0, columnspan=2, pady=10)

        subscription_id_label = ttk.Label(self.subscriptions_tab, text="Subscription ID:")
        subscription_id_label.grid(column=0, row=1, padx=10, pady=5, sticky='E')
        self.subscription_id_entry = ttk.Entry(self.subscriptions_tab)
        self.subscription_id_entry.grid(column=1, row=1, padx=10, pady=5)

        member_label = ttk.Label(self.subscriptions_tab, text="Member:")
        member_label.grid(column=0, row=2, padx=10, pady=5, sticky='E')
        self.subscription_member_entry = ttk.Entry(self.subscriptions_tab)
        self.subscription_member_entry.grid(column=1, row=2, padx=10, pady=5)

        plan_label = ttk.Label(self.subscriptions_tab, text="Plan:")
        plan_label.grid(column=0, row=3, padx=10, pady=5, sticky='E')
        self.plan_entry = ttk.Entry(self.subscriptions_tab)
        self.plan_entry.grid(column=1, row=3, padx=10, pady=5)

        start_date_label = ttk.Label(self.subscriptions_tab, text="Start Date:")
        start_date_label.grid(column=0, row=4, padx=10, pady=5, sticky='E')
        self.start_date_entry = ttk.Entry(self.subscriptions_tab)
        self.start_date_entry.grid(column=1, row=4, padx=10, pady=5)

        end_date_label = ttk.Label(self.subscriptions_tab, text="End Date:")
        end_date_label.grid(column=0, row=5, padx=10, pady=5, sticky='E')
        self.end_date_entry = ttk.Entry(self.subscriptions_tab)
        self.end_date_entry.grid(column=1, row=5, padx=10, pady=5)

        add_subscription_button = ttk.Button(self.subscriptions_tab, text="Add Subscription", command=self.add_subscription)
        add_subscription_button.grid(column=1, row=6, padx=10, pady=10)

        self.subscriptions_treeview = ttk.Treeview(self.subscriptions_tab, columns=('ID', 'Member', 'Plan', 'Start Date', 'End Date'), show='headings')
        self.subscriptions_treeview.heading('ID', text='Subscription ID')
        self.subscriptions_treeview.heading('Member', text='Member')
        self.subscriptions_treeview.heading('Plan', text='Plan')
        self.subscriptions_treeview.heading('Start Date', text='Start Date')
        self.subscriptions_treeview.heading('End Date', text='End Date')
        self.subscriptions_treeview.grid(column=0, row=7, columnspan=2, padx=10, pady=10, sticky='nsew')

        self.subscriptions_tab.grid_columnconfigure(1, weight=1)
        self.subscriptions_tab.grid_rowconfigure(7, weight=1)

    def create_attendance_tab(self):
        header = ttk.Label(self.attendance_tab, text="Attendance Tracking", style='Header.TLabel')
        header.grid(column=0, row=0, columnspan=2, pady=10)

        member_label = ttk.Label(self.attendance_tab, text="Member:")
        member_label.grid(column=0, row=1, padx=10, pady=5, sticky='E')
        self.attendance_member_entry = ttk.Entry(self.attendance_tab)
        self.attendance_member_entry.grid(column=1, row=1, padx=10, pady=5)

        class_label = ttk.Label(self.attendance_tab, text="Class:")
        class_label.grid(column=0, row=2, padx=10, pady=5, sticky='E')
        self.class_entry = ttk.Entry(self.attendance_tab)
        self.class_entry.grid(column=1, row=2, padx=10, pady=5)

        date_label = ttk.Label(self.attendance_tab, text="Date:")
        date_label.grid(column=0, row=3, padx=10, pady=5, sticky='E')
        self.attendance_date_entry = ttk.Entry(self.attendance_tab)
        self.attendance_date_entry.grid(column=1, row=3, padx=10, pady=5)

        log_attendance_button = ttk.Button(self.attendance_tab, text="Log Attendance", command=self.log_attendance)
        log_attendance_button.grid(column=1, row=4, padx=10, pady=10)

        self.attendance_treeview = ttk.Treeview(self.attendance_tab, columns=('Member', 'Class', 'Date'), show='headings')
        self.attendance_treeview.heading('Member', text='Member')
        self.attendance_treeview.heading('Class', text='Class')
        self.attendance_treeview.heading('Date', text='Date')
        self.attendance_treeview.grid(column=0, row=5, columnspan=2, padx=10, pady=10, sticky='nsew')

        self.attendance_tab.grid_columnconfigure(1, weight=1)
        self.attendance_tab.grid_rowconfigure(5, weight=1)

    def create_staff_tab(self):
        header = ttk.Label(self.staff_tab, text="Staff Management Dashboard", style='Header.TLabel')
        header.grid(column=0, row=0, columnspan=2, pady=10)

        # Mockup data
        self.membership_growth_label = ttk.Label(self.staff_tab, text="Membership Growth: 10%")
        self.membership_growth_label.grid(column=0, row=1, padx=10, pady=5, sticky='W')

        self.revenue_trends_label = ttk.Label(self.staff_tab, text="Revenue Trends: Upward")
        self.revenue_trends_label.grid(column=0, row=2, padx=10, pady=5, sticky='W')

        self.trainer_schedules_label = ttk.Label(self.staff_tab, text="Trainer Schedules: Available")
        self.trainer_schedules_label.grid(column=0, row=3, padx=10, pady=5, sticky='W')

        self.equipment_maintenance_label = ttk.Label(self.staff_tab, text="Equipment Maintenance: No Issues")
        self.equipment_maintenance_label.grid(column=0, row=4, padx=10, pady=5, sticky='W')

    # Command methods for button actions
    def add_gym(self):
        gym_id = self.gym_id_entry.get()
        city = self.city_entry.get()
        manager = self.manager_entry.get()
        self.gyms_treeview.insert('', 'end', values=(gym_id, city, manager))
        self.clear_gym_entries()

    def add_zone(self):
        zone_id = self.zone_id_entry.get()
        exercise = self.exercise_entry.get()
        attendant = self.attendant_entry.get()
        self.zones_treeview.insert('', 'end', values=(zone_id, exercise, attendant))
        self.clear_zone_entries()

    def add_member(self):
        member_id = self.member_id_entry.get()
        name = self.name_entry.get()
        age = self.age_entry.get()
        health_info = self.health_info_entry.get()
        status = self.membership_status_combobox.get()
        self.members_treeview.insert('', 'end', values=(member_id, name, age, health_info, status))
        self.clear_member_entries()

    def add_appointment(self):
        appointment_id = self.appointment_id_entry.get()
        member = self.member_entry.get()
        trainer = self.trainer_entry.get()
        date_time = self.datetime_entry.get()
        session = self.session_type_entry.get()
        self.appointments_treeview.insert('', 'end', values=(appointment_id, member, trainer, date_time, session))
        self.clear_appointment_entries()

    def add_payment(self):
        payment_id = self.payment_id_entry.get()
        member = self.payment_member_entry.get()
        amount = self.amount_entry.get()
        date = self.payment_date_entry.get()
        method = self.payment_method_entry.get()
        self.payments_treeview.insert('', 'end', values=(payment_id, member, amount, date, method))
        self.clear_payment_entries()

    def add_subscription(self):
        subscription_id = self.subscription_id_entry.get()
        member = self.subscription_member_entry.get()
        plan = self.plan_entry.get()
        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()
        self.subscriptions_treeview.insert('', 'end', values=(subscription_id, member, plan, start_date, end_date))
        self.clear_subscription_entries()

    def log_attendance(self):
        member = self.attendance_member_entry.get()
        class_name = self.class_entry.get()
        date = self.attendance_date_entry.get()
        self.attendance_treeview.insert('', 'end', values=(member, class_name, date))
        self.clear_attendance_entries()

    # Helper methods to clear entries
    def clear_gym_entries(self):
        self.gym_id_entry.delete(0, 'end')
        self.city_entry.delete(0, 'end')
        self.manager_entry.delete(0, 'end')

    def clear_zone_entries(self):
        self.zone_id_entry.delete(0, 'end')
        self.exercise_entry.delete(0, 'end')
        self.attendant_entry.delete(0, 'end')

    def clear_member_entries(self):
        self.member_id_entry.delete(0, 'end')
        self.name_entry.delete(0, 'end')
        self.age_entry.delete(0, 'end')
        self.health_info_entry.delete(0, 'end')
        self.membership_status_combobox.set('')

    def clear_appointment_entries(self):
        self.appointment_id_entry.delete(0, 'end')
        self.member_entry.delete(0, 'end')
        self.trainer_entry.delete(0, 'end')
        self.datetime_entry.delete(0, 'end')
        self.session_type_entry.delete(0, 'end')

    def clear_payment_entries(self):
        self.payment_id_entry.delete(0, 'end')
        self.payment_member_entry.delete(0, 'end')
        self.amount_entry.delete(0, 'end')
        self.payment_date_entry.delete(0, 'end')
        self.payment_method_entry.delete(0, 'end')

    def clear_subscription_entries(self):
        self.subscription_id_entry.delete(0, 'end')
        self.subscription_member_entry.delete(0, 'end')
        self.plan_entry.delete(0, 'end')
        self.start_date_entry.delete(0, 'end')
        self.end_date_entry.delete(0, 'end')

    def clear_attendance_entries(self):
        self.attendance_member_entry.delete(0, 'end')
        self.class_entry.delete(0, 'end')
        self.attendance_date_entry.delete(0, 'end')

# Run the application
root = tk.Tk()
app = GymApp(root)
root.mainloop()
