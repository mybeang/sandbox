# def solution(X, Y, D): # bad solution
#     # Implement your solution here
#     jump_count = 0
#     while (X <= Y):
#         X += D
#         jump_count += 1
#
#     return jump_count

def solution(X, Y, D):  # nice solution
    distance = Y - X
    return (distance + D - 1) // D
