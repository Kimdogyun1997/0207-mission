
#
# import webbrowser
# import time
#
# ## 함수 선언 부분 ##
# def isStackFull() :
# 	global SIZE, stack, top
# 	if (top >= SIZE-1) :
# 		return True
# 	else :
# 		return False
#
# def isStackEmpty() :
# 	global SIZE, stack, top
# 	if (top == -1) :
# 		return True
# 	else :
# 		return False
#
# def push(data) :
# 	global SIZE, stack, top
# 	if (isStackFull()) :
# 		print("스택이 꽉 찼습니다.")
# 		return
# 	top += 1
# 	stack[top] = data
#
# def pop() :
# 	global SIZE, stack, top
# 	if (isStackEmpty()) :
# 		print("스택이 비었습니다.")
# 		return None
# 	data = stack[top]
# 	stack[top] = None
# 	top -= 1
# 	return data
#
# def peek() :
# 	global SIZE, stack, top
# 	if (isStackEmpty()) :
# 		print("스택이 비었습니다.")
# 		return None
# 	return stack[top]
#
# ## 전역 변수 선언 부분 ##
# SIZE = 100
# stack = [ None for _ in range(SIZE) ]
# top = -1
#
# ## 메인 코드 부분 ##
# if __name__ == "__main__" :
# 	urls = [ 'inha.edu', 'havard.edu', 'yale.edu']
#
# 	for url in urls :
# 		push(url)
# 		webbrowser.open('http://'+url)
# 		print(url, end = '-->')
# 		time.sleep(1)
#
# 	print("방문 종료")
# 	time.sleep(5)
#
# 	while True :
# 		url = pop()
# 		if url == None :
# 			break
# 		webbrowser.open('http://'+url)
# 		print(url, end = '-->')
# 		time.sleep(1)
# 	print("방문 종료")


## 괄호의 매칭 검사

## 함수 선언 부분 ##
# def is_Stack_Full() :
# 	global SIZE, stack, top
# 	if (top >= SIZE-1) :
# 		return True
# 	else :
# 		return False
#
# def is_Stack_Empty() :
# 	global SIZE, stack, top
# 	if (top == -1) :
# 		return True
# 	else :
# 		return False
#
# def push(data) :
# 	global SIZE, stack, top
# 	if (is_Stack_Full()) :
# 		print("스택이 꽉 찼습니다.")
# 		return
# 	top += 1
# 	stack[top] = data
#
# def pop() :
# 	global SIZE, stack, top
# 	if (is_Stack_Empty()) :
# 		print("스택이 비었습니다.")
# 		return None
# 	data = stack[top]
# 	stack[top] = None
# 	top -= 1
# 	return data
#
# def peek() :
# 	global SIZE, stack, top
# 	if (is_Stack_Empty()) :
# 		print("스택이 비었습니다.")
# 		return None
# 	return stack[top]
#
# def check_Bracket(expr) :
# 	for ch in exprssion:
# 		if ch in '([{<':
# 			push(ch)
# 		elif ch in ')]}>':
# 			out = pop()
# 			if ch == ')' and out == '(':
# 				pass
# 			elif ch == ']' and out == '[':
# 				pass
# 			elif ch == '}' and out == '{':
# 				pass
# 			elif ch == '>' and out == '<':
# 				pass
# 			else:
# 				return False
# 		else :  # 괄호 계열이 아닌 것들 ex)숫자, 연산자, 문자열 등
# 			pass
# 	if is_Stack_Empty() :
# 		return True
# 	else :
# 		return False
#
# ## 전역 변수 선언 부분 ##
# SIZE = 5
# stack = [ None for _ in range(SIZE) ]
# top = -1
#
# # 메인 코드 부분 ##
# if __name__ == "__main__" :
#
# 	exprssion_Ary = ['(2*[3+1)', ')A+B(', '((A+B)-C', '(A+B]', '(<A+{B-C}/[C*D]>)']
#
# 	for exprssion in exprssion_Ary :
# 		top = -1
# 		print(exprssion, '==>', check_Bracket(exprssion))



## <큐(Queue): first in, first out>


# 양쪽이 뚫려 있어 한쪽은 삽입(enQueue), 한 쪽은 추출(deQueue)
# front(머리), rear(꼬리)

# **추출(deQueue)는 front가 증가하고, 삽입(enQueue)는 rear가 증가.**
# front, rear 초기값 = -1

# is_Queue_Full() : if (rear == SIZE - 1) // if (rear == SIZE - 1) and (front == -1)
# is_Queue_Empty(): if (front == rear)

# peek : 추출될 데이터를 큐에 그대로 두고 확인만 하는 것. 값이 바뀌는 것 X


# 디큐로 인한 오버헤드를 방지하기 위한 원형 큐 -> if (front값 == rear 값): 큐가 비어있음
#                                     ->if ((rear값+1)%SIZE == front값): 큐 꽉 찼음 // 원형 큐는 공간 하나 loss

# 원형 큐가 꽉 차 있지 않을 때 -> rear = (rear+1) % 큐 크기
#                          -> front = (front+1) % 큐 크기



## 함수 선언 부분 ##
# def is_Queue_Full() :
# 	global SIZE, queue, front, rear
# 	if  rear + 1 % SIZE == front:
# 		return True
# 	else:
# 		return False
#
#
# def is_Queue_Empty() :
# 	global SIZE, queue, front, rear
# 	if front == rear:
# 		return True
# 	else :
# 		return False
#
#
# def en_Queue(data) :
# 	global SIZE, queue, front, rear
# 	if (is_Queue_Full()) :
# 		print("큐가 꽉 찼습니다.")
# 		return
# 	rear = (rear + 1) % SIZE
# 	queue[rear] = data
#
#
# def deQueue() :
# 	global SIZE, queue, front, rear
# 	if is_Queue_Empty():
# 		print("큐가 비었습니다.")
# 		return None
# 	front = (front + 1) % SIZE
# 	data = queue[front]
# 	queue[front] = None
# 	return data
#
#
# def peek() :
# 	global SIZE, queue, front, rear
# 	if is_Queue_Empty():
# 		print("큐가 비었습니다.")
# 		return None
# 	return queue[(front + 1) % SIZE]
#
# ## 전역 변수 선언 부분 ##
# SIZE = int(input("큐의 크기를 입력하세요 ==> "))
# queue = [ None for _ in range(SIZE) ]
# front = rear = 0
#
# ## 메인 코드 부분 ##
# if __name__ == "__main__" :
# 	select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")
#
# 	while select != 'X' and select != 'x':
# 		if select=='I' or select =='i' :
# 			data = input("입력할 데이터 ==> ")
# 			en_Queue(data)
# 			print("큐 상태 : ", queue)
# 			print("front : ", front, ", rear : ", rear)
# 		elif select=='E' or select =='e' :
# 			data = deQueue()
# 			print("추출된 데이터 ==> ", data)
# 			print("큐 상태 : ", queue)
# 			print("front : ", front, ", rear : ", rear)
# 		elif select=='V' or select =='v' :
# 			data = peek()
# 			print("확인된 데이터 ==> ", data)
# 			print("큐 상태 : ", queue)
# 			print("front : ", front, ", rear : ", rear)
# 		else :
# 			print("입력이 잘못됨")
#
# 		select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")
#
# 	print("프로그램 종료!")

# class Treenode():
#     def __init__ (self):
#         self.data = None
#         self.left = None
#         self.right = None
#
# node1 = Treenode()
# node1.data = "화사"
#
# node2 = Treenode()
# node2.data = "솔라"
# node1.left = node2
#
# node3 = Treenode()
# node3.data = "문별"
# node1.right = node3
#
# print(node1.left.data, node1.right.data, end = "")



# class TreeNode() :
# 	def __init__ (self) :
# 		self.left = None
# 		self.data = None
# 		self.right = None
#
# node1 = TreeNode()
# node1.data = '화사'
#
# node2 = TreeNode()
# node2.data = '솔라'
# node1.left = node2
#
# node3 = TreeNode()
# node3.data = '문별'
# node1.right = node3
#
# node4 = TreeNode()
# node4.data = '휘인'
# node2.left = node4
#
# node5 = TreeNode()
# node5.data = '쯔위'
# node2.right = node5
#
# node6 = TreeNode()
# node6.data = '선미'
# node3.left = node6
#
# # node7 = TreeNode()
# # node7.data = '다현'
# # node4.right = node7
# #
# # node8 = TreeNode()
# # node8.data = '사나'
# # node6.left = node8
#
#
# def preorder(node) :
# 	if node == None:
# 		return
# 	print(node.data, end='->')
# 	preorder(node.left)
# 	preorder(node.right)
# #
# def inorder(node):
# 	if node == None :
# 		return
# 	inorder(node.left)
# 	print(node.data, end='->')
# 	inorder(node.right)
#
# def postorder(node):
# 	if node == None :
# 		return
# 	postorder(node.left)
# 	postorder(node.right)
# 	print(node.data, end='->')
# #
# print('전위 순회 : ', end = '')
# preorder(node1)
# print('끝')
#
# print('중위 순회 : ', end = '')
# inorder(node1)
# print('끝')
#
# print('후위 순회 : ', end = '')
# postorder(node1)
# print('끝')




## 함수 선언 부분 ##
class TreeNode():
	def __init__(self):
		self.left = None
		self.data = None
		self.right = None


## 전역 변수 선언 부분 ##
# memory = []
# root = None
# nameAry = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']
#
# ## 메인 코드 부분 ##
# node = TreeNode()
# node.data = nameAry[0]
# root = node
# memory.append(node)
#
# for name in nameAry[1:]:
#
# 	node = TreeNode()
# 	node.data = name
#
# 	current = root
# 	while True:
# 		if name < current.data:
# 			if current.left == None:
# 				current.left = node
# 				break
# 			current = current.left
# 		else:
# 			if current.right == None:
# 				current.right = node
# 				break
# 			current = current.right
#
# 	memory.append(node)
#
# deleteName = '마마무'
#
# current = root
# parent = None
# while True:
# 	if deleteName == current.data:
#
# 		if current.left == None and current.right == None:
# 			if parent.left == current:
# 				parent.left = None
# 			else:
# 				parent.right = None
# 			del (current)
#
# 		elif current.left != None and current.right == None:
# 			if parent.left == current:
# 				parent.left = current.left
# 			else:
# 				parent.right = current.left
# 			del (current)
#
# 		elif current.left == None and current.right != None:
# 			if parent.left == current:
# 				parent.left = current.right
# 			else:
# 				parent.right = current.right
# 			del (current)
#
# 		print(deleteName, '이(가) 삭제됨.')
# 		break
# 	elif deleteName < current.data:
# 		if current.left == None:
# 			print(deleteName, '이(가) 트리에 없음')
# 			break
# 		parent = current
# 		current = current.left
# 	else:
# 		if current.right == None:
# 			print(deleteName, '이(가) 트리에 없음')
# 			break
# 		parent = current
# 		current = current.right



import random
## 함수 선언 부분 ##
class TreeNode() :
	def __init__ (self) :
		self.left = None
		self.data = None
		self.right = None

## 전역 변수 선언 부분 ##
memory = []
rootBook, rootAuth = None, None
bookAry = [ ['어린왕자', '쌩떽쥐베리'],['이방인', '까뮈'], ['부활', '톨스토이'],
		   ['신곡', '단테'], ['돈키호테', '세브반테스'], ['동물농장', '조지오웰'],
		   ['데미안','헤르만헤세'], ['파우스트', '괴테'], ['대지', '펄벅'] ]
random.shuffle(bookAry)

## 메인 코드 부분 ##

### 책 이름 트리 ###
node = TreeNode()
node.data = bookAry[0][0]
rootBook = node
memory.append(node)

for book in bookAry[1:] :
	name = book[0]
	node = TreeNode()
	node.data = name

	current = rootBook
	while True :
		if name < current.data :
			if current.left == None :
				current.left = node
				break
			current = current.left
		else :
			if current.right == None :
				current.right = node
				break
			current = current.right

	memory.append(node)

print("책 이름 트리 구성 완료!")

preorder(rootBook)

### 작가 이름 트리 ###
node = TreeNode()
node.data = bookAry[0][1]
rootAuth = node
memory.append(node)

for book in bookAry[1:] :
	name = book[1]
	node = TreeNode()
	node.data = name

	current = rootAuth
	while True :
		if name < current.data :
			if current.left == None :
				current.left = node
				break
			current = current.left
		else :
			if current.right == None :
				current.right = node
				break
			current = current.right

	memory.append(node)

print("작가 이름 트리 구성 완료!")
preorder(rootBook)

## 책 이름 및 작가 이름 검색 ##
bookOrAuth = int(input('책검색(1), 작가검색(2)-->'))
findName = input('검색할 책 또는 작가-->')

if bookOrAuth == 1 :
	root = rootBook
else :
	root = rootAuth

current = root
while True:
	if findName == current.data :
		print(findName, '을(를) 찾음.')
		findYN = True
		break
	elif findName < current.data :
		if current.left == None :
			print(findName, '이(가) 목록에 없음')
			break
		current = current.left
	else:
		if current.right == None :
			print(findName, '이(가) 목록에 없음')
			break
		current = current.right


