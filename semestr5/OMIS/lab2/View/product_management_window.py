import tkinter as tk
from View.product_editing_window import ProductEditingWindow

class ProductManagementWindow(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.display_product_management_window()

    def display_product_management_window(self):
        tk.Label(self, text="Product Management", font=("Arial", 16)).pack(pady=10)

        tk.Button(self, text="Add New Product", command=self.add_new_product).pack(pady=10)
        tk.Button(self, text="Edit Existing Product", command=self.edit_existing_product).pack(pady=10)
        tk.Button(self, text="Delete Product", command=self.delete_product).pack(pady=10)
        tk.Button(self, text="Back to Dashboard", command=self.back_to_dashboard).pack(pady=10)

    def add_new_product(self):
        self.controller.show_frame(ProductEditingWindow)

    def edit_existing_product(self):
        print("Editing Existing Product")  # Заглушка

    def delete_product(self):
        print("Deleting Product")  # Заглушка

    def back_to_dashboard(self):
        self.controller.show_frame(self.controller.frames[RepresentativeDashboard])
