import random
from Tree import Tree
import sys

LIST_LENGTH = 20


def main():
    """
    Main function to create and manipulate an AVL Tree.
    """
    # Create a seed
    seed_value = random.randrange(sys.maxsize)
    print('Seed value:', seed_value)
    print()
    random.seed(seed_value)

    # Create the initial list to put in the tree
    initList = [random.randint(1, 100) for _ in range(LIST_LENGTH)]
    print("Initial elements:")
    print(initList)

    # Create tree with initial list
    t = Tree(initList)
    print()
    print("Step #1.")
    print('Initial AVL tree after inserting the above list and rebalancing:')
    print(t)

    # Insert 3 random numbers into the tree (between 20 and 100)
    list_inserted = []
    print("Step #2.")
    for _ in range(3):
        random_var = random.randint(20, 100)
        list_inserted.append(random_var)
        t.insert(random_var)

    # Print the updated tree
    converted_list = [str(element) for element in list_inserted]
    print(
        f'AVL Tree after attempting to insert {", ".join(converted_list)} and rebalancing:')
    print(t)

    # Deleting Nodes
    list_removed = []
    all_variables = t.make_list(t.root)
    random.shuffle(all_variables)

    for _ in range(3):
        random_var = all_variables[_]
        list_removed.append(random_var)
        t.delete(random_var)

    # Print the updated tree
    converted_list = [str(element) for element in list_removed]
    print("Step #3.")
    print(
        f'AVL Tree after removing {", ".join(converted_list)} and rebalancing:')
    print(t)


class Logger(object):
    """
    Logger class for capturing the output of the program and storing it in a log file.
    """

    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("../logs/logfile.log", "a")

    def write(self, message):
        """
        Write a message to both the terminal and the log file.
        """
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        """
        Flush method for python 3 compatibility. Handles the flush command by doing nothing.
        You might want to specify some extra behavior here.
        """
        pass


sys.stdout = Logger()

if __name__ == "__main__":
    main()
