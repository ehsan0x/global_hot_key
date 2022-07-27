from cx_Freeze import setup, Executable

base = None

executables = [Executable("global_hotkey.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {
        'packages': ["idna", "os", "datetime", "mss",
                     "datetime", "pynput", "pynput.keyboard"],
    },
}

setup(
    name="Global Hotkey",
    options=options,
    version="0.1",
    description='System-wide access to user defined keyboard hotkey combinations.',
    executables=executables
)