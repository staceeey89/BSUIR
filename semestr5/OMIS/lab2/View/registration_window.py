import tkinter as tk
from tkinter import messagebox, ttk
from View.visitor_dashboard import VisitorDashboard
from View.representative_dashboard import RepresentativeDashboard
import sys
sys.path.append('C:/Users/Anastasiya/PycharmProjects/omis2labt/View')  # Путь к вашему каталогу



class RegistrationWindow(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.display_registration_screen()

    def display_registration_screen(self):
        tk.Label(self, text="Register", font=("Arial", 16)).pack(pady=10)

        tk.Label(self, text="Логин", font=("Arial", 12)).pack(pady=10)
        self.register_login_entry = ttk.Entry(self)
        self.register_login_entry.pack(pady=5)

        tk.Label(self, text="Пароль", font=("Arial", 12)).pack(pady=10)
        self.register_password_entry = ttk.Entry(self, show="*")
        self.register_password_entry.pack(pady=5)

        tk.Button(self, text="Зарегистрироваться как посетитель", command=self.register_as_visitor).pack(pady=10)
        tk.Button(self, text="Зарегистрироваться как представитель", command=self.register_as_representative).pack(pady=10)
        tk.Button(self, text="Назад к входу", command=self.go_to_auth).pack(pady=10)

    def register_as_visitor(self):
        username = self.register_login_entry.get()
        password = self.register_password_entry.get()
        if username and password:
            messagebox.showinfo("Success", "Registration successful as Visitor")
            self.controller.show_frame(VisitorDashboard)
        else:
            messagebox.showerror("Error", "Please fill in all fields")

    def register_as_representative(self):
        username = self.register_login_entry.get()
        password = self.register_password_entry.get()
        if username and password:
            messagebox.showinfo("Success", "Registration successful as Representative")
            self.controller.show_frame(RepresentativeDashboard)
        else:
            messagebox.showerror("Error", "Please fill in all fields")

    def go_to_auth(self):
        # Перемещаем импорт внутри метода, чтобы избежать циклической зависимости
        from View.auth_window import AuthWindow
        self.controller.show_frame("AuthWindow")
