def calories():
    with open(r"data\day_1 list.txt","r") as file:
        read = file.readlines()
    read = [i.replace("\n", "") for i in read]
    calories = 0
    calories_list = []
    for x in read:

        if x != '':
            calories += int(x)
        else:
            calories_list.append(calories)
            calories = 0
    
    return calories_list



# DriverCode
if __name__ == '__main__':
    print(max(calories()))
    print(sum(calories()[-3:]))

   
   
   
   