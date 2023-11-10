class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Queue:
  
  def __init__(self):
    self.head = None
    self.tail = None

  def enqueue(self, newData):
    newNode = Node(newData)
    if self.head == None:
      self.head = newNode
      self.tail = newNode
      print("New Data Added")
    else:
      temp = self.head
      while temp.next:
        temp = temp.next
      temp.next = newNode
      self.tail = temp.next
      print("New Data Added")

  def dequeue(self):
    if self.head == None:
      print("List is Empty")
    else:
      current = self.head
      self.head = self.head.next
      print("Data Deleted")
      return current

  def displayHead(self):
    if self.head == None:
      print("List is Empty")
    else:
      print(self.head.data)

  def displayTail(self):
    if self.head == None:
      print("List is Empty")
    else:
      print(self.tail.data)


queue = Queue()
while True:
  print("1. Enqueue")
  print("2. Dequeue")
  print("3. Display front")
  print("4. Display rear")
  print("5. Exit")

  choice = int(input("Enter your choice : "))

  if choice == 1:
      data = input("Enter data to be inserted : ")
      queue.enqueue(data)
  elif choice == 2:
      data = queue.dequeue()
      if data != None:
          print(f"{data} removed from queue")
      else:
          print("Queue is empty")
  elif choice == 3:
      queue.displayHead()
  elif choice == 4:
      queue.displayTail()
  elif choice == 5:
      break
  else:
      print("Invalid choice")