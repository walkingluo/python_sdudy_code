# -*- coding:utf-8 -*-

class Node(object):
    '''
        Linked Node
    '''
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SinglyLinkedList:
    '''
        SinglyLinkedList
        head.value = None
    '''
    def __init__(self):
        self.head = Node()

    def __len__(self):
        curr = self.head
        count = 0
        while curr.next:
            count += 1
            curr = curr.next
        return count

    def __repr__(self) -> str:
        nodes = []
        curr = self.head
        while curr.next:
            curr = curr.next
            nodes.append(curr.value)
        return '->'.join(nodes)

    def __str__(self) -> str:
        nodes = []
        curr = self.head
        while curr.next:
            curr = curr.next
            nodes.append(str(curr.value))
        return '->'.join(nodes)
    
    def __iter__(self):
        curr = self.head
        while curr.next:
            curr = curr.next
            yield curr

    def add_node(self, value):
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(value)

    def add_head(self, value):
        curr = self.head
        node = Node(value)
        if curr.next:
            curr = curr.next
            node.next = curr
        self.head.next = node

    def delete(self, value):
        curr = self.head
        while curr.next:
            prev = curr
            curr = curr.next
            if curr.value == value:
                prev.next = curr.next


if __name__ == '__main__':
    linked_list = SinglyLinkedList()
    
    linked_list.add_node(1)
    linked_list.add_node(2)
    linked_list.add_node(3)
    linked_list.add_node(4)
    linked_list.add_node(5)
    linked_list.add_node(6)
    linked_list.add_node(7)

    linked_list.add_head(8)
    linked_list.add_head(9)

    linked_list.delete(3)
    linked_list.delete(9)
    linked_list.delete(7)
    
    print(len(linked_list))
    print(linked_list)

    for node in linked_list:
        print(node.value)
