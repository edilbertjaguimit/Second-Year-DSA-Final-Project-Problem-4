# Write a menu-driven program that will implement the concept of queue data structure. Your
# program will ask the user to insert into the queue, remove from the queue, and display both the
# front and last values.

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Queue:
  
  def __init__(self):
    # Initializes an empty queue with head and tail pointers set to None.
    self.head = None
    self.tail = None

  # Insert at the End
  def enqueue(self, newData):
    # Creates a new node with the given data.
    newNode = Node(newData)
    if self.head == None:
      # If the queue is empty, sets the new node as the head and tail.
      self.head = newNode
      self.tail = newNode
      print("New Data Added")
    else:
      # Iterates through the list to find the last node.
      temp = self.head
      while temp.next:
        temp = temp.next
      # Sets the next pointer of the last node to point to the new node, and updates the tail pointer.
      temp.next = newNode
      self.tail = temp.next
      print("New Data Added")

  # Delete at the Beginning
  def dequeue(self):
    if self.head == None:
      print("List is Empty")
    else:
      # Retrieves the data from the head of the queue.
      current = self.head
      # Updates the head pointer to point to the next node in the list.
      self.head = self.head.next
      print("Data Deleted")
      # Returns the retrieved data.
      return current.data

  # Prints the data of the Head node.
  def displayHead(self):
    if self.head == None:
      print("List is Empty")
    else:
      print(self.head.data)

  # Prints the data of the Tail node.
  def displayTail(self):
    if self.head == None:
      print("List is Empty")
    else:
      print(self.tail.data)


queue = Queue()
while True:
  print("1. Enqueue")
  print("2. Dequeue")
  print("3. Display Head")
  print("4. Display Tail")
  print("5. Exit")

  choice = input("Enter your choice : ")
  print()
  if choice == '1':
    data = input("Enter Data to be Added : ")
    queue.enqueue(data)
  elif choice == '2':
    queue.dequeue()
  elif choice == '3':
    queue.displayHead()
  elif choice == '4':
    queue.displayTail()
  elif choice == '5':
    print("Program Terminated.")
    break
  else:
    print("Invalid Input")
  print()