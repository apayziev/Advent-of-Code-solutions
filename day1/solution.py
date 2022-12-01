# with open("./input.txt", "r") as file:
# problem set 1

# num_list = {
#     f"Elf-{str(index)}": sum(map(int, num_list.split("\n")))
#     for index, num_list in enumerate(file.read().strip().split("\n\n"), start=1)
# }

# print(num_list[max(num_list, key=num_list.get)])

# problem set 2
# num_list = []
# lines = file.read().split("\n")
# store = 0
# for line in lines:
#     if line != "":
#         store += int(line)
#     else:
#         num_list.append(store)
#         store = 0
#         continue

# print(sum(sorted(num_list, reverse=True)[:3]))
