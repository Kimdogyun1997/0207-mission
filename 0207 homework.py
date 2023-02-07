rear = -1
front = -1
SIZE = 5

queue = [None for _ in range(SIZE)]


def is_Queue_Full():
    global SIZE, front, rear, queue
    if rear == SIZE - 1:
        return True
    else:
        return False


def is_Queue_Empty():
    global SIZE, queue, front, rear
    if front == rear:
        return True
    else:
        return False


def En_Queue(data):
    global SIZE, queue, front, rear
    if (is_Queue_Full()):
        print("현재 줄이 꽉 찼습니다. 잠시만 기다려주십시오.")
        return
    else:
        rear += 1
        queue[rear] = data


def De_Queue(data) :
	global SIZE, queue, front, rear
	if (is_Queue_Empty()) :
		print("큐가 비었습니다.")
		return None
	front += 1
	data = queue[front]
	queue[front] = None

	for i in range(front + 1, rear + 1): 	# 모든 사람을 한칸씩 앞으로 당긴다.
		queue[i - 1] = queue[i]
		queue[i] = None
	front = -1
	rear -= 1

	return data







def peek():  # peek : 추출될 데이터를 큐에 그대로 두고 확인만 하는 것. 값이 바뀌는 것 X
    global SIZE, queue, fornt, rear
    if (is_Queue_Empty()):
        print('현재 줄이 없습니다.')
        return None
    return queue[front+1]
#
En_Queue("스펀지밥")
En_Queue("징징이")
En_Queue("뚱이")
En_Queue("집게사장")
En_Queue("플랭크톤")

print("대기 줄 상태:", queue)

for j in range(5):
    print(De_Queue(queue), "이(가) 들어가신다!")
    print("대기 줄 상태:", queue )

    if queue[:] == None:
        print("퇴근이닷!")




# SIZE = 6
# front = 0  # 순차 큐와 달리 0번 칸 앞쪽이 -1이 아니므로 둘 다 초기값은 0
# rear = 0
# queue = [None for _ in range(SIZE)]
# total_time = 0
#
# def Is_Queue_Empty():
#     global SIZE, queue, front, rear
#     if front == rear:
#         return True
#     else:
#         return False
#
#
# def Is_Queue_Full():
#     global SIZE, queue, front, rear
#     if (rear+1) % SIZE == front:
#         print("대기시간이 꽉 찼습니다.")
#         return True
#     else:
#         return False
#
#
# def En_Queue(data):
#     global SIZE, queue, front, rear
#     if Is_Queue_Full():
#         print("대기시간이 꽉 찼습니다")
#         return
#     rear = (rear + 1) % SIZE
#     queue[rear] = data
#
#
# def De_Queue(data):
#     global SIZE, queue, front, rear
#     if Is_Queue_Empty():
#         print("대기시간이 없습니다.")
#         return None
#     front = (front + 1) % SIZE
#     queue[front] = None
#
#
#
# def peeck():
#     global SIZE, queue, front, rear
#     if Is_Queue_Empty():
#         print("볼 필요 없다.")
#         return None
#     return queue[(front+1) % SIZE]
#
#
# def Calc_Time():
#     global SIZE, queue, front, rear, total_time
#     for i in range(SIZE):
#         if queue[i] == None:
#             continue
#             total_time += queue[i][1]
#     return total_time
#
# if __name__ =="__main__":
#
#
#     Waiting = [("사용", 7), ("고장", 3), ("환불", 5), ("환불", 5), ("고장",3) ]
#
#     for wait in Waiting:
#         print("귀하의 현재 대기시간은", Calc_Time(), "분입니다")
#         print("현재 대기 콜", queue)
#         En_Queue(wait)



# import random
#
# class TreeNode():
#     def __init__(self):
#         self.data = None
#         self.left = None
#         self.right = None
#
# memory = [ ]
# root = None
# dataAry = ["쪼코우유", "왕뚜껑", "트롤리", "카스", "참치마요", "신라면", "참이슬"]
#
# sellAry = [random.choice(dataAry) for _ in range(20)]
#
# print("오늘 판매된 물건(중복허용 -->", sellAry)
#
# node1 = TreeNode()
# node1.data = sellAry[0]
# root = node1
# memory.append(node1)
#
# for name in sellAry[1:] :
#
# 	node = TreeNode()
# 	node.data = name
#
# 	current = root
# 	while True :
# 		if name == current.data :
# 			break
# 		if name < current.data :
# 			if current.left == None :
# 				current.left = node
# 				memory.append(node)
# 				break
# 			current = current.left
# 		else :
# 			if current.right == None :
# 				current.right = node
# 				memory.append(node)
# 				break
# 			current = current.right
#
# print("이진 탐색 트리 구성 완료!")
#
# def preorder(node) :
# 	if node == None :
# 		return
# 	print(node.data, end = ' ')
# 	preorder(node.left)
# 	preorder(node.right)
#
# print('오늘 판매된 종류(중복X)--> ', end = ' ')
# preorder(root)

