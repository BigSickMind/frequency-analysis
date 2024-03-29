import sys

from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "build_exe": "frequency-analysis-exe",
    "packages": ["os", "tkinter", "statistics", "numpy", "scipy", "matplotlib", "wavio"],
    "excludes": ["scipy.spatial.cKDTree"],
    "includes": [
        "matplotlib.backends.backend_qt5agg",
        "matplotlib.dviread",
        "matplotlib.tight_bbox"
    ],
    "include_files": [
        # source
        "src/",
        # qt
        "venv/Lib/site-packages/PyQt5/Qt/bin/libEGL.dll",
        "venv/Lib/site-packages/PyQt5/Qt/plugins/platforms",
    ],
}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

exe = Executable(script='src/main.py', base=base, icon='src/main.ico', targetName='frequency-analysis.exe')

setup(name="frequency-analysis",
      version="1.0",
      description="",
      options={"build_exe": build_exe_options},
      executables=[exe])
