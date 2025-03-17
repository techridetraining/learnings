class Queue(object):
    def __init__(self):
        self.queue=[]
    def isempty(self):
         return self.queue==[]
    def enqueue(self,item):
        self.queue.insert(0,item)
        return '{}add to queue'.format(item)
    def dequeue(self):
          return self.queue.pop()
    def queuesize(self):
        return '{} size of queue'.format(len(self.queue))
# testing

if __name__=='__main__':
     q=Queue()
     print(q.enqueue(1))
     print(q.enqueue(6))
     print(q.enqueue(2))

     print(q.dequeue())

     print(q.queuesize())
     print(q.isempty())
 


     