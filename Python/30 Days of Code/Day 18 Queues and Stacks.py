# Solution for Day 18 Queues and Stacks

class Solution:

    # Write your code here

    def __init__(self):
        from collections import deque
        self.__stack = deque()
        self.__queue = deque()

    def pushCharacter(self, char):
        self.__stack.append(char)

    def enqueueCharacter(self, char):
        self.__queue.append(char)

    def popCharacter(self):
        return self.__stack.pop()

    def dequeueCharacter(self):
        return self.__queue.popleft()


# read the string s
s = input()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")
