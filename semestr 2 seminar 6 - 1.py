class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
class LinkedList:
     def __init__(self):
        self.start_node = None

     def insert_at_start(self, data):
         new_node = Node(data)
         new_node.next = self.start_node
         self.start_node = new_node

     def insert_at_end(self, data):
         new_node = Node(data)
         if self.start_node is None:
             self.start_node = new_node
             return
         current = self.start_node
         while current.next is not None:
             current = current.next
         current.next = new_node
     def insert_after_item(self, x, data):
         current = self.start_node
         while current is not None:
              if current.item == x:
                   break
         current = current.next
         if current is None:
              print("item not in the list")
         else:
              new_node = Node(data)
         new_node.next = current.next
         current.next = new_node

     def del_start(self):
         if self.start_node is None:
             print("is empty")
             return
         self.start_node = self.start_node.next

     def del_end(self):
         if self.start_node is None:
             print("is empty")
             return
         if self.start_node.next is None:
             self.start_node = None
             return
         current = self.start_node
         while current.next is not None:
             m = current
             current = current.next
         m.next = None
     def del_after_item(self, data):
         current = self.start_node
         while current.item != data:
             if current.next == None:
                 print("value is not available")
                 return
             prev = current
             current = current.next
         prev.next = current.next
     def print_list(self):
         if self.start_node is None:
             print("List has no element")
             return
         else:
              current = self.start_node
         while current is not None:
              print(current.item, end=" ")
              current = current.next
     def command(self):
         a = int(input("Введите номер команды"))
         if a == 0:
             exit()
         if a == 1:
             new_linked_list.print_list()
         if a == 2:
             data = int(input('Добавте чего хотите'))
             new_linked_list.insert_at_start(data)
             new_linked_list.print_list()
         if a == 3:
             data = int(input('Добавте чего хотите'))
             new_linked_list.insert_at_end(data)
             new_linked_list.print_list()
         if a == 4:
             x = int(input('до какого элемента хотите добавить?'))
             data = int(input('Добавте чего хотите'))
             new_linked_list.insert_after_item(x, data)
             new_linked_list.print_list()
         if a == 5:
             new_linked_list.del_start()
             new_linked_list.print_list()
         if a == 6:
             new_linked_list.del_end()
             new_linked_list.print_list()
         if a == 7:
             data = int(input('Удалите чего хотите'))
             new_linked_list.del_after_item(data)
             new_linked_list.print_list()
         if a == 8:
             self.start_node = None
             new_linked_list.print_list()
         new_linked_list.command()

new_linked_list = LinkedList()
k = int(input("Введите количество звеньев"))
for i in range(k):
    x = int(input('Введите элемент'))
    new_linked_list.insert_at_end(x)
new_linked_list.command()