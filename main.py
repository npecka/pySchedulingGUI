import tkinter as tk
import numpy as np
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
                # break
            else:
                return task_sets

            #choice_case = choice.lower()


        def rms_scheduler():
            string = e.get()
            task_sets = scheduling_setup(string)
            #if choice_case == "rms" or choice_case == "both":
            print("This is rms")
            rms = RMS(task_sets)
            least_common_multiple = rms.lcm_rms(task_sets)
            priority_order = rms.priority_order(task_sets)
            flag = rms.exact_analysis()
            if flag is False:
                print("Unschedulable")
            else:
                rms_schedule = rms.rms_schedule(priority_order, least_common_multiple, task_sets)
                element = ''
                for i in range(len(rms_schedule)):
                    element = element + rms_schedule[i] + ' '
                label = tk.Label(root, text="This is RMS")
                label2 = tk.Label(root, text=element)
                label.pack()
                label2.pack()

        def edf_scheduler():
            string = e.get()
            task_sets = scheduling_setup(string)
            #if choice_case == "edf" or choice_case == "both":
            print("This is edf")
            edf = EDF(task_sets)
            l_c_m = edf.lcm_edf(task_sets)
            p_ord = edf.priority_order(task_sets)[0]
            flag = edf.utilization_test(task_sets)
            if flag is False:
                print("Unschedulable")
            else:
                edf_schedule = edf.edf_schedule(p_ord, l_c_m, task_sets)
                element = ''
                for i in range(len(edf_schedule)):
                    element = element + edf_schedule[i] + ' '
                label = tk.Label(root, text="This is EDF")
                label2 = tk.Label(root, text=element)
                label.pack()
                label2.pack()

        root = tk.Tk()
        root.title("RMS/EDF Scheduling\nPlease specify Ci Pi Di")

        e = tk.Entry(root)
        e.pack()
        e.focus_set()

        #b.pack(side='bottom')

        button = tk.Button(root, text="RMS", command=rms_scheduler)
        button2 = tk.Button(root, text="EDF", command=edf_scheduler)
        button.pack()
        button2.pack()

        root.mainloop()