import tkinter
import numpy

# Input is task set
# Run utilization test
# If needed run exact analysis based on threshold
# If pass/fail notify user
# If pass then move on to scheduling
# RMS does scheduling based on priority via smallest period
# If task is available then override based on priority


class RMS:

    # Expected task format ci, pi, dl
    def __init__(self, task1, task2):
        self.task1 = task1
        self.task2 = task2

    # Utilization test will take ci/pi of each task
    # It will then add them all together
    # Then check if it is < n(2^1/n - 1)
    # Where n is # of tasks
    def utilization_test(self):
        util1 = float(self.task1[0]) / float(self.task1[1])
        util2 = float(self.task2[0]) / float(self.task2[1])
        util3 = util1 + util2
        # u_test = n(2^1/n - 1)
        if util3 <= 0.82:
            return True
        else:
            return False

    def exact_analysis(self):
        self.speed += 5

    # compare task priorities
    # lowest priority wins
    def priority_order(self):
        if self.task1 <= self.task2:
            return True
        else:
            return False

    # schedule task based on lowest priority
    # schedule up to LCM of the deadlines
    # Phase 1: print array of tasks in order
    # Phase final: prints excel style on GUI
    def rms_schedule(self):
        flag = self.priority_order()
        lcm = numpy.lcm(int(self.task1[1]), int(self.task2[1]))
        if flag is True:
            firstTask = lcm / self.task1[2]
        else:
            firstTask = lcm / self.task2[2]


# Input is task set
# Run utilization test
# If needed run exact analysis based on threshold
# If pass/fail notify user
# If pass then move on to scheduling
# EDF does scheduling based on earliest deadline first
# Ties will be given to task that is currently executing
# Otherwise task will be selected at random amongst tied


class EDF:

    def __init__(self, task1, task2):
        self.task1 = task1
        self.task2 = task2

    # Utilization test will take ci/pi of each task
    # It will then add them all together
    # Then check if it is <= 1
    # Where n is # of tasks
    # Necessary for EDF and sufficient
    def utilization_test(self):
        util1 = float(self.task1[0]) / float(self.task1[1])
        util2 = float(self.task2[0]) / float(self.task2[1])
        util3 = util1 + util2
        # u_test = n(2^1/n - 1)
        if util3 <= 1:
            return True
        else:
            return False

# Two entries, RMS and EDF
# Input is a task set
# Task set is run through each function
# output of each is generated via GUI using Tkinter


if __name__ == '__main__':

    while True:

        action = input("Please input 2 task sets in format \"Ci, Pi, Dl\", \"Ci, Pi, Dl\" ")
        if len(action) == 6:
            print(action)
        else:
            print("Invalid task set entered")
            break
        t1 = action[0:3]
        t2 = action[3:6]

        print(t1)
        print(t2)

        rms = RMS(t1, t2)
        edf = EDF(t1, t2)

        print(rms.utilization_test())
        print(rms.rms_schedule())

        # TKinter setup for GUI of scheduling

        #top = tkinter.Tk()
        #top.mainloop()