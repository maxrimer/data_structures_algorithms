# total = 0
# count = 0
# while True:
#     inp = input('Please enter a number: ')
#     if inp == 'done':
#         break
#     value = float(inp)
#     total += value
#     count += 1
#     average = total / count
#
# print(f'Average: {average}')


lst = []
while True:
    inp = input('Please enter a number: ')
    if inp == 'done':
        break
    lst.append(float(inp))

average = sum(lst)/len(lst)
print(f'Average: {average}')
