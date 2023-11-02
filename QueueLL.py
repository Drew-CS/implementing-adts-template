# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 3: Queue-LL
#
# NAME:         FIXME
# ASSIGNMENT:   Project 5: Implementing ADTs

from Node import Node

class QueueLL(object):
    def __init__(self, list=None):
        self.front = None
        self.tail = None
        if list is not None:
            for item in list:
                self.enq(item)

    def get_front(self):
        # FIXME
        return

    def get_tail(self):
        # FIXME
        return

    def deq(self):
        # FIXME
        return

    def enq(self, data=None):
        # FIXME
        return

    def print(self):
        n = self.front
        while n is not None:
            print(n.get_data(), "=>", end=" ")
            n = n.get_next()
        print("NULL")

    def is_empty(self):
        # FIXME
        return

    def clear(self):
        # FIXME
        return


def main():
    ql = QueueLL()
    ql.print()
    print("Is empty?", ql.is_empty())
    for i in range(1, 7):
        ql.enq(i)
    ql.print()
    print("Front:   ", ql.get_front())
    print("Deq:     ", ql.deq())
    ql.print()
    print("Is empty?", ql.is_empty())

# Don't run main on import
if __name__ == "__main__":
    main()

