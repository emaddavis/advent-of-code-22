#get input 
data = open("/home/user/git/advent-of-code-22/01/input.txt")
text = data.read()
data.close()

#convert input data from open() object to nested array 
#wherein the values of the outer array is an elf's holdings 
#and the values of the inner array are the items' Calories
#then find the max by iterating over the outer array while finding the sum of the inner array
arr_1 = text.split('\n\n')
max = 0
for a in arr_1:
    arr_working = a.split('\n')
    arr_working = [int(i) for i in arr_working]
    num = sum(arr_working)
    if num > max:
        max = num

#show result

print(max)