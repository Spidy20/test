# i=0
a=('shok','kushal','chintan')
b=list(a)
b[1]='chintan'
a=tuple(b)
print(a)

# j=6
#
# for row in range(4):
#     for col in range(7):
#         if row==col:
#             print('*',end='')
#         elif row==i and col==j:
#             print('*',end='')
#             i=i+1
#             j=j-1
#         else:
#             print(end=' ')
#     print()
#
#
# ## i code
#
#
# for row in range(7):
#     for col in range(5):
#         if col==2 or ((row==0 or row==6) and col!=2):
#             print('*',end='')
#         else:
#             print(end=' ')
#     print()
#
#
# ## m code
#
# for row in range(7):
#     for col in range(7):
#         if col==0 or col==6 or ((row==col) and (col>0 and col<4)) or (row==1 and col==5) or (row==2 and col==4):
#             print('*',end='')
#         else:
#             print(end=' ')
#     print()
#
#
# ## a code
#
# for row in range(7):
#     for col in range(5):
#         if ((col==0 or col==4) and row!=0) or (row==0 or row==3) and (col>0 and col<4):
#             print('*',end='')
#         else:
#             print(end=' ')
#     print()
#
#
# ## r code
#
# for row in range(7):
#     for col in range(5):
#         if col==0 or (col==4 and( row!=0 and row!=3)) or (row==0 or row==3 and (col>0 and col<4)):
#             print('*',end='')
#         else:
#             print(end=' ')
#     print()
#
#
#
# ## s code
#
# for row in range(7):
#     for col in range(5):
#         if (row==0 or row==3 or row==6) and (col>0 and col<4) or (col==0 and (row>0 and row<3)) or (col==4 and (row>3 and row<6)):
#             print('*',end='')
#         else:
#             print(end=' ')
#     print()
#
#
# ## h code
#
# for row in range(7):
#     for col in range(5):
#         if col==0 or col==4 or (row==3 and (col>0 and col<4)):
#             print('*',end='')
#         else:
#             print(end=' ')
#     print()
