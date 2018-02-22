# PERTgen
Python code to generate a PERT graph and Gantt chart given a task schedule.

## Requirements
This project uses python3, and the following libraries must be installed to run it:
* [NetworkX](https://networkx.github.io/) - Used to make the PERT graph.
* [Matplotlib](https://matplotlib.org/) - Used to make the Gantt chart, as well as show and save both the PERT graph and Gantt chart.

## Data input
The task data must be given in a CSV file, in the format of the sample ones given (```tasks.csv``` and ```tasks2.csv```),
i.e. each row starting from the second one should have a task, its duration and all its dependencies seperated by spaces

## Test it
The project can be tested with the simple tkinter GUI by running ```gui.py``` with the python3 interpreter, although all the important code is in ```pert.py``` which can also be run after specifying which file is to be loaded.
