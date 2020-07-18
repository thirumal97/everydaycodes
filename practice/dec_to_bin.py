from stack import Stack

def convert_int_to_bin(dec_num):
    
    stack = Stack()
    while dec_num > 0:
        stack.push(dec_num%2)
        dec_num = dec_num//2
    s = []
    while not stack.is_empty():        
        s.append(str(stack.pop()))
    return ''.join(s)
    #s = ""    
    #while not stack.is_empty():
        #s+=str(stack.pop())        
    #return s

n= int(input())
print(convert_int_to_bin(n))
