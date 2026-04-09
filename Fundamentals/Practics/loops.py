# For loop
# for i in range():
#     print("hello")



# * * *
# * * *
# * * *

# for i in range(3):
#     for j in range(3):
#         print("*", end=" ")
#     print()

# *
# * *
# * * *
# * * * *

# for i in range(1,5):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# * * * *
# * * *
# * *
# *

# for i in range(4,0,-1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

#     *
#    **
#   ***
#  ****

# for i in range(1,5):
#     for j in range(5-i):
#         print(" ", end=" ")
#     for k in range(i):
#         print("*", end=" ")
#     print()


#     *
#    ***
#   *****
#  *******

# for i in range(1,5):
#     for j in range(5-i):
#             print("x", end=" ")
#     for k in range(2*i -1):
#         print("*", end=" ")
#     print()

# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

# n = 5
# for i in range(1, n*2):
#     if i <= 5 : 
#         for j in range(i):
#             print("*", end=" ")
#     if i > 5:
#         for k in range(n*2 - i):
#             print("*", end=" ")
#     print()

#     *
#    **
#   ***
#  ****
# *****
#  ****
#   ***
#    **
#     *

# n = 5
# for i in range(1, n*2):
#     if i <= n:
#         spaces = n - i
#         stars = i
#     else:
#         spaces = i - n
#         stars = n*2 - i

#     for _ in range(spaces):
#         print(" ", end=" ")
#     for _ in range(stars):
#         print("*", end=" ")
    
#     print()

# ===========================================

# While loop

# * * * *
# * * *
# * *
# *

# i=0
# while i < 4:
#     j = i
#     while j  < 5:
#         print("*" , end=" ")
#         j+=1
#     i+=1
#     print()

# *
# * * 
# * * *
# * * * *
# * * * * *

i = 1
while i <= 5:
    j = i
    while j > 0 and j <= 5:
        print("*", end=" ")
        j-=1
    print();
    i+=1

