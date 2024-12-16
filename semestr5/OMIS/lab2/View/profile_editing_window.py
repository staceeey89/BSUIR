import tkinter as tk

class ProfileEditingWindow(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.display_profile_editing_window()

    def display_profile_editing_window(self):
        tk.Label(self, text="Edit Profile", font=("Arial", 16)).pack(pady=10)

        tk.Label(self, text="Username:").pack(pady=5)
        self.username_entry = tk.Entry(self)
        self.username_entry.pack(pady=5)

        tk.Label(self, text="Password:").pack(pady=5)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self, text="Save Changes", command=self.save_changes).pack(pady=10)
        tk.Button(self, text="Cancel", command=self.cancel).pack(pady=10)

    def save_changes(self):
        print("Saving Profile Changes")  # Заглушка

    def cancel(self):
        self.controller.show_frame(self.controller.frames[RepresentativeDashboard])
