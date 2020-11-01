try:
    from .processes import get_windows_processes
    from .windows import get_all_windows
except ImportError:
    pass
