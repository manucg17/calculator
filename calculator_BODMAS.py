## Calulator using BODMAS 
def operator_check(index_opchk,input_strng,op_check,current_opchk):
    current_opchk = input_strng[index_opchk]
    op_check.append(current_opchk)
    current_opchk = ""
    
def update_list(index_val,number_val,operator_val,result_val):
    popped_operator_at_index = operator_val.pop(index_val)
    # Specify the indices for the split
    split_index = index_val
    # Use slicing to create two new lists
    numbers_prt1 = number_val[:split_index]
    numbers_prt2 = number_val[split_index+2:]
    # Appending new result into number list after popping used numbers
    numbers_prt1.append(result_val)
    number_val = numbers_prt1+ numbers_prt2
    print(f"{number_val} --> output of update list function\n")
    return number_val

def calculate(numbers,operators,sub,add,mul,div):
    result = 0
    i = 0
    divbyzero=False
    # for i in range(0,len(operators)): ===> Cannot use For --> since this value will not change even if length varies within the loop, so while is used.
    while i < len(operators):
        print(f"index value of operators in Calculate is {i}\n")
        if operators[i] == "/":
            print(f"{i} is the index value, {numbers[i]}/{numbers[i+1]}")
            print(f"{len(operators)}")
            if (numbers[i+1] == 0):
                print(f"Number cannot be divided by {numbers[i+1]}")
                divbyzero = True 
                break
            result = numbers[i]/numbers[i+1]
            print(f"{numbers} --> Caluculate Fn --> before update list function\n")
            numbers= update_list(i,numbers,operators,result)
            print(f"{numbers} --> Caluculate Fn --> After update list function\n")
            div = div-1
            i = i-1
            print(f"division reduced to: {div}\nlength of operators is {len(operators)}\n remaining operators are {operators}")
        elif div == 0 and operators[i] == "*":
            print(f"{i} index, {numbers[i]}*{numbers[i+1]}")
            print(f"{len(operators)}")
            result = numbers[i]*numbers[i+1]
            numbers= update_list(i,numbers,operators,result)
            mul = mul-1
            i = i-1
            print(f"multiplication reduced to:{mul}\nlength of operators is {len(operators)}\n remaining operators are {operators}")
        elif div == 0 and mul == 0 and operators[i] == "+":
            print(f"{i} index, {numbers[i]}+{numbers[i+1]}")
            print(f"{len(operators)}")
            result = numbers[i]+numbers[i+1]
            print(f"{numbers} --> Caluculate Fn --> before update list function\n")
            numbers= update_list(i,numbers,operators,result)
            print(f"{numbers} --> Caluculate Fn --> After update list function\n")
            add = add-1
            i = i-1
            print(f"addition reduced to:{add}\nlength of operators is {len(operators)}\n remaining operators are {operators}")
        elif div == 0 and mul == 0 and add == 0 and operators[i] == "-":
            print(f"{i} index, {numbers[i]}-{numbers[i+1]}")
            print(f"{len(operators)}")
            result = numbers[i]-numbers[i+1]
            numbers= update_list(i,numbers,operators,result)
            sub = sub-1
            i = i-1
            print(f"subtraction reduced to:{sub}\nlength of operators is {len(operators)}\n remaining operators are {operators}")
        i = i+1
        print(f"{i} value of i --After-- while loop\n")
    return result,divbyzero

input_str= input("Enter the Equation to be calculated without Brackets:\n")

# Initialize variables
current_number = ""
numbers = []
divbyzero = False
if input_str[0].isdigit() and input_str[-1].isdigit():
    for char in input_str:
        if char.isdigit():
            current_number += char
        elif current_number:
            numbers.append(int(current_number))
            current_number = ""
    # Add the last number if there is one
    if current_number:
        numbers.append(int(current_number))
else:
    print(f"Entered Equation should Start or End with a digit. Please Verify Input --> {input_str}\n")
    exit(-1)
print("Numbers used here are    :", numbers)

# Initialize operators
current_operator = ""
operators = []
(sub,add,mul,div) = (0,0,0,0)

for i in range (len(input_str)):
    if(input_str[i] == '-'):
        operator_check(i,input_str,operators,current_operator)
        sub= sub + 1
    elif(input_str[i] == '+'):
        operator_check(i,input_str,operators,current_operator)
        add = add + 1
    elif(input_str[i] == '*'):
        operator_check(i,input_str,operators,current_operator)
        mul = mul + 1
    elif(input_str[i] == '/'):
        operator_check(i,input_str,operators,current_operator)
        div = div + 1
print("Arithmetic operators used:", operators)
print (f"Sub -> {sub}\nAdd -> {add}\nMul -> {mul}\nDiv -> {div}\n ")

Result, divbyzero = calculate(numbers,operators,sub,add,mul,div)
if divbyzero:
    print(f"Unexpeted input resulting in division by zero")
else:
    print(f"Output for {input_str}: {Result}")
    