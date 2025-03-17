# stack
class stack(object):
    # constructor
    def __init__(self):
        self.stack=[]
        self.numofitems=0 # or any variable we assign instead of no.of. items
    # checking stack empty or not
    def isempty(self):
        return self.stack==[]
    # pushing or adding element
    def push(self,data): #only one arguement give ,for multiple arguments use *data,items etc.
        self.stack.insert(self.numofitems,data)
        self.numofitems+=1 #increment index num
        return '{} pushed to stack'.format(data)
    # deleting the element
    def pop(self):
        self.numofitems-=1
        data=self.stack.pop(self.numofitems)
        return '{} pop to stack'.format(data)
    # element size
    def stacksize(self):
        return len(self.stack)

# testing

if __name__=='__main__':
    s=stack()
    print(s.push(2)) 
    print(s.push(4)) 
    print(s.push(6)) 
    print(s.push(9)) 
   
    print(s.pop())
    print(s.stacksize())