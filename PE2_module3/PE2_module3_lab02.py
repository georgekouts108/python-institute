class QueueError(Exception):  # Choose base class for the new exception.
    #
    #  Write code here
    #
    def __init__(self):
        pass
    
class Queue:
    def __init__(self):
        #
        # Write code here
        #
        self.__queue = []

    def put(self, elem):
        #
        # Write code here
        #
        self.__queue.insert(0, elem)

    def get(self):
        #
        # Write code here
        #
        try:
            if len(self.__queue) == 0:
                raise QueueError()
                
            val = self.__queue[-1]
            del self.__queue[-1]
            return val
        except (QueueError):
            print("Queue error")
        


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
