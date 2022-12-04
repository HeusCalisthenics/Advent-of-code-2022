with open(r"data\data_3.txt","r") as day3:
    read = day3.readlines()

l = []
# print(read)
for x in read:
    length = int((len(x)-1)/2)
    first_half = x[:length]
    second_half = x[length:]
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in letters:
        if i in first_half and i in second_half:
            l.append(i)


part_1_total = 0
for letter in l:
    value = letters.index(letter)+1
    part_1_total += value
print(part_1_total)

