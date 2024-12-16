import tkinter as tk


class ExhibitionStandManagementWindow(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.display_stand_management_window()

    def display_stand_management_window(self):
        tk.Label(self, text="Manage Exhibition Stand", font=("Arial", 16)).pack(pady=10)

        tk.Label(self, text="Stand Name:").pack(pady=5)
        self.stand_name_entry = tk.Entry(self)
        self.stand_name_entry.pack(pady=5)

        tk.Label(self, text="Stand Description:").pack(pady=5)
        self.stand_description_entry = tk.Entry(self)
        self.stand_description_entry.pack(pady=5)

        tk.Button(self, text="Save Stand", command=self.save_stand).pack(pady=10)
        tk.Button(self, text="Cancel", command=self.cancel).pack(pady=10)

    def save_stand(self):
        print("Saving Stand")  # Заглушка

    def cancel(self):
        self.controller.show_frame(self.controller.frames[ManageStandsWindow])
