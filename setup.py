import cx_Freeze
import sys
import os
os.environ["TCL_LIBRARY"] = "C:/Users/JIT/AppData/Local/Programs/Python/Python37/tcl/tcl8.6"
os.environ["TK_LIBRARY"] = "C:/Users/JIT/AppData/Local/Programs/Python/Python37/tcl/tk8.6"

base = None

if sys.platform =="win32":
    base = "Win32GUI"

executables = [cx_Freeze.Executable("Courtcase_Calculator.py", base=base, icon="LogoMakr_0YT8k4.ico")]

cx_Freeze.setup(
    name = "Court Case Calculator",
    options = {"build_exe": {"packages":["tkinter","matplotlib","tkcalendar", "os", "datetime", "babel", "xlrd"],
                             "include_files":["my_project", "test.xlsx", "icon.ico", "biswa-bangla.png"]}},
    version = "1",
    description = "Calculate Interest on court cases",
    executables = executables)
