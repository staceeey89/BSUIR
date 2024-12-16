import tkinter as tk
from View.product_management_window import ProductManagementWindow
from View.manage_stands_window import ManageStandsWindow

class RepresentativeDashboard(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Representative Dashboard", font=("Arial", 18), bg="black", fg="white").grid(row=0, column=0, columnspan=2, pady=10, sticky="nsew")

        menu_label = tk.Label(self, text="Menu", font=("Arial", 14, "bold"), bg="black", fg="white")
        menu_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)

        tk.Button(self, text="My Profile", command=self.open_profile, width=20).grid(row=2, column=0, padx=10, pady=5)
        tk.Button(self, text="Logout", command=self.logout, width=20).grid(row=3, column=0, padx=10, pady=5)
        tk.Button(self, text="Product Management", command=self.open_product_management, width=20).grid(row=4, column=0, padx=10, pady=5)
        tk.Button(self, text="Manage Stands", command=self.open_manage_stands, width=20).grid(row=5, column=0, padx=10, pady=5)

        action_label = tk.Label(self, text="Dashboard Actions", font=("Arial", 14, "bold"), bg="black", fg="white")
        action_label.grid(row=1, column=1, sticky="w", padx=10, pady=5)

        tk.Button(self, text="Edit Profile", bg="red", fg="white", width=20, height=2, command=self.open_profile).grid(row=2, column=1, padx=10, pady=5)
        tk.Button(self, text="Create New Product", bg="red", fg="white", width=20, height=2, command=self.open_product_management).grid(row=3, column=1, padx=10, pady=5)

    def open_profile(self):
        print("Profile Editing Window Opened")  # Заглушка

    def logout(self):
        print("Logged Out")  # Заглушка

    def open_manage_stands(self):
        self.controller.show_frame(ManageStandsWindow)

    def open_product_management(self):
        self.controller.show_frame(ProductManagementWindow)
