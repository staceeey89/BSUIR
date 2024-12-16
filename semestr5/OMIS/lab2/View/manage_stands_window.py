import tkinter as tk
from View.exhibition_stand_management_window import ExhibitionStandManagementWindow


class ManageStandsWindow(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.display_manage_stands_window()

    def display_manage_stands_window(self):
        tk.Label(self, text="Manage Exhibition Stands", font=("Arial", 16)).pack(pady=10)

        tk.Button(self, text="Add New Stand", command=self.add_new_stand).pack(pady=10)
        tk.Button(self, text="Edit Existing Stand", command=self.edit_existing_stand).pack(pady=10)
        tk.Button(self, text="Delete Stand", command=self.delete_stand).pack(pady=10)
        tk.Button(self, text="Back to Dashboard", command=self.back_to_dashboard).pack(pady=10)

    def add_new_stand(self):
        self.controller.show_frame(ExhibitionStandManagementWindow)

    def edit_existing_stand(self):
        print("Editing Existing Stand")  # Заглушка

    def delete_stand(self):
        print("Deleting Stand")  # Заглушка

    def back_to_dashboard(self):
        self.controller.show_frame(self.controller.frames[RepresentativeDashboard])
