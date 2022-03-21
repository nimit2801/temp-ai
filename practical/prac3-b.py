# Priority Queue in python

queue = []

# Adding elements to the queue
queue.append('12')
queue.append('1')
queue.append('14')
queue.append('7')

print("Initial queue")
print(queue)

max = 0
# while not len(queue) == 0:
for i in range(len(queue)):
    if(queue[i] > queue[max]):
        print("i: "+queue[i] + " max: "+queue[max])
        max = i
        print(queue[max])
    else:
        print("skip")
    # del queue[max]
# print(queue[max])
