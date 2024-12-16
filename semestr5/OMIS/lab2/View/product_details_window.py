import tkinter as tk

class ProductDetailsWindow(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.display_product_details()

    def display_product_details(self):
        self.product_label = tk.Label(self, text="Product Details", font=("Arial", 16))
        self.product_label.pack(pady=10)

        tk.Label(self, text="Description of the product").pack(pady=10)

        tk.Button(self, text="Buy Product", command=self.buy_product).pack(pady=10)
        tk.Button(self, text="Back to Stand", command=self.back_to_stand).pack(pady=10)

    def buy_product(self):
        print("Buying Product")  # Заглушка

    def back_to_stand(self):
        self.controller.show_frame(self.controller.frames[ExhibitionStandView])
