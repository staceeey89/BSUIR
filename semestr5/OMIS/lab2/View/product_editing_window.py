import tkinter as tk

class ProductEditingWindow(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.display_product_editing_window()

    def display_product_editing_window(self):
        tk.Label(self, text="Edit Product", font=("Arial", 16)).pack(pady=10)

        tk.Label(self, text="Product Name:").pack(pady=5)
        self.product_name_entry = tk.Entry(self)
        self.product_name_entry.pack(pady=5)

        tk.Label(self, text="Product Description:").pack(pady=5)
        self.product_description_entry = tk.Entry(self)
        self.product_description_entry.pack(pady=5)

        tk.Button(self, text="Save Product", command=self.save_product).pack(pady=10)
        tk.Button(self, text="Cancel", command=self.cancel).pack(pady=10)

    def save_product(self):
        print("Saving Product")  # Заглушка

    def cancel(self):
        self.controller.show_frame("ProductManagementWindow")
