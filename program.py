inp_string = input()
mid_index = len(inp_string)//2
result_str = []
print_cnt = len(inp_string)

def print_result(result_str,print_cnt):
    temp_list = [" "]*(print_cnt-2)
    print("".join(temp_list)+"".join(result_str))


new_str = inp_string[mid_index:]+inp_string[:mid_index]
print(new_str)
str_len = len(new_str)

for i in range(0,str_len):
    print_result(new_str[:(i+1)],(str_len-i+1))

