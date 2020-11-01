import sys
import win32gui
import win32process


def get_all_windows():
    """ Create a list of all the active windows and it"s associated PIDs.

    This data will then be used by ``psutil``, in order to create a dynamic CLI
    with CPU/RAM/disk info.

    :return: a list containing dictionaries with names and PIDs.
    """
    windows = []

    win32gui.EnumWindows(construct_windows_list, windows)

    return windows


def construct_windows_list(hwnd, strings):
    """ Callback filtering function.

    Will receive a window and a list of strings, this method will check if
    the window is visible and active, if it is, it will append it to the
    ``strings`` list, along with its PID.

    :param hwnd: the current window.
    :param strings: the list of window names.
    :return: true.
    """
    if win32gui.IsWindowVisible(hwnd):
        title = win32gui.GetWindowText(hwnd)
        pid = get_window_pid(title)

        left, top, right, bottom = win32gui.GetWindowRect(hwnd)

        if title and right - left and bottom - top:
            strings.append({"title": title, "pid": pid})

    return True


def get_window_pid(title):
    """ Return a window"s PID.

    This method retrieves a window"s PID given its title through the 
    ``win32process`` api.

    :param title: the window title.
    :return: the window"s PID.
    """
    hwnd = win32gui.FindWindow(None, title)
    _, pid = win32process.GetWindowThreadProcessId(hwnd)

    return pid
