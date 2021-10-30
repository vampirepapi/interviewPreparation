contents = []
while True:
    try:
        line = int(input())
    except EOFError:
        break
    contents.append(line)
# print(contents)
for x in contents:
	if x==42:
		break
	else:
		print(x)

