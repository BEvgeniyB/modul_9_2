# cpllec = [1,4,5,8,6,3,7]
# list_mya = [x * 3 for x in cpllec if  x // 2]
# # list_mya = [x 2 if x % 2 else x for x in cpllec ]
# print(list_mya)

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(x) for x in first_strings if len(x) >= 5]
second_result = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]
# third_result = {x: len(x) for x in (first_strings+second_strings) if not len(x) % 2}
# third_result = {x: len(x) for x in [*first_strings,*second_strings] if not len(x) % 2}
third_result = {x: len(x) for k in [first_strings,second_strings] for x in k  if not len(x) % 2}
print(first_result)
print(second_result)
print(third_result)
