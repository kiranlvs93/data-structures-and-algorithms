class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data=data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_beginning(data)
        else:
            curr_ele = self.head
            while curr_ele.next is not None:
                curr_ele = curr_ele.next
            curr_ele.next = Node(data=data)

    def insert_at_index(self, index, data):
        if index < 0:
            raise ValueError("Negative indices aren't allowed. Please insert at index >=0")
        if index == 0:
            self.insert_at_beginning(data)
        else:
            curr_index = 0
            curr_ele = self.head
            while curr_index != (index - 1):
                if curr_ele is None:
                    raise IndexError("Index out of bounds")
                curr_ele = curr_ele.next
                curr_index += 1

            # At (index -1), insert the new node
            next_ele = curr_ele.next
            curr_ele.next = Node(data=data, next_node=next_ele)

    def delete_by_value(self, value):
        prev_ele = None
        curr_ele = self.head

        while curr_ele is not None:
            if curr_ele.data == value:
                if prev_ele is None:
                    self.head = curr_ele.next
                else:
                    # Skipping over current node
                    prev_ele.next = curr_ele.next
                return True  # Exit after first match
            prev_ele = curr_ele
            curr_ele = curr_ele.next

    def delete_by_index(self, index):
        curr_ele = self.head

        if index == 0:
            if curr_ele is not None:
                self.head = curr_ele.next
                return True  # Remove the head
            return False  # List is empty

        prev_ele = None
        curr_index = 0

        while curr_ele is not None:
            if curr_index == index:
                # Skipping over current node
                prev_ele.next = curr_ele.next
                return True  # Exit after first match

            prev_ele = curr_ele
            curr_ele = curr_ele.next
            curr_index += 1
        raise IndexError("Index out of bounds")

    def search(self, data):
        curr_ele = self.head
        index = 0
        while curr_ele is not None:
            if curr_ele.data == data:
                return index
            curr_ele = curr_ele.next
            index += 1
        return -1

    def __str__(self):
        if self.head is None:
            return "[]"
        curr_ele: Node = self.head
        linked_list = []

        while curr_ele is not None:
            linked_list.append(str(curr_ele.data))
            curr_ele = curr_ele.next

        return " -> ".join(linked_list)


my_ll = LinkedList()

# Insert at beginning
# my_ll = LinkedList()
# my_ll.insert_at_beginning(3)
# my_ll.insert_at_beginning(2)
# my_ll.insert_at_beginning(1)
# print(my_ll)

# Insert at end
# my_ll.insert_at_end(1)
# my_ll.insert_at_end(2)
# my_ll.insert_at_end(3)
# print(my_ll)

# Insert at index
# my_ll.insert_at_beginning(1)
# my_ll.insert_at_end(3)
# my_ll.insert_at_index(1, 2)
# my_ll.insert_at_end(5)
# my_ll.insert_at_index(3, 4)
# print(my_ll)
# print(my_ll.search(3))
# print(my_ll.search(6))

# # delete_by_value
# my_ll.insert_at_end(1)
# my_ll.insert_at_end(2)
# my_ll.insert_at_end(3)
# print(my_ll)
# my_ll.delete_by_value(2)
# print(my_ll)
# my_ll.delete_by_value(3)
# print(my_ll)

# delete_by_index
my_ll.insert_at_end(1)
my_ll.insert_at_end(2)
my_ll.insert_at_end(3)
print(my_ll)
my_ll.delete_by_index(2)
my_ll.insert_at_beginning(5)
print(my_ll)
my_ll.delete_by_index(0)
print(my_ll)
my_ll.delete_by_index(5)
print(my_ll)
