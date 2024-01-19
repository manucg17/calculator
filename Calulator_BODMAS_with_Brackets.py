## Calulator using BODMAS using Brackets

def number_listing(input_str):
    current_number = ""
    numbers = []
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
    print(f"Numbers used here are :\n{numbers}")
    return numbers

def operator_listing(input_str):
    current_operator = ""
    operators = []
    (sub,add,mul,div) = (0,0,0,0)
    for i in range (len(input_str)):
        if(input_str[i] == '/'):
            operator_check(i,input_str,operators,current_operator)
            div = div + 1
        elif(input_str[i] == '*'):
            operator_check(i,input_str,operators,current_operator)
            mul = mul + 1
        elif(input_str[i] == '+'):
            operator_check(i,input_str,operators,current_operator)
            add = add + 1
        elif(input_str[i] == '-'):
            operator_check(i,input_str,operators,current_operator)
            sub= sub + 1
    print("Arithmetic operators used:", operators)
    print (f"Sub -> {sub}\nAdd -> {add}\nMul -> {mul}\nDiv -> {div}\n ")
    return operators,sub,add,mul,div

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
    continue_flag = True
    # for i in range(0,len(operators)): ===> Cannot use For --> since this value will not change even if length varies within the loop, so while is used.
    while continue_flag == True:
        i = 0
        while i < len(operators):
            print(f"index value of operators in Calculate is {i}\n")
            print(f"value of Sub:{sub}\n")
            print(f"value of Add:{add}\n")
            print(f"value of Mul:{mul}\n")
            print(f"value of Div:{div}\n")
            if operators[i] == "/":
                print(f"Current Index value: {i}, {numbers[i]}/{numbers[i+1]}")
                print(f"{len(operators)}")
                if (numbers[i+1] == 0):
                    print(f"Number cannot be divided by {numbers[i+1]}")
                    divbyzero = True 
                    break
                result = numbers[i]/numbers[i+1]
                print(f"{numbers} --> Calculate Fn --> before update list function\n")
                numbers= update_list(i,numbers,operators,result)
                print(f"{numbers} --> Calculate Fn --> After update list function\n")
                div = div-1
                i = i-1
                print(f"Division reduced to: {div}\nNew length of Operators: {len(operators)}\nRemaining Operators in the List: {operators}")
                if div == 0:
                    continue_flag = True
                    break
            elif div == 0 and operators[i] == "*":
                print(f"Current Index value: {i}, {numbers[i]}*{numbers[i+1]}")
                print(f"{len(operators)}")
                result = numbers[i]*numbers[i+1]
                numbers= update_list(i,numbers,operators,result)
                mul = mul-1
                i = i-1
                print(f"Multiplication reduced to: {mul}\nNew length of Operators: {len(operators)}\nRemaining Operators in the List: {operators}")
                if mul == 0:
                    continue_flag = True
                    break
            elif div == 0 and mul == 0 and operators[i] == "+":
                print(f"Current Index value: {i}, {numbers[i]}+{numbers[i+1]}")
                print(f"{len(operators)}")
                result = numbers[i]+numbers[i+1]
                print(f"{numbers} --> Calculate Fn --> before update list function\n")
                numbers= update_list(i,numbers,operators,result)
                print(f"{numbers} --> Calculate Fn --> After update list function\n")
                add = add-1
                i = i-1
                print(f"Addition reduced to: {add}\nNew length of Operators: {len(operators)}\nRemaining Operators in the List: {operators}")
                if add == 0:
                    continue_flag = True
                    break
            elif div == 0 and mul == 0 and add == 0 and operators[i] == "-":
                print(f"Current Index value: {i}, {numbers[i]}-{numbers[i+1]}")
                print(f"{len(operators)}")
                result = numbers[i]-numbers[i+1]
                numbers= update_list(i,numbers,operators,result)
                sub = sub-1
                i = i-1
                print(f"Subtraction reduced to: {sub}\nNew length of Operators: {len(operators)}\nRemaining Operators in the List: {operators}")
                if sub == 0:
                    continue_flag = False
                    break
            i = i+1
            print(f"value of index {i} --After-- while loop\n")       
    return result,divbyzero

input_str= input("Enter the Equation to be calculated without Brackets:\n")
if input_str[0] == "-":
    input_str = str(0) + input_str
elif input_str[0] == "+":
    input_str = str(0) + input_str

# Initialize variables
current_number = ""
numbers = []
divbyzero = False

# Initialize operators
current_operator = ""
operators = []
(sub,add,mul,div) = (0,0,0,0)

#Splitting Numbers and Operators to separate Lists
numbers = number_listing(input_str)
operators,sub,add,mul,div = operator_listing(input_str)

Result, divbyzero = calculate(numbers,operators,sub,add,mul,div)
if divbyzero:
    print(f"Unexpected input resulting in division by zero")
else:
    print(f"\n")
    print(format("****","*^22"))
    print(f"Solving Equation:\n{input_str} = {Result}")
    print(format("****","*^22"))
    print(f"\n")