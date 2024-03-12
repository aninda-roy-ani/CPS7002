class Task:

    def __init__(self, title, description, assigned_to, status="New"):
        self.title = title
        self.description = description
        self.assigned_to = assigned_to
        self.status = status

    def display(self):
        print("Title:", self.title)
        print("Description:", self.description)
        print("Assigned To:", self.assigned_to)
        print("Status:", self.status)