class Human:
	def __init__(self,n,o):
		self.name = n
		self.occupation = o

	def do_work(self):
		if self.occupation == 'actor':
			print(self.name, 'shoots movies')

		elif self.occupation == 'tennis player':
			print(self.name, 'plays tennis')

	def do_speaks(self):
		print(self.name, "says fuck off shithead")

tom = Human('tom cruise', 'actor')
tom.do_work()
tom.do_speaks()

maria = Human('maria sharapova', 'tennis player')
maria.do_work()
maria.do_speaks()