import tkinter as tk
from View.auth_window import AuthWindow
from View.registration_window import RegistrationWindow
from View.visitor_dashboard import VisitorDashboard
from View.representative_dashboard import RepresentativeDashboard
from View.manage_stands_window import ManageStandsWindow
from View.product_management_window import ProductManagementWindow
from View.profile_editing_window import ProfileEditingWindow
from View.exhibition_stand_view import ExhibitionStandView
from View.product_details_window import ProductDetailsWindow
from View.review_window import ReviewWindow
from View.exhibition_stand_management_window import ExhibitionStandManagementWindow
from View.product_editing_window import ProductEditingWindow


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.container = tk.Frame(self)
        self.container.pack(expand=True, fill="both")
        self.title("Exhibition Platform")
        self.geometry("800x600")
        self.frames = {}

        # Create all frames
        for FrameClass in (
                AuthWindow,
                RegistrationWindow,
                VisitorDashboard,
                RepresentativeDashboard,
                ManageStandsWindow,
                ProductManagementWindow,
                ProfileEditingWindow,
                ExhibitionStandView,
                ProductDetailsWindow,
                ReviewWindow,
                ExhibitionStandManagementWindow,
                ProductEditingWindow,
        ):
            frame = FrameClass(self.container, self)
            self.frames[FrameClass] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        # Show initial frame
        self.show_frame(AuthWindow)

    def show_frame(self, page_class):
        frame = self.frames[page_class]
        frame.tkraise()


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
