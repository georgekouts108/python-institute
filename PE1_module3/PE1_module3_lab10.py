blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
#	

height = 0
blocks_used = 0
_next = 1

while blocks_used <= blocks:
    blocks_used += _next
    height += 1
    _next += 1
    if blocks_used > blocks:
        height -= 1
    
print("The height of the pyramid:", height)
