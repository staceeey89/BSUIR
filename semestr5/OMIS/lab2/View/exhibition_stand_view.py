import tkinter as tk

class ExhibitionStandView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.display_stand_details()

    def display_stand_details(self):
        self.stand_label = tk.Label(self, text="Exhibition Stand", font=("Arial", 16))
        self.stand_label.pack(pady=10)

        self.product_listbox = tk.Listbox(self)
        self.product_listbox.pack(pady=10)

        self.product_listbox.insert(tk.END, "Product 1")
        self.product_listbox.insert(tk.END, "Product 2")
        self.product_listbox.insert(tk.END, "Product 3")

        tk.Button(self, text="View Product Details", command=self.view_product_details).pack(pady=10)
        tk.Button(self, text="Leave Stand", command=self.leave_stand).pack(pady=10)

    def update_stand(self, stand_num):
        self.stand_label.config(text=f"Exhibition Stand {stand_num}")

    def view_product_details(self):
        print("Viewing Product Details")  # Заглушка

    def leave_stand(self):
        self.controller.show_frame(self.controller.frames[VisitorDashboard])
