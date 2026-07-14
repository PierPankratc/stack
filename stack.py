class Stack:
    def __init__(self, stack: list = []):
        self.stack = stack

    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self,element):
        self.stack.append(element)
        pass

    def pop(self):
        last_element = self.stack.pop()
        return last_element
    
    def peek(self):
        if len(self.stack)>0:
            return self.stack[-1]
        pass
    
    def size(self):
        return len(self.stack)
    

def balanced_str():
    s = input()
    new_stack = Stack()
    pairs = {
        '(':')',
        '{':'}',
        '[':']'
    }
    for el in s:
        if el in pairs.keys():
            new_stack.push(el)
        else: 
            if new_stack.is_empty() or pairs[new_stack.pop()] != el:
                print('Несбалансированно')
                return 
        # print(tuple(new_stack.stack))
            
            
    if new_stack.is_empty():
        print('Сбалансированно')
        return 
    else:
        print('Несбалансированно')
        return 

balanced_str()



