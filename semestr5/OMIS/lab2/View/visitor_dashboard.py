import tkinter as tk
from View.exhibition_stand_view import ExhibitionStandView

class VisitorDashboard(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.display_dashboard()

    def display_dashboard(self):
        tk.Label(self, text="Exhibition Stands", font=("Arial", 18)).pack(pady=10)

        # Example stands (can be dynamic)
        for stand_num in range(1, 4):
            stand_frame = tk.Frame(self, bd=2, relief="raised", padx=10, pady=5)
            stand_frame.pack(pady=10, padx=10, fill="x")

            tk.Label(stand_frame, text=f"Stand {stand_num}", font=("Arial", 14)).pack(side="left", padx=10)
            tk.Button(stand_frame, text="Visit Stand", command=lambda s=stand_num: self.visit_stand(s)).pack(side="right")

        tk.Button(self, text="Выход", command=self.exit_app).pack(pady=10)

    def visit_stand(self, stand_num):
        self.controller.frames[ExhibitionStandView].update_stand(stand_num)
        self.controller.show_frame(ExhibitionStandView)

    def exit_app(self):
        self.controller.quit()
