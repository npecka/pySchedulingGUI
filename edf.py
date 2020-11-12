import numpy as np
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
    @staticmethod
    def utilization_test(task):
        u_task = 0
        task_copy = np.copy(task)
        task_row = task_copy.shape[0]
        for x in range(task_row):
            u_task = u_task + (float(task_copy[x][0]) / float(task_copy[x][1]))
        if u_task <= 1:
            return True
        else:
            return False

    # order on deadlines
    @staticmethod
    def priority_order(task):
        ordered_array = []
        ordered_index = []
        copy_array = np.copy(task)
        copy_index = []
        for x in range(len(copy_array)):
            copy_index.append(x)
        for x in range(len(task)):
            temp = np.copy(copy_array[0])
            index_temp = copy_index[0]
            for y in range(len(copy_array)):
                if temp[2] >= copy_array[y][2]:
                    temp = np.copy(copy_array[y])
                    index_temp = copy_index[y]
            ordered_array.append(temp)
            ordered_index.append(index_temp)
            test_r = np.where((copy_array == temp).all(axis=1))
            copy_array = np.delete(copy_array, test_r[0][0], 0)
            copy_index.remove(index_temp)
        order_array = np.array(ordered_array)
        return order_array, ordered_index

    # find least common multiple from deadlines of tasks
    @staticmethod
    def lcm_edf(task):
        list_of_deadlines = []
        for x in range(len(task)):
            list_of_deadlines.append(int(task[x][2]))
        lcm = list_of_deadlines[0]
        for i in list_of_deadlines[1:]:
            lcm = lcm * i // gcd(lcm, i)
        return lcm

    def edf_schedule(self, p_order, lcm, original_order):
        queue_order = np.copy(p_order)
        row = queue_order.shape[0]
        organized_array = []
        temp = 0
        queue_flag = 0
        swap_flag = 0
        # arrays made at this point

        for x in range(lcm + 1):
            if x != 0:
                if temp == "":
                    organized_array.append(0)
                    queue_flag = 0
                else:
                    organized_array.append(p_order[temp])
                    queue_flag = 0
                swap_flag = 0
            for y in range(row):
                if x != 0 and x % int(p_order[y][2]) == 0:
                    queue_order[y][2] += p_order[y][2]
                    queue_order[y][0] += p_order[y][0]
                    swap_flag = 1
            if swap_flag == 1:
                swap = self.priority_order(queue_order)
                queue_order = swap[0]
                p_order = p_order[swap[1]]
            for z in range(row):
                if queue_flag == 0:
                    if queue_order[z][0] > 0:
                        temp = z
                        queue_order[z][0] -= 1
                        queue_flag = 1
                    else:
                        temp = ""
        org_array = np.array(organized_array, dtype="object")
        t_array = []
        for x in range(len(org_array)):
            for y in range(len(p_order)):
                if np.array_equal(org_array[x], 0):
                    t_array.append(" ")
                    break
                elif np.array_equal(org_array[x], original_order[y]):
                    t_array.append("T" + str(y + 1))
        print(t_array)
        return t_array