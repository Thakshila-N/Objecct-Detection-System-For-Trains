import sys
from cx_Freeze import setup, Executable


setup(name="Simple",
      version="0.1",
      description="This software detects objects in realtime",
      executables=[Executable("main.py")]
      )


