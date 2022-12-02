#get input 
data = open("/home/user/git/advent-of-code-22/01/input.txt")
text = data.read()
data.close()

#convert input data from open() object to nested array 
#wherein the values of the outer array is an elf's holdings 
#and the values of the inner array are the items' Calories
#then find the max by iterating over the outer array while finding the sum of the inner array
arr_1 = text.split('\n\n')
max_1 = 0
max_2 = 0
max_3 = 0
for a in arr_1:
    arr_working = a.split('\n')
    arr_working = [int(i) for i in arr_working]
    num = sum(arr_working)
    if num > max_1:
        max_1 = num
    elif num > max_2:
        max_2 = num
    elif num > max_3:
        max_3 = num

result = max_1 + max_2 + max_3
#show result

print(result)