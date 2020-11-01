import tkinter

from tkinter import ttk
from tkinter.font import Font


def create_process_tree(container, processes):
    """ Create the process tree widget.

    This methods creates a ``TreeView`` containing the processes listed by 
    the system monitor.

    :param container: the frame container.
    :param processes: the active processes.
    :return: a ``TreeView`` widget.
    """
    process_columns = ("PID", "Name", "Status", "CPU", "Memory", "Threads")

    tree = ttk.Treeview(container, columns=process_columns, show="headings")

    tree.grid(column=0, row=0, sticky="nsew", in_=container)

    for column in process_columns:
        tree.heading(column, text=column.title())
        tree.column(column, width=Font().measure(column.title()))

    for process in processes:
        tree.insert("", "end", values=process)

    container.grid_columnconfigure(0, weight=1)
    container.grid_rowconfigure(0, weight=1)

    return tree
