import queue

#Build a simple FIFO queue, as we want to have the oldest timestamp to be used first
q = queue.Queue()

for i in range(0,1000):
    q.put(i)

for i in range(0,1000):
    print(q.get())



