Directions for using RMS/EDF GUI Scheduler

The input must be either a string of Ci Pi Di separated by spaces with no leading space at the end

The other option for input is a .xlsx file (Excel work book) where the contents of the file must be the same Ci Pi Di with spaces in between and no leading space at the end.

Also for the excel method, each task in the set must be in the same row and each task have its own column (ex. row 1, col 1 = [1 2 3] row 1, col 2 = [4 5 6] etc.)

The program iterates through the excel sheet row by row and attempts to schedule all task sets per row until it hits an empty row

Results for scheduled to excel sheet methods will appear in a file called updatedResults.xlsx which will be found in the working directory