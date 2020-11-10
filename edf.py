import numpy
from math import gcd

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

    # Utilization test will take ci/pi of each task
    # It will then add them all together
    # Then check if it is <= 1
    # Where n is # of tasks
    # Necessary for EDF and sufficient
    def utilization_test(self):
        u_task = 0
        for x in range(len(self.task)):
            u_task = u_task + (float(self.task[x][0]) / float(self.task[x][1]))
        if u_task <= 1:
            return True
        else:
            return False

    # order on deadlines
    @staticmethod
    def priority_order(task):
        ordered_array = []
        for x in range(len(task)):
            copy_array = task
            temp = [copy_array[0]]
            for y in range(len(copy_array)):
                if temp[0][2] >= copy_array[y][2]:
                    temp = [copy_array[y]]
            ordered_array.append(temp[0])
            copy_array.remove(temp[0])
        return ordered_array

    # find least common multiple from deadlines of tasks
    @staticmethod
    def lcm_edf(task):
        list_of_deadlines = []
        for x in range(len(task)):
            list_of_deadlines.append(int(task[x][2]))
        print(list_of_deadlines)
        lcm = list_of_deadlines[0]
        for i in list_of_deadlines[1:]:
            lcm = lcm * i // gcd(lcm, i)
        return lcm

    def edf_schedule(self, p_order, lcm):
        queue = []
        d_queue = []
        for x in range(len(p_order)):
            queue.append(int(p_order[x][0]))
            d_queue.append(int(p_order[x][2]))
        organized_array = []
        temp = 0
        queue_copy = queue.copy()
        queue_flag = 0
        adjusted_order = p_order.copy()

        # arrays made at this point

        for x in range(lcm + 1):
            # self.priority_order(p_order)

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
                    adjusted_order[y] = adjusted_order[y][0] + adjusted_order[y][1] + \
                                        str(int(adjusted_order[y][2]) + int(adjusted_order[y][2]))
                    print(adjusted_order)
                    adjusted_order = self.priority_order(adjusted_order)
                    print(adjusted_order)

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