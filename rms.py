import numpy
from math import gcd


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
        for x in range(len(self.task)):
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
        p_order = self.priority_order(self.task)
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
    @staticmethod
    def priority_order(task):
        ordered_array = []
        for x in range(len(task)):
            copy_array = task
            temp = [copy_array[0]]
            for y in range(len(copy_array)):
                if temp[0][1] >= copy_array[y][1]:
                    temp = [copy_array[y]]
            ordered_array.append(temp[0])
            copy_array.remove(temp[0])
        return ordered_array

    # compare task priorities
    # lowest priority wins
    # create array of tasks in order
    # highest to lowest priority order
    @staticmethod
    def priority_order_task_name(task):
        ordered_array = []
        for x in range(len(task)):
            copy_array = task
            temp = [copy_array[0]]
            for y in range(len(copy_array)):
                if temp[0][1] >= copy_array[y][1]:
                    temp = [copy_array[y]]
            ordered_array.append(temp[0])
            copy_array.remove(temp[0])
        return ordered_array

    @staticmethod
    def lcm_rms(task):
        list_of_deadlines = []
        for x in range(len(task)):
            list_of_deadlines.append(int(task[x][2]))
        print(list_of_deadlines)
        lcm = list_of_deadlines[0]
        for i in list_of_deadlines[1:]:
            lcm = lcm * i // gcd(lcm, i)
        return lcm

    @staticmethod
    def rms_schedule(p_order, lcm):
        queue = []
        for x in range(len(p_order)):
            queue.append(int(p_order[x][0]))
        organized_array = []
        temp = 0
        queue_copy = queue.copy()
        queue_flag = 0

        # arrays made at this point

        for x in range(lcm+1):
            if x != 0:
                if temp == "":
                    organized_array.append(0)
                    queue_flag = 0
                else:
                    organized_array.append(p_order[temp])
                    queue_flag = 0
            for y in range(len(queue)):
                if x != 0 and x % int(p_order[y][2]) == 0:
                    queue_copy[y] += queue[y]
                if queue_flag == 0:
                    if queue_copy[y] > 0:
                        temp = y
                        queue_copy[y] -= 1
                        queue_flag = 1
                    else:
                        temp = ""
        print(organized_array)
        print(len(organized_array))
        t_array = []
        for x in range(len(organized_array)):
            for y in range(len(p_order)):
                if organized_array[x] == 0:
                    t_array.append(" ")
                    break
                elif organized_array[x] == p_order[y]:
                    t_array.append("T" + str(y + 1))
        print(t_array)
