#Given a linked list we have to reverse it.
#For this we would have to implement a linked list from scratch first, so we will import our Implementation.py file
#And use the LinkedList and Node classes defined there so that we don't have to create a Linked List from scratch

from Implementation import LinkedList, Node

#Now we create a Linked List by appending some values
my_linked_list = LinkedList()
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.print_list()
#2 3 4 5 6

#Time complexity pretty clearly will be O(n)
def reverse(linked_list):
    if linked_list.length <=1:
        return linked_list
    else:
        first = linked_list.head
        second = first.next
        linked_list.tail = linked_list.head
        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp
        linked_list.head.next = None
        linked_list.head = first
        return linked_list

reversed_linked_list = reverse(my_linked_list)
reversed_linked_list.print_list()
#6 5 4 3 2
