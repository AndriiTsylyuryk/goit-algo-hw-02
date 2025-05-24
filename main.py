import queue
from collections import deque


queue = queue.Queue(maxsize = 3)

def generate_request():
    request = 'New request'
    if not queue.full():
        queue.put(request)
        print("request added to queue.", queue.queue)
    else:
        print("Queue is full!")


def process_request():
    if not queue.empty():
        request = queue.get()
        print("Processing:", request)
    else:
        print("Queue is empty")


while True:
    command = input("Enter 'R' to create request, 'P' to process, 'E' to exit: ").lower()
    
    if command == 'r':
        generate_request()
    elif command == 'p':
        process_request()
    elif command == 'e':
        print('Request suspended')
        break 
    else: 
        print('unknown command')



# //////////////////

# rotator

def isPalindrome(string):
    string = string.lower()
    d = deque(string)
    while len(d) > 1:
        if d[0] == d[-1]:
            d.pop()
            d.popleft()
        else: 
            return 'not a palindrome'
    return True
    

print(isPalindrome('rotator'))