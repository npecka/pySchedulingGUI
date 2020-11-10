import tkinter
from rms import RMS
import edf

# Two entries, RMS and EDF
# Input is a task set
# Task set is run through each function
# output of each is generated via GUI using Tkinter

# schedule task based on lowest priority
# schedule up to LCM of the deadlines
# Phase 1: print array of tasks in order
# Phase final: prints excel style on GUI
def rms_schedule(p_order, lcm):
    queue = []
    for x in range(len(p_order)):
        queue.append(int(p_order[x][0]))
    organized_array = []
    temp = 0
    queue_copy = queue.copy()
    for x in range(lcm):
        organized_array.append(p_order[temp])
        for y in range(len(queue)):
            if x != 0 and x % int(p_order[y][2]) == 0:
                queue_copy[y] += queue[y]
                temp = y
                queue_copy[y] -= 1
                break
            elif queue_copy[y] > 0:
                queue_copy[y] -= 1
                if queue_copy[y] != 0:
                    temp = y
                    break
    print(organized_array)


if __name__ == '__main__':

    while True:

        action = input("Please input at least 2 task sets in format Ci Pi Dl, Ci Pi Dl ")
        replace = action.replace(" ", "")
        task_sets = replace.split(",")

        if len(task_sets) >= 2:
            print(task_sets)
        else:
            print("Invalid task set entered")
            break

        rms = RMS(task_sets)
        least_common_multiple = rms.lcm_rms(task_sets)
        priority_order = rms.priority_order(task_sets)
        flag = rms.exact_analysis()

        if flag is False:
            print("Unschedulable")
        else:
            rms_schedule(priority_order, least_common_multiple)

        # edf = EDF(task_sets)

        #for x in range(len(order)):
        #    if order[x] == task_sets[x]:
        #        print("T1")
        # rms.lcm_rms()
        #print(rms.exact_analysis())
        # print(rms.rms_schedule())

        # TKinter setup for GUI of scheduling

        # top = tkinter.Tk()
        # top.mainloop()
