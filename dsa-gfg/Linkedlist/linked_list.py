class Node:
	def __init__(self, data = None, next = None):
		self.data = data 
		self.next = next

class Linkedlist:
	def __init__(self):
		self.head = None 

	def insert_at_begining(self, data):
		node = Node(data, self.head)
		self.head = node 

	def print(self):
		if self.head is None:
			print('Linked List is empty')
			return

		itr = self.head
		llstr = ''

		while itr:
			llstr += str(itr.data) + '-->'
			itr = itr.next

		print(llstr) 

	def insert_at_end(self,data):
		if self.head is None:
			node = Node(data, None)
			#self.head = Node(data,None)
			self.head = node
			return
		
		itr = self.head
		
		while itr.next:
			itr = itr.next

		itr.next = Node(data, None)

	def insert_values(self, data_list):
		self.head = None

		for data in data_list:
			self.insert_at_end(data)





if __name__ == '__main__':
	ll = Linkedlist()
	# ll.insert_at_begining(5)
	# ll.insert_at_begining(89)
	# ll.insert_at_end(15)
	# ll.insert_at_end(11)
	# ll.insert_at_begining(54)
	ll.insert_values([1,2,3,4,5,6])
	# ll.insert_values(['shubham','anish','himanshu'])
	ll.print()
