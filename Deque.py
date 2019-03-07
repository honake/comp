from collections import deque

L=deque([1,2,3,4])
#push,enqueue
L.append(5) #[1,2,3,4,5]
#pop
L.pop() #[1,2,3,4]
#dequeue
L.popleft() #[2,3,4]
