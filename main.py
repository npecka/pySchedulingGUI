import tkinter as tk
import numpy as np
import openpyxl
from openpyxl.styles import Alignment
from rms import RMS
from edf import EDF

# Two entries, RMS and EDF
# Input is a task set
# Task set is run through each function
# output of each is generated via GUI using Tkinter


# schedule task based on lowest priority
# schedule up to LCM of the deadlines
# Phase 1: print array of tasks in order
# Phase final: prints excel style on GUI


if __name__ == '__main__':

    while True:
        # TKinter setup for GUI of scheduling
        global e

        # action = input("Please input at least 2 task sets in format Ci Pi Dl, Ci Pi Dl ")
        # choice = input("Please input if you would like rms, edf, or both by typing 'rms' 'edf' or 'both' ")
        def scheduling_setup(string):
            replace = string.replace(",", "")
            task = replace.split(" ")
            task_convert = np.array(task)
            tasks = task_convert.astype(int)
            n = int(len(task) / 3)
            m = 3
            task_sets = tasks.reshape(n, m)

            if len(tasks) < 6:
                print("Invalid task set entered")
                label = tk.Label(root, text="The task set can not be scheduled")
                label.pack()
            else:
                return task_sets

            #choice_case = choice.lower()


        def rms_scheduler(string):
            if string == '':
                string_input = e.get()
                task_sets = scheduling_setup(string_input)
            else:
                task_sets = scheduling_setup(string)
            print("This is rms")
            rms = RMS(task_sets)
            least_common_multiple = rms.lcm_rms(task_sets)
            priority_order = rms.priority_order(task_sets)
            flag = rms.exact_analysis()
            if flag is False:
                label = tk.Label(root, text="The task set can not be scheduled for RMS")
                label.pack()
            else:
                rms_schedule = rms.rms_schedule(priority_order, least_common_multiple, task_sets)
                element = ''
                for i in range(len(rms_schedule)):
                    element = element + rms_schedule[i] + ' '
                label = tk.Label(root, text="This is RMS")
                label2 = tk.Label(root, text=element)
                label.pack()
                label2.pack()
                return rms_schedule

        def edf_scheduler(string):
            if string == '':
                string_input = e.get()
                task_sets = scheduling_setup(string_input)
            else:
                task_sets = scheduling_setup(string)
            print("This is edf")
            edf = EDF(task_sets)
            l_c_m = edf.lcm_edf(task_sets)
            p_ord = edf.priority_order(task_sets)[0]
            flag = edf.utilization_test(task_sets)
            if flag is False:
                label = tk.Label(root, text="The task set can not be scheduled for EDF")
                label.pack()
            else:
                edf_schedule = edf.edf_schedule(p_ord, l_c_m, task_sets)
                element = ''
                for i in range(len(edf_schedule)):
                    element = element + edf_schedule[i] + ' '
                label = tk.Label(root, text="This is EDF")
                label2 = tk.Label(root, text=element)
                label.pack()
                label2.pack()
                return edf_schedule

        def print_scheduler_rms(string, iteration, number_of_tasks):
            wb = openpyxl.load_workbook('updatedResults.xlsx')
            sheet = wb['results']
            arr = rms_scheduler(string)

            for i in range(len(arr)):
                for j in range(number_of_tasks):
                    string_check = 'T' + str(j + 1)
                    if arr[i] == ' ':
                        my_cell = sheet.cell(row=(number_of_tasks + 1 + iteration), column=(i + 1))
                        my_cell.value = i
                        my_cell.alignment = Alignment(horizontal='right')
                        break
                    if arr[i] == string_check:
                        my_cell = sheet.cell(row=(j + 1 + iteration), column=(i + 2))
                        my_cell.value = arr[i]
                        my_cell.alignment = Alignment(horizontal='center')
                        my_cell = sheet.cell(row=(number_of_tasks + 1 + iteration), column=(i+1))
                        my_cell.value = i
                        my_cell.alignment = Alignment(horizontal='right')
            my_cell = sheet.cell(row=(number_of_tasks + 1 + iteration), column=(len(arr) + 1))
            my_cell.value = len(arr)
            my_cell.alignment = Alignment(horizontal='right')
            wb.save('updatedResults.xlsx')
            point_in_sheet = number_of_tasks + 2
            return point_in_sheet


        def print_scheduler_edf(string):
            wb = openpyxl.load_workbook('results.xlsx')
            sheet = wb['results']
            arr = edf_scheduler(string)
            number_of_tasks = int(len(arr) / 3)

            for i in range(len(arr)):
                for j in range(number_of_tasks):
                    string_check = 'T' + str(j + 1)
                    if arr[i] == string_check:
                        my_cell = sheet.cell(row=(j + 1), column=(i + 2))
                        my_cell.value = arr[i]
                        my_cell.alignment = Alignment(horizontal='center')
                        my_cell = sheet.cell(row=(number_of_tasks + 1), column=(i + 1))
                        my_cell.value = i
                        my_cell.alignment = Alignment(horizontal='right')
            my_cell = sheet.cell(row=(number_of_tasks + 1), column=(len(arr) + 1))
            my_cell.value = len(arr)
            my_cell.alignment = Alignment(horizontal='right')
            wb.save('updatedResults.xlsx')

        def file_schedule_setup():
            string = e.get()
            wb = openpyxl.load_workbook(string)
            sheet = wb['results']
            rows = sheet.max_row
            cols = sheet.max_column
            iterator = 0
            for i in range(rows):
                task_string = ""
                task_count = 0
                for j in range(cols):
                    if sheet.cell(row=i+1, column=j+1).value is None:
                        break
                    my_cell = sheet.cell(row=i + 1, column=j + 1)
                    task_string = task_string + my_cell.value
                    if sheet.cell(row=i + 1, column=j + 2).value is not None:
                        task_string = task_string + ', '
                    task_count += 1
                iterator += print_scheduler_rms(task_string, iterator, task_count)
            # wb.save('updatedResults.xlsx')


        root = tk.Tk()
        root.title("RMS/EDF Scheduling           Please specify Ci Pi Di, Ci Pi Di")
        root.geometry("500x300")

        e = tk.Entry(root)
        e.place(relx = 0.5,
                rely = 0.5,
                anchor = "center")
        e.focus_set()

        button = tk.Button(root, text="RMS\nPreview", command=rms_scheduler)
        button.config(width=10)
        button.config(height=3)
        button.place(relx = 0.0,
                     rely = 1.0,
                     anchor = 'sw')
        button2 = tk.Button(root, text="EDF\nPreview", command=edf_scheduler)
        button2.config(width=10)
        button2.config(height=3)
        button2.place(relx=1.0,
                     rely=1.0,
                     anchor='se')
        button3 = tk.Button(root, text="RMS to Excel", command=print_scheduler_rms)
        button3.config(width=10)
        button3.config(height=3)
        button3.place(relx=0.3,
                      rely=1.0,
                      anchor='s')
        button4 = tk.Button(root, text="EDF to Excel", command=print_scheduler_edf)
        button4.config(width=10)
        button4.config(height=3)
        button4.place(relx=0.7,
                      rely=1.0,
                      anchor='s')
        button5 = tk.Button(root, text="Convert list\nfrom file", command=file_schedule_setup)
        button5.config(width=10)
        button5.config(height=3)
        button5.place(relx=0.5,
                      rely=1.0,
                      anchor='s')

        root.mainloop()
