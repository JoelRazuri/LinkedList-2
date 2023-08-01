"""
    Ejercicio 11.7. Agregar a ListaEnlazada un método extend que reciba una ListaEnlazada y agregue a la lista actual los elementos que se encuentran en la lista recibida.
""" 
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.first = None
        self.size = 0

    def append(self, value):
        my_node = Node(value)

        if self.size == 0:
            self.first = my_node
        else:
            current = self.first
            while current.next != None:
                current = current.next
            current.next = my_node
        
        self.size+=1
        
        return my_node

    def remove(self, value):
        if self.size == 0:
            return False
        else:
            current = self.first
            try:
                if current.value == value:
                    deleted_node = current
                    self.first = deleted_node.next
                    current = self.first
                    self.size-=1
                    return deleted_node
                    
                while current.next.value != value:
                    if current.next == None:
                        return False
                    current = current.next
                
                deleted_node = current.next
                current.next = deleted_node.next
            except AttributeError:
                return False
        self.size-=1
        
        return deleted_node

    def __len__(self):
        return self.size
    
    # Ejercicio 11.6.
    def __str__(self):
        string = "["
        current = self.first
        
        for i in range(len(self)):
            string += str(current)
            if i != len(self) - 1:
                string += str(", ")
            current = current.next
        
        string +="]"

        return string
    
    # Ejercicio 11.7
    def extend(self, new_linked_list):
        
        current = new_linked_list.first

        for i in range(len(new_linked_list)):
            self.append(current.value)
            current = current.next


my_list1 = LinkedList()
my_list2 = LinkedList()


my_list1.append(1)
my_list1.append(2)
my_list1.append(3)
my_list1.append(4)

my_list2.append(5)
my_list2.append(6)
my_list2.append(5)
my_list2.append(7)


print(f"Lista 1 : {my_list1}")
print(f"Lista 2 : {my_list2}")

my_list1.extend(my_list2)

print(f"Lista extendida: {my_list1}")
print(len(my_list1))