

class Node:
    def __init__(self, value = 0, next= None):
        self.value = value
        self.next = next
first = Node(1)
second = Node(2)
third = Node(3)
first.next = second
second.next = third
first.value = 6


class LinkedList(object):
    def __init__(self):
        self.head = None
    def append(self, value):
        new_node = Node(value) #새로운 노드 생성
        if self.head is None:
            self.head = new_node
            # 맨 뒤의 노드가 new_node를 가리켜야 한다.
        else:
            current = self.head
            while(current.next):
                current = current.next
            current.next = new_node
            
    def get(self, idx):
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value
    
    def insert(self, idx, value):
        new_node = Node(value)
        new_node.value = value
        current = self.head

        if idx == 0:
            self.head = new_node
            self.head.next = current # idx 가 0 이면 head가 가르키는 다음 요소를 current로 지정
        else:
            for _ in range(idx - 1):
                current = current.next  # current가 다음 노드를 가리키게 한다.
                new_node.next = current.next # 새로운 노드가 current의 다음노드를 가리키게 한다.
                current.next = new_node #current의 다음이 새로운 노드를 가리키게 한다. 
    def remove(self, idx):
        if idx == 0:
            self.head = self.head.next # idx가 0이면 head는 0번쨰 원소에서 1번쨰 원소를 가리킨다.
                                        # 0번째 원소는 가리키는 주소가 없으므로 gc에 의해 삭제
        else:
            current = self.head # head 가 가리키는 원소가 current
            for _ in range(idx - 1):    
                current = current.next # 다음 요소를 가리킴
                current.next = current.next.next # 다음 요소가 그 다음요소를 가리키므로 다음 요소는
                                                # 가리키는 원소가 없으므로 gc에 의해 삭제



ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.insert(idx = 2, value = 9)






