# PierrePictureCompare
Little Program used to compare images

#---#
This program is used to display 6 images and see the contents of the images

## How to run
1. `python main.py` inside a powershell window

### Prerequisites
- Python 2.7
- Pygame
- csv
- pandas
- tkinter


## #How it works
1. The program reads a csv file and takes the path (in coluumn one of csv file) and the file name (second column of the csv file)
2. Then displays the picture (if png of jpg) or invalid (if not valid picture format)

### Options
The main pygame window has four options by hitting a specific key:
- Down arrow --> Will read the next 6 lines from the csv
- Numbers 1-6 --> Will open the associated file in the window exsplorer
- Spacebar --> Pop a second window that will ask the user to enter in the next row they would like to read in from the csv file
- Escape --> Close and exit

### Bugs
-The tkinter window is very buggy and will not close properly, Once you have hit the "Show" button, you must then make sure the main pygame window is activated (by clicking in the window)
-Commands are know to stack up when in the tkinter window, so make sure the tkinter window is close and that the main window is selected

--> More info to come
