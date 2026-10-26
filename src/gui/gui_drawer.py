import os
import tkinter as tk
from tkinter import filedialog

class GUIDrawer:
    def __init__(self, app):
        self.app = app
        self.tooltips = {}

    @staticmethod
    def truncate_path(path, max_length=45):
        if len(path) <= max_length:
            return path
        return "..." + path[-(max_length - 3):]

    @staticmethod
    def create_tooltip(widget, text):
        tooltip = tk.Toplevel(widget)
        tooltip.withdraw()
        tooltip.overrideredirect(True)

        label = tk.Label(
            tooltip,
            text=text,
            background="#ffffe0",
            relief="solid",
            borderwidth=1,
            padx=5,
            pady=3
        )
        label.pack()

        def show(event):
            tooltip.geometry(f"+{event.x_root + 10}+{event.y_root + 10}")
            tooltip.deiconify()

        def hide(_event):
            tooltip.withdraw()

        widget.bind("<Enter>", show)
        widget.bind("<Leave>", hide)

        return tooltip

    def input_group(self, title, width_percent=100, height_percent=10):
        self.app.update_idletasks()

        app_width = self.app.winfo_width()
        app_height = self.app.winfo_height()

        width = int(app_width * width_percent / 100)
        height = int(app_height * height_percent / 100) if height_percent is not None else None

        group = tk.LabelFrame(self.app, text=title, padx=10, pady=10)

        if height is None:
            group.configure(width=width)
            group.pack(anchor="nw", fill="x", padx=10, pady=10)
            group.pack_propagate(False)
        else:
            group.configure(width=width, height=height)
            group.pack(anchor="nw", padx=10, pady=10)
            group.pack_propagate(False)

        return group

    def browse_file(self, types, var_name, title):
        group = self.input_group(title, width_percent=50, height_percent=15)

        frame = tk.Frame(group)
        frame.pack(anchor="w", fill="x")

        current_path = str(getattr(self, var_name, None))
        initial_text = self.truncate_path(current_path) if current_path else "No file selected"

        path_label = tk.Label(frame, text=initial_text, width=40, anchor="w")
        path_label.pack(side=tk.LEFT, padx=(0, 10))

        if current_path:
            self.set_tooltip(path_label, current_path)

        browse_button = tk.Button(
            frame,
            text="Browse files",
            command=lambda: self.select_file(path_label, types, var_name)
        )
        browse_button.pack(side=tk.RIGHT, padx=(0, 10))

    def select_file(self, label, types, var_name):
        current_path = str(getattr(self, var_name, None))

        options = {
            "parent": self.app,
            "title": "Select a file",
            "filetypes": types
        }

        if current_path:
            if os.path.isfile(current_path):
                options["initialdir"] = os.path.dirname(current_path)
                options["initialfile"] = os.path.basename(current_path)
            elif os.path.isdir(current_path):
                options["initialdir"] = current_path

        file_path = filedialog.askopenfilename(**options)

        if file_path:
            setattr(self, var_name, file_path)
            label.config(text=self.truncate_path(file_path))
            self.set_tooltip(label, file_path)

        return file_path

    def set_tooltip(self, widget, text):
        widget_id = str(widget)

        if widget_id in self.tooltips:
            self.tooltips[widget_id].destroy()

        self.tooltips[widget_id] = self.create_tooltip(widget, text)



