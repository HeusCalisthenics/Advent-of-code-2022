with open(r"data\data_3.txt","r") as day3:
    read = day3.readlines()

def convertCharToInt(c):
    return ord(c) - 96 if c.islower() else ord(c) - 38

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
# print(part_1_total)

def part2():
    keys = []
    for b in range(0, len(read), 3):
            current = []
            badge = read[b]
            badge = read[b].replace('\n', '')
            
            for t in badge:
                if t in read[b + 1] and t in read[b + 2] and t not in current:
                    keys.append(t)
                    current.append(t)
    
    return(keys)
 

print(part2())
part_2_total = 0
for num in part2():
    value2 = letters.index(num) +1
    part_2_total += value2

print(part_2_total)