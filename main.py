import tkinter
import numpy
from math import gcd


# Input is task set
# Run utilization test
# If needed run exact analysis based on threshold
# If pass/fail notify user
# If pass then move on to scheduling
# RMS does scheduling based on priority via smallest period
# If task is available then override based on priority


class RMS:

    # Expected task format ci, pi, dl
    def __init__(self, task):
        self.task = task

    # Utilization test will take ci/pi of each task
    # It will then add them all together
    # Then check if it is < n(2^1/n - 1)
    # Where n is # of tasks
    def utilization_test(self):
        u_task = 0
        for x in range(len(task_sets)):
            u_task = u_task + (float(self.task[x][0]) / float(self.task[x][1]))
        u_test = len(self.task) * (pow(2, 1 / len(self.task)) - 1)
        if u_task <= u_test:
            return True
        else:
            return False

    # exact analysis
    # Get task priority
    # iterate through priorities
    # add all as iterating
    # for each iteration take # of tasks get total Ci
    # check if each task is below that deadline
    # if not then if it's not the last task, times 2 and check again
    # continue doing so until deadlines qualify or until failure
    def exact_analysis(self):
        p_order = self.priority_order()
        print(p_order)
        total_ci = 0
        flag = True
        for x in range(len(p_order)):
            total_ci = total_ci + int(p_order[x][0])
            total_ci_tmp = total_ci
            p_order_tmp = p_order
            i = 0
            while i < x:
                if int(p_order_tmp[x][2]) < total_ci_tmp:
                    flag = False
                    break
                elif int(p_order_tmp[i][2]) < total_ci_tmp:
                    total_ci_tmp = total_ci_tmp + int(p_order_tmp[i][0])
                    p_order_tmp[i] = str(int(p_order_tmp[i][0]) + int(p_order_tmp[i][0])) + \
                                     str(int(p_order_tmp[i][1]) + int(p_order_tmp[i][1])) + \
                                     str(int(p_order_tmp[i][2]) + int(p_order_tmp[i][2]))
                    i = 0
                else:
                    i += 1
        return flag

    # compare task priorities
    # lowest priority wins
    # create array of tasks in order
    # highest to lowest priority order
    def priority_order(self):
        ordered_array = []
        for x in range(len(self.task)):
            copy_array = self.task
            temp = [copy_array[0]]
            for y in range(len(copy_array)):
                if temp[0][1] >= copy_array[y][1]:
                    temp = [copy_array[y]]
            ordered_array.append(temp[0])
            copy_array.remove(temp[0])
        return ordered_array

    def lcm_rms(self):
        list_of_deadlines = []
        for x in range(len(self.task)):
            list_of_deadlines.append(int(self.task[x][2]))
        lcm = list_of_deadlines[0]
        for i in list_of_deadlines[1:]:
            lcm = lcm * i // gcd(lcm, i)
        return lcm

    # schedule task based on lowest priority
    # schedule up to LCM of the deadlines
    # Phase 1: print array of tasks in order
    # Phase final: prints excel style on GUI
    def rms_schedule(self):
        flag = self.exact_analysis()
        if flag is False:
            print("Unschedulable")
            return

        p_order = self.priority_order()
        lcm = self.lcm_rms()

        # TODO

        array = []
        if flag is True:
            first_task = numpy.floor(lcm / int(self.task1[2]))
            second_task = numpy.floor(lcm / int(self.task2[2]))
            amount_to_be_scheduled = int(first_task) + int(second_task)
            for x in range(amount_to_be_scheduled):
                if flag is True:
                    array.append("T1")
                    flag = False
                else:
                    array.append("T2")
                    flag = True
            print(array)
        else:
            first_task = numpy.floor(lcm / int(self.task2[2]))


# Input is task set
# Run utilization test
# If needed run exact analysis based on threshold
# If pass/fail notify user
# If pass then move on to scheduling
# EDF does scheduling based on earliest deadline first
# Ties will be given to task that is currently executing
# Otherwise task will be selected at random amongst tied


class EDF:

    def __init__(self, task):
        self.task = task
        print(task)

    # Utilization test will take ci/pi of each task
    # It will then add them all together
    # Then check if it is <= 1
    # Where n is # of tasks
    # Necessary for EDF and sufficient
    def utilization_test(self):
        util1 = float(self.task[0]) / float(self.task[1])
        # util2 = float(self.task2[0]) / float(self.task2[1])
        # util3 = util1 + util2
        # u_test = n(2^1/n - 1)
        # if util3 <= 1:
        #    return True
        # else:
        #    return False


# Two entries, RMS and EDF
# Input is a task set
# Task set is run through each function
# output of each is generated via GUI using Tkinter


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
        # edf = EDF(task_sets)

        # print(rms.utilization_test())
        # rms.priority_order()
        # rms.lcm_rms()
        print(rms.exact_analysis())
        # print(rms.rms_schedule())

        # TKinter setup for GUI of scheduling

        # top = tkinter.Tk()
        # top.mainloop()
