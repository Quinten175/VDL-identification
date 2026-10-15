import os
import tkinter as tk
from .gui_drawer import GUIDrawer

class GUI(GUIDrawer):
    def __init__(self):
        self.app = tk.Tk()
        super().__init__(self.app)
        self.app.title("Synthetic data generation")

        self.app.geometry("1000x500")
        self.app.resizable(width=False, height=False)

        self.center_window()

        # file browser
        cad_types = [
            ("CAD files", "*.step *.stp *.iges *.igs *.stl"),
            ("All files", "*.*")
        ]
        self.cad_path = None
        self.browse_file(cad_types, "cad_path", "CAD File Selection")

        # config browser
        config_types = [
            ("CFG files", "*.cfg"),
        ]
        self.config_path = os.path.abspath("../config/default.cfg")
        self.browse_file(config_types, "config_path", "Config File Selection")

        # environment browser
        env_types = [
            ("Environment files", "*.hdr, *.exr"),
        ]
        self.env_path = None
        self.browse_file(env_types, "env_path", "Environment Selection")

        # button frame
        bottom_frame = tk.Frame(self.app)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)
        self.start_button = tk.Button(
            bottom_frame,
            text="Start pipeline",
            command=self.start_task,
            font=("Arial", 14, "bold"),
            padx=20,
            pady=10
        )
        self.start_button.pack(side=tk.RIGHT, padx=(0, 10))
        self.validate_able_start()

        self.app.mainloop()

    def center_window(self):
        self.app.update_idletasks()

        width = self.app.winfo_width()
        height = self.app.winfo_height()

        x = (self.app.winfo_screenwidth() - width) // 2
        y = (self.app.winfo_screenheight() - height) // 2

        self.app.geometry(f"{width}x{height}+{x}+{y}")

    def validate_able_start(self):
        is_valid = tk.NORMAL

        if self.cad_path is None:
            is_valid = tk.DISABLED

        if self.config_path is None:
            is_valid = tk.DISABLED

        if self.env_path is None:
            is_valid = tk.DISABLED

        self.start_button.config(state=is_valid)

        self.app.after(200, self.validate_able_start)

    def start_task(self):
        pass