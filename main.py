import tkinter
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

        action = input("Please input at least 2 task sets in format Ci Pi Dl, Ci Pi Dl ")
        replace = action.replace(",", "")
        task = replace.split(" ")
        task_convert = np.array(task)
        tasks = task_convert.astype(int)
        n = int(len(task) / 3)
        m = 3
        task_sets = tasks.reshape(n, m)

        if len(tasks) < 6:
            print("Invalid task set entered")
            break

        rms = RMS(task_sets)
        least_common_multiple = rms.lcm_rms(task_sets)
        # print(least_common_multiple)
        priority_order = rms.priority_order(task_sets)
        # print(priority_order)
        flag = rms.exact_analysis()

        if flag is False:
            print("Unschedulable")
        else:
            rms.rms_schedule(priority_order, least_common_multiple)

        #edf = EDF(task_sets)
        #l_c_m = edf.lcm_edf(task_sets)
        #p_ord = edf.priority_order(task_sets)
        #print(p_ord)
        #print(len(p_ord))
        #flag = edf.utilization_test()

        #if flag is False:
        #    print("Unschedulable")
        #else:
        #    edf.edf_schedule(p_ord, l_c_m)

        # TKinter setup for GUI of scheduling

        # top = tkinter.Tk()
        # top.mainloop()
