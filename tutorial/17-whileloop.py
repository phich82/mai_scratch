i = 1

while i < 6:
  print(i)
  i += 1 # i + 1 is increment
# l1: 1 < 6 => true
#   i = 1
#   in ra 1
#   i = 1 + 1 = 2
# l2: 2 < 6 => True
#   in ra 2
#   i = 2 + 1 = 3
# l3: 3 < 6 => True
#   in ra 3 
#   i = 3 + 1 = 4
# l4: 4 < 6
#   in ra 4
#   i = 4 +1 =5
# l5: 5 < 6 => True
#   in ra 5
# i = 5 + 1 = 6
# l6: 6 < 6 => False

i = 1
while i < 6:
  print(i)
  if (i == 3):
    break # stop `while`` loop
  i += 1
  
# i = 1
# l1: 1 < 6 => true
#  in ra 1
#  1 == 3 => False
#  i = 1 + 1 =2

# i = 2 
# l2: 2 < 6 => True
#   in ra 2
#   2 == 3 => False
#   i = 2 + 1 = 3
  
# i = 3
# l3: 3 < 6 => True
# in ra 3
# 3==3 => True
# stop

 
i = 0
while i < 6: # in 'while' loop need break and continue to exit or continue the 'while' loop
  i += 1
  if i == 3:
    continue
  print(i)
  
# """ i = 0
# l1: 0 < 6 => True
#   i=0+1=1
#   1==3=>False
#   in ra 1

# l2: 1 < 6 => True
#  i=1+1=2
#  2==3 => False
#  in ra 2
  
# l3: 2 < 6 => True 
#  i=2+1=3
#  3==3 => True
#   continue => continue next loop (all codes after `continue` are NOT executed)

# l4: 3 < 6 => True
#  i=3+1=4
#  4==3 => False
#  in ra 4

# l5: 4 < 6 => True
#  i=4+1=5
#  5==3 => False
#  in ra 5

# l6: 5 < 6 => True
#  i=5+1=6
#  6==3 => False
#  in ra 6
# l7: 6 < 6 => False
#  stop
# Note that number 3 is missing in the result

