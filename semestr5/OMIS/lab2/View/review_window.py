import tkinter as tk

class ReviewWindow(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.display_review_window()

    def display_review_window(self):
        self.review_label = tk.Label(self, text="Leave a Review", font=("Arial", 16))
        self.review_label.pack(pady=10)

        tk.Label(self, text="Rate the product:").pack(pady=5)
        self.rating = tk.Scale(self, from_=1, to_=5, orient="horizontal")
        self.rating.pack(pady=10)

        tk.Label(self, text="Your review:").pack(pady=5)
        self.review_text = tk.Text(self, height=5, width=40)
        self.review_text.pack(pady=10)

        tk.Button(self, text="Submit Review", command=self.submit_review).pack(pady=10)
        tk.Button(self, text="Back to Product", command=self.back_to_product).pack(pady=10)

    def submit_review(self):
        print("Review submitted")  # Заглушка

    def back_to_product(self):
        self.controller.show_frame(self.controller.frames[ProductDetailsWindow])
