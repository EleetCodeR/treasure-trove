# Completely Fair Scheduler in Linux
import sys
import random
global curr_pID
curr_pID = 0
# data structure that represents a node in the tree


class Node():
    def __init__(self, data, pid=0):
        global curr_pID
        self.data = data  # holds the key (here-execution time of process)
        self.parent = None  # pointer to the parent
        self.left = None  # pointer to left child
        self.right = None  # pointer to right child
        self.color = 1  # 1 . Red, 0 . Black
        if(pid != 0):
            pass
        else:
            self.pID = curr_pID + 1  # assigning process id.
            curr_pID = self.pID
# class RedBlackTree implements the operations in Red Black Tree


class RedBlackTree():
    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL

    # fix the rb tree modified by the delete operation

    def __fix_delete(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 1:
                    # case 3.1
                    s.color = 0
                    x.parent.color = 1
                    self.left_rotate(x.parent)
                    s = x.parent.right

                if s.left.color == 0 and s.right.color == 0:
                    # case 3.2
                    s.color = 1
                    x = x.parent
                else:
                    if s.right.color == 0:
                        # case 3.3
                        s.left.color = 0
                        s.color = 1
                        self.right_rotate(s)
                        s = x.parent.right

                    # case 3.4
                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 1:
                    # case 3.1
                    s.color = 0
                    x.parent.color = 1
                    self.right_rotate(x.parent)
                    s = x.parent.left

                if s.right.color == 0 and s.right.color == 0:
                    # case 3.2
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:
                        # case 3.3
                        s.right.color = 0
                        s.color = 1
                        self.left_rotate(s)
                        s = x.parent.left

                    # case 3.4
                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 0

    def __rb_transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def __delete_node_helper(self, node, key):
        # find the node containing key
        z = self.TNULL
        while node != self.TNULL:
            if node.data == key:
                z = node

            if node.data <= key:
                node = node.right
            else:
                node = node.left

        if z == self.TNULL:
            print("Couldn't find key in the tree")
            return

        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            self.__rb_transplant(z, z.right)
        elif (z.right == self.TNULL):
            x = z.left
            self.__rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.__rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.__rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 0:
            self.__fix_delete(x)

    # fix the red-black tree
    def __fix_insert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left  # uncle
                if u.color == 1:
                    # case 3.1
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        # case 3.2.2
                        k = k.parent
                        self.right_rotate(k)
                    # case 3.2.1
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right  # uncle

                if u.color == 1:
                    # mirror case 3.1
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        # mirror case 3.2.2
                        k = k.parent
                        self.left_rotate(k)
                    # mirror case 3.2.1
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0

    def __print_helper(self, node, indent, last):
        # print the tree structure on the screen
        if node != self.TNULL:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print(str(node.data) + "(" + s_color + ","+"%d" % node.pID + ")")
            self.__print_helper(node.left, indent, False)
            self.__print_helper(node.right, indent, True)

    # find the node with the minimum key

    def minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node

    # find the node with the maximum key
    def maximum(self, node):
        while node.right != self.TNULL:
            node = node.right
        return node

    # rotate left at node x
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # rotate right at node x
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    # insert the key to the tree in its appropriate position
    # and fix the tree
    def insert(self, key, pid=0):
        # Ordinary Binary Search Insertion
        node = Node(key)
        node.parent = None
        node.data = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1  # new node must be red
        if(pid != 0):
            node.pID = pid

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        # y is parent of x
        node.parent = y
        if y == None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        # if new node is a root node, simply return
        if node.parent == None:
            node.color = 0
            return

        # if the grandparent is None, simply return
        if node.parent.parent == None:
            return

        # Fix the tree
        self.__fix_insert(node)

    # delete the node from the tree

    def delete_node(self, data):
        self.__delete_node_helper(self.root, data)

    # print the tree structure on the screen
    def pretty_print(self):
        self.__print_helper(self.root, "", True)

    def cfscheduler(self, max_exectime):

        # Select leftmost
        leftmost_node = self.minimum(self.root)

        # Execution of Process:
        print("PID:%d -- Process is in running state..." % leftmost_node.pID)
        # When Completes Execution remove from schedule tree
        if(leftmost_node.data <= max_exectime):
            print("PID:%d -- Process completed execution." % leftmost_node.pID)
            self.delete_node(leftmost_node.data)
            self.pretty_print()
            return
        else:
            # When reaches max execution time, re-insert the node with difference in exec.time (keep PID same)
            pid = leftmost_node.pID
            new_exectime = leftmost_node.data-max_exectime
            print("PID:%d -- Process moved back to NEW state; Remaining Processor Time :%d" %
                  (leftmost_node.pID, new_exectime))
            self.delete_node(leftmost_node.data)
            self.insert(new_exectime, pid)

        # When reaches max execution time, re-insert the node with difference in exec.time (keep PID same)

        # elif(leftmost_node.data < exec_const):
        #     pid = leftmost_node.pID

        #     # calculte new remaining execution time after reaching max.exec time on processor.

        #     new_exectime = abs(exec_const - leftmost_node.data)
        #     # new_exectime = exec_const - leftmost_node.data
        #     if(leftmost_node.data < new_exectime):
        #         if(leftmost_node.data - 2 <= 0):
        #             # new_exectime = 0
        #             print("PID:%d -- Process completed execution." %
        #                   leftmost_node.pID)
        #             self.delete_node(leftmost_node.data)
        #             return
        #         else:
        #             # non zero / non negative exec.time
        #             new_exectime = leftmost_node.data - 2

        #     print("PID:%d -- Process moved back to NEW state; Remaining Processor Time :%d" %
        #           (leftmost_node.pID, new_exectime))

            self.pretty_print()
            return


bst = RedBlackTree()
print(" ==============[ Creating Schedule Tree ]=============== \n")
# Create a Schedule Tree
bst.insert(8)
bst.insert(18)
bst.insert(5)
bst.insert(15)
bst.insert(17)
bst.insert(25)
bst.insert(40)
bst.insert(80)
print("The Schedule Tree is as follows:\n")
bst.pretty_print()
print("\nInvoking C.F.Scheduler...")
# Hypothetical Processor:
min_exec = (bst.minimum(bst.root)).data
max_exec = (bst.maximum(bst.root)).data
# exec_const = random.randint(min_exec, max_exec)
max_exectime = int(max_exec/min_exec)
bst.cfscheduler(max_exectime)
bst.cfscheduler(max_exectime)
bst.cfscheduler(max_exectime)
bst.cfscheduler(max_exectime)
bst.cfscheduler(max_exectime)
bst.cfscheduler(max_exectime)
bst.cfscheduler(max_exectime)
bst.cfscheduler(max_exectime)
bst.cfscheduler(max_exectime)
