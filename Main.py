class Solution:

    def __init__(self, size):
        self.stack = []
        self.queue = []
        self.size = size
        self.top = -1
        self.rear = -1
        self.front = -1

    def is_stack_empty(self):
        return self.top == -1
    
    def is_queue_empty(self):
        return self.front == -1 or self.front > self.rear

    def is_stack_full(self):
        return self.top == self.size - 1

    def is_queue_full(self):
        return self.rear == self.size - 1

    def push_character(self, character):
        if not self.is_stack_full():
            self.stack.append(character)
            self.top += 1
            
    def enqueue_character(self, character):
        if not self.is_queue_full():
            if  self.front == -1:
                self.front = 0
            self.rear += 1
            self.queue.append(character)
            
    def pop_character(self):
        if not self.is_stack_empty():
            self.top -= 1
            return self.stack.pop(self.top + 1)

    def dequeue_character(self):
        if not self.is_queue_empty():
            self.front += 1
            return self.queue[self.front - 1]
        
# read the string text
text = input()
# find the length of text
length_of_text = len(text)
# Create the Solution class object
solution = Solution(length_of_text)
# push/enqueue all the characters of string text to stack

for index in range(length_of_text):
    solution.push_character(text[index])
    solution.enqueue_character(text[index])

is_palindrome = True
for index in range(length_of_text):
    if solution.pop_character() != solution.dequeue_character():
        is_palindrome = False

# finally print whether string text is palindrome or not.
if is_palindrome:
    print("The word, " + text + ", is a palindrome.")
else:
    print("The word, " + text + ", is not a palindrome.")
