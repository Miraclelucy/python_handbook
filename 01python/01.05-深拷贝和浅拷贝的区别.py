import copy
origin = [1, 2, [3, 4]]
#origin 里边有三个元素：1， 2，[3, 4]
cop1 = copy.copy(origin)
cop2 = copy.deepcopy(origin)
print(cop1 == cop2)
print(cop1 is cop2)
#cop1 和 cop2 看上去相同，但已不再是同一个object
#把origin内的子list [3, 4] 改掉了一个元素，观察 cop1 和 cop2
origin[2][0] = "hey!"
print(origin)
print(cop1)
print(cop2)
#把origin内的元素 [1, 2] 改掉了一个元素，观察 cop1 和 cop2
origin[0] = "mark"
print(origin)
print(cop1)
print(cop2)
