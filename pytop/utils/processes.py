import psutil


def get_size(bytes):
    """ Get size of bytes in a nice format.

    This method will parse a byte ammount and convert it to its greatest unit.

    :param bytes: the bytes used by the process.
    :return: a string of the formatted bytes.
    """
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"

        bytes /= 1024


def get_windows_processes(windows):
    """ Create a detailed list of all the active processes.

    This data will then be used by the ``App`` class, in order to create a
    dynamic GUI list with CPU/RAM/disk/uptime info.

    :param windows: the active windows.
    :return: a list containing tuples with processes info.
    """
    pids = [window["pid"] for window in windows]
    processes = []

    for process in psutil.process_iter():
        with process.oneshot():
            if process.pid in pids:
                pid = process.pid
                name = process.name()
                status = process.status()
                cpu_percent = process.cpu_percent()

                try:
                    memory_usage = get_size(process.memory_full_info().uss)
                except PermissionError:
                    memory_usage = "0MB"

                threads = process.num_threads()

                processes.append((
                    pid,
                    name,
                    status,
                    cpu_percent,
                    memory_usage,
                    threads
                ))

    return processes
