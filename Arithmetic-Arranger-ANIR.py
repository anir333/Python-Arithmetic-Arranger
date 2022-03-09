def arithmetic_arranger(args, calc=False):
    #First: Check length of the problems array given
    if len(args) > 5:
        return 'Error: Too many problems.'

    #Second: Check if the operators are only + or -, then check if the numbers given are only digits and finally check if the length of the numbers given are 4 or less and return an error if not.    
    for i in args:
        [one, operator, two] = i.split(' ')
        if operator != '+' and operator != '-':
            return 'Error: Operator must be \'+\' or \'-\'.'
        elif operator == '+' or operator == '-':
            digits = '1234567890'
            for num in one:
                if num not in digits:
                    return 'Error: Numbers must only contain digits.'
            for num in two:
                if num not in digits:
                    return 'Error: Numbers must only contain digits.'
            else:
                if len(one) > 4 or len(two) > 4:
                    return 'Error: Numbers cannot be more than four digits.'

    
    return formatted(args, calc)


#Third format the operations:
def formatted(args, calc):
    array = []
    top_line = []
    bottom_line = []
    dashes = []
    answers = []

    #Create an array where the values of each operation ar separated: 
    i = 0
    while i < len(args):
        [one, operator, two] = args[i].split(' ')
        array.append([one, operator + two])

        i += 1

    # print(array)
        
    #Create the bottom line of he array with the correspondant separation of each operation:
    for i in array:
        value_length = len(i[1]) - 1
        if len(i[0]) > value_length:
            bottom_line_separation = (len(i[0]) - value_length) + 1
        else:
            bottom_line_separation = 1
        
        if '-' in i[1]:
            bottom_line.append('-' + ' ' * bottom_line_separation + i[1][1:])
        elif '+' in i[1]:
            bottom_line.append('+' + ' ' * bottom_line_separation + i[1][1:])
            
    
    #Create the top line of each operation with its correspondent separation:
    i = 0
    while i < len(bottom_line):
        [one, operator, two] = args[i].split(' ')
        top_line_separation = len(bottom_line[i]) - len(one)
        top_line.append(' ' * top_line_separation + one)
        
        i += 1
        
        
    #Create the dashes under each operation:
    for i in bottom_line:
        dashes.append('-' * len(i))
    
    
    #Store the answers of each operation with their correspondent separation in case the have to be displayed if calc is == True:
    i = 0
    while i < len(args):
        [one, operator, two] = args[i].split(' ')
        dash_len = ''
        if operator == '+':
            answer = (str(int(one) + int(two)))
            dash_len = len(dashes[i]) - len(answer)
            answers.append(' ' * dash_len + answer)
        elif operator == '-':
            answer = (str(int(one) - int(two)))
            dash_len = len(dashes[i]) - len(answer)
            answers.append(' ' * dash_len + answer)
    
        i += 1
    

    #Join all the items of each line with four spaces to display the operations as strings and not as arrays:
    separator = '    ' 
    top_line_joined = separator.join(top_line)
    bottom_line_joined = separator.join(bottom_line)
    dashes_joined = separator.join(dashes)
    answers_joined = separator.join(answers)


    #Print each line of the operation:
    print('Operations arranged: ')
    print(top_line_joined)
    print(bottom_line_joined)
    
    #Return the answers if calc is True:
    if calc == True:
        print(dashes_joined)
        return answers_joined
    else:
        return dashes_joined


print(arithmetic_arranger(['3801 - 2', '123 + 49']))
print(arithmetic_arranger(['1 + 2', '1 - 9380']))
print(arithmetic_arranger(['3 + 855', '3801 - 2', '45 + 43', '123 + 49']))
print(arithmetic_arranger(['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380']))
print(arithmetic_arranger(['44 + 815', '909 - 2', '45 + 43', '123 + 49',
          '888 + 40', '653 + 87']))
print(arithmetic_arranger(['3 / 855', '3801 - 2', '45 + 43', '123 + 49']))
print(arithmetic_arranger(['24 + 85215', '3801 - 2', '45 + 43', '123 + 49']))
print(arithmetic_arranger(['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49']))
print(arithmetic_arranger(['3 + 855', '988 + 40'], True))
print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))
