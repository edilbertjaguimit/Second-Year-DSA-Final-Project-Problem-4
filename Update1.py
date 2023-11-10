class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front == None

    def enqueue(self, data):
        new_node = Node(data)

        if self.rear == None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None

        temp = self.front
        self.front = temp.next

        if(self.front == None):
            self.rear = None
        return temp.data

    def display_front(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Front item is:", self.front.data)

    def display_rear(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Rear item is:", self.rear.data)

queue = Queue()

while True:
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display front")
    print("4. Display rear")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = input("Enter data to be inserted: ")
        queue.enqueue(data)
    elif choice == 2:
        data = queue.dequeue()
        if data != None:
            print(f"{data} removed from queue")
        else:
            print("Queue is empty")
    elif choice == 3:
        queue.display_front()
    elif choice == 4:
        queue.display_rear()
    elif choice == 5:
        break
    else:
        print("Invalid choice")
