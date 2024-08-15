class Node:
    """A Node in a singly linked list."""

    def __init__(self, data=None, next=None):
        self.data = data  # The value stored in the node
        self.next = next  # Pointer to the next node


class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def append(self, data):
        new_node = Node(data, None)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next
            last_node.next = new_node

    def get_len(self):
        count = 0
        cur_node = self.head
        while cur_node:
            cur_node = cur_node.next
            count = count + 1
        return count

    def insert_at(self, index, data):
        if index < 0 or index > self.get_len():
            raise Exception('invalid index')

        if index == 0:
            new_node = Node(data, self.head)
            self.head = new_node

        cur_node = self.head
        count = 0
        while count < index - 1:
            cur_node = cur_node.next
            count += 1
        new_node = Node(data, cur_node.next)
        cur_node.next = new_node

    def remove_at(self, index):
        if index == 0:
            self.head = self.head.next
            return

        count = 0
        cur_node = self.head
        while count < index - 1:
            count += 1
            cur_node = cur_node.next
        cur_node.next = cur_node.next.next

    def print_list(self):
        """Print the linked list."""
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")  # Indicate the end of the list


if __name__ == "__main__":
    ll = LinkedList()
    ll.prepend(1)
    ll.prepend(2)

    ll.print_list()
    ll.append(100)
    ll.print_list()

    ll.insert_at(1, 11)
    ll.print_list()

    ll.remove_at(0)
    ll.print_list()
