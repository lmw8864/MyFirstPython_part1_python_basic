# tuple.py

dimensions = (200, 50)
print(dimensions[0])  # 200
print(dimensions[1])  # 50

# 튜플을 수정하려고 하면?
# dimensions[0] = 250

# Traceback (most recent call last):
#   File "D:/Users/Minwoo_Lee/Documents/ImaDeveloper/myFirstPython/part1/4_list/tuple.py", line 6, in <module>
#     dimensions[0] = 250
# TypeError: 'tuple' object does not support item assignment


# 리스트처럼 루프도 가능하고~
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)
# 200
# 50

print("\n")

# 튜플은 수정할 수 없으므로, 필요하면 새로 정의해서 쓴다. (덮어쓰기)
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
for dimension in dimensions:
    print(dimension)

# 200
# 50
# 400
# 100
