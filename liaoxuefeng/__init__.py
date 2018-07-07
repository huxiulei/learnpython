def print_line_separator(remark=''):
    if remark ==  '':
        print(" ")
        print("*" * 30)
        print(" ")
    else:
        print(" ")
        print("*" * 15 , remark , "*" * 15 , sep=" ")