import tkinter
import time

from tkinter import ttk

from pytop.utils import get_all_windows,  get_windows_processes
from pytop.widgets import create_process_tree


class App:
    """ The App class initializes the PyTop GUI. """

    def __init__(self):
        """ Create a new window and initialize widgets. """
        self.root = tkinter.Tk()

        self.root.title("PyTop")
        self.root.geometry("500x500")

        self._create_widgets()

    def _create_widgets(self):
        """ Build the necessary widgets (Notebook and TreeView). """
        self.notebook = ttk.Notebook(self.root)

        processes = get_windows_processes(get_all_windows())

        self.tree = create_process_tree(self.notebook, processes)

        self.notebook.add(self.tree, text="Apps")
        self.notebook.pack(expand=True, fill="both")

    def _update_tree(self):
        """ Update the TreeView every second. """
        processes = get_windows_processes(get_all_windows())

        for children in self.tree.get_children():
            self.tree.delete(children)

        for process in processes:
            self.tree.insert("", "end", values=process)

        self.root.after(1000, self._update_tree)

    def start(self):
        """ Start the main loop. """
        self.root.after(1000, self._update_tree)
        self.root.mainloop()
