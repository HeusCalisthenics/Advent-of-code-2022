#part 2
A = 1
B = 2
C = 3

X = 1
Y= 2
Z = 3
rock = 1
paper = 2
scissors = 3

lose = 0 
draw = 3
win = 6



with open(r"data\day_2.txt",'r')  as input:
    read = input.readlines() 
    read = [i.replace('\n','') for i in read]
    # print(read)

    score = []
    # points = 0
    # for number in read:
        # print(number)
        # if  "C" in number:
            # points += scissors
    
    # print(points)

def game(games):
    points = 0
    for n in games:
        # print(points)
        # print(n)
        if "A" in n and "X" in n:
            points += Z
            points += lose
        elif "B" in n and "X" in n:
            points += X
            points += lose
        elif "C" in n and "X" in n:
            points += Y
            points += lose
        elif "A" in n and "Y" in n:
            points += X
            points += draw
        elif "B" in n and "Y" in n:
            points += Y
            points += draw 
        elif "C" in n and "Y" in n:
            points += Z
            points += draw
        elif "A" in n and "Z" in n:
            points += Y
            points += win
        elif "B" in n and "Z" in n:
            points += Z
            points += win
        elif "C" in n and "Z" in n:
            points += X
            points += win



    print(points)




game(read)