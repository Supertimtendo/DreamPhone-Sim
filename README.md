# DreamPhone-Sim
Open Dream Dialer is a project to recreate the 1992 board game Dreamphone in a computer software simulation.

# Installation
DreamPhone-Sim was built to work in Windows 10, but it should work in any Python 3.X compatible OS. 

##Dependencies
Using Windows 10/11:
If you do not have Python installed, get it from here: https://www.python.org/downloads/windows/
When installing, make sure Python is added to system PATH. There is a checkbox to tick in the installer to do this. 

More information on adding Python to PATH can be found here: https://datatofish.com/add-python-to-windows-path/

Open Dream Dialer requires two Python extensions to work, Colorama and Prettytable.

Once Python is installed, added to path and your system has been rebooted, open the command line (Win + R, "cmd", Enter) and type the following commands:

```pip install colorama```

This will install the Colorama extension.

```python -m pip install -U prettytable```

This will install the Prettytable extension.

##Downloading DreamPhone-Sim
If you have Git installed (https://git-scm.com/downloads), simply open the command line (Win + R, "cmd", Enter) and type:

```git clone DreamPhone-Sim```

If you don't have Git, you can simply click on the main.py, right-click its "Raw" tab on the right side of the page, and "save link as".
From that dialog box, you can save the "main.py" somewhere on your PC. This method might break if future builds add additional file dependencies, so fall back to the "Git clone" method if this does not work.

##Running DreamPhone-Sim
The "cleanest" way to run DreamPhone-Sim is from the Windows Command Line. If Python is configured correctly, you can open a command line  (Win + R, "cmd", Enter), navigate to where DreamPhone-Sim is downloaded, and run 

'''Python main.py'''

I've included "Launch DreamPhone-Sim in Windows.bat" as a quick shortcut you can download and run without entering the command line manually. It is assumed to be placed in the same directory as "main.py" to operate correctly (Git Clone will do this automatically). 

If you wish to have Windows use Python to run .py scripts directly:
Navigate to where you cloned/downloaded DreamPhone-Sim, and select "main.py", then right-click and "open with" - "choose another app" - "more apps" - scroll down and click "look for another app on this PC". Then navigate and select your installed Python executable
(default is C:\Users\(your user name)\AppData\Local\Programs\Python\Pythonxx\python.exe).
