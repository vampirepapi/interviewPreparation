#YT - Link = https://www.youtube.com/watch?v=qp8u-frRAnU&t=633s&ab_channel=codebasics
class Node:
	def __init__(self, data = None, next = None):
		self.data = data 
		self.next = next

class Linkedlist:
	def __init__(self):
		self.head = None 


	#Inserting data at the begining
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
			llstr += str(itr.data) + '-->' if itr.next else str(itr.data)
			itr = itr.next

		print(llstr) 


	#Inserting data at the end
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


	#Inserting list of values as input
	def insert_values(self, data_list):
		self.head = None

		for data in data_list:
			self.insert_at_end(data)

	#length of the linked list
	def get_length(self):
		count = 0

		itr = self.head

		while itr:
			count+=1
			itr = itr.next

		return count


	#Remove from given index
	def remove_at(self, index):
		if index < 0 or index >= self.get_length():
			raise Exception("invalid index")

		if index == 0:
			self.head = self.head.next
			return

		count = 0
		itr = self.head

		while itr:
			if count == index-1:
				itr.next = itr.next.next
				break

			itr = itr.next
			count+=1


	#insert at given index
	def insert_at(self, index, data):
		if index < 0 or index > self.get_length():
			raise Exception('invalid index')

		if index == 0:
			self.insert_at_begining(data)
			return

		
		count = 0
		itr = self.head

		while itr:
			if count == index - 1:
				node = Node(data, itr.next)
				itr.next = node

			itr = itr.next
			count += 1


#if __name__ == '__main__':
ll = Linkedlist()
# ll.insert_at_begining(5)
# ll.insert_at_begining(89)
# ll.insert_at_end(15)
# ll.insert_at_end(11)
# ll.insert_at_begining(54)
#ll.insert_values([1,2,3,4,5,6])
ll.insert_values(['shubham','anish','himanshu'])
#ll.print()
print("Length:", ll.get_length())
ll.remove_at(2)
ll.insert_at(1,"sourabh")
ll.print()
