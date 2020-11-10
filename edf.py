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