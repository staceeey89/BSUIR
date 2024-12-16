import tkinter as tk
from tkinter import messagebox, ttk
from View.registration_window import RegistrationWindow
from View.visitor_dashboard import VisitorDashboard
from View.representative_dashboard import RepresentativeDashboard


class AuthWindow(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.display_auth_screen()

    def display_auth_screen(self):
        tk.Label(self, text="Login", font=("Arial", 16)).pack(pady=10)
        tk.Label(self, text="Логин", font=("Arial", 12)).pack(pady=10)
        self.login_entry = ttk.Entry(self)
        self.login_entry.pack(pady=5)
        tk.Label(self, text="Пароль", font=("Arial", 12)).pack(pady=10)
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self, text="Войти как посетитель", command=self.login_as_visitor).pack(pady=10)
        tk.Button(self, text="Войти как представитель", command=self.login_as_representative).pack(pady=10)
        tk.Button(self, text="Регистрация", command=self.go_to_registration).pack(pady=10)

    def login_as_visitor(self):
        self.controller.show_frame(VisitorDashboard)

    def login_as_representative(self):
        self.controller.show_frame(RepresentativeDashboard)

    def go_to_registration(self):
        self.controller.show_frame(RegistrationWindow)
