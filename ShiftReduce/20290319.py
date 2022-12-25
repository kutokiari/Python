table = [
["S5"," " ," " ,"S4"," " ," ","1","2","3"],
[" " ,"S6"," " ," " ," "  ,"ACCEPT"," "," "," "],
[" " ,"R2","S7"," " ,"R2" ,"R2"," "," "," " ],
[" " ,"R4","R4"," " ,"R4" ,"R4"," "," "," "],
["S5"," " ," " ,"S4"," "  ," ","8","2","3"],
[" " ,"R6","R6"," " ,"R6" ,"R6"," "," "," "],
["S5"," " ," " ,"S4"," "  ," "," ","9","3"],
["S5"," " ," " ,"S4"," "  ," "," "," ","10"],
[" " ,"S6"," " ," " ,"S11"," "," "," "," ",],
[" " ,"R1","S7"," " ,"R1" ,"R1"," "," "," "],
[" " ,"R3","R3"," " ,"R3" ,"R3"," "," "," "],
[" " ,"R5","R5"," " ,"R5" ,"R5"," "," "," "],
]
element_dict = {"id" : 0 , "+" : 1 , "*" : 2 , "(" : 3 , ")" : 4 , "$" : 5 , "E" : 6 , "T" : 7 , "F" : 8}
string_input = input("Enter your string:")
string_input = string_input + "$"
string_action = ""
string_stack = "0"
string_list = list()
last_digit = 0
for i in string_input:
    if i == 'i':
        string_list.append("id")
    elif i == 'd':
        continue
    else:
        string_list.append(i)
string_list.append("$")

#For the initializing and defining string_action for the first time.
def initial():
    global string_input
    global string_action
    global string_stack
    global string_list
    global last_digit
    if string_list[0] == 'id':
        string_action = table[last_digit][element_dict["id"]]
    elif string_list[0] == '(':
        string_action = table[last_digit][element_dict["("]]
    else:
        print("INVALID string entered. SYNTAX ERROR!")
        quit()
    #print(string_stack,"\t",string_input,"","\t",string_action)   Printing statement              

def shift_():
    global string_input
    global string_action
    global string_stack
    global string_list
    global last_digit
    if string_action[0] == "S":
        last_digit = string_action[1:]
        string_stack = string_stack + str(string_list[0]) + last_digit
        last_digit = int(last_digit)
        if string_list[0] == "id":
            string_input = string_input[2:]
        else:
            string_input = string_input[1:]
    elif string_action == " ":
        print("INVALID string entered. SYNTAX ERROR!")
        quit()
    string_list.pop(0)
    string_action = table[last_digit][element_dict[string_list[0]]]
    #print(string_stack,"\t",string_input,"","\t",string_action)   Printing statement
    
    
def reduce_():
    global string_input
    global string_action
    global string_stack
    global string_list
    global last_digit
    if string_action[1] == "1":              #REDUCE 1   E -> E + T
        e_temp = string_stack.rfind('E')
        op_temp = string_stack.rfind('+')
        t_temp = string_stack.rfind('T')
        if t_temp > op_temp > e_temp:
            string_stack = string_stack[:e_temp + 1]
            temp = int(string_stack[e_temp - 1])
            temp_ = table[temp][element_dict["E"]]
            string_stack = string_stack + temp_
            last_digit = int(temp_)
            string_action = table[last_digit][element_dict[string_list[0]]]
            #print(string_stack,"\t",string_input,"","\t",string_action)   Printing statement
        else:
            print("INVALID string entered. SYNTAX ERROR!")
            quit()
    
    
    elif string_action[1] == "2":          #REDUCE2    E -> T
        t_temp = string_stack.rfind("T")
        string_stack = string_stack[:t_temp]
        string_stack = string_stack + "E"
        temp = int(string_stack[t_temp - 1])
        temp_ = table[temp][element_dict["E"]]
        string_stack = string_stack + temp_
        last_digit = int(temp_)
        string_action = table[last_digit][element_dict[string_list[0]]]
        #print(string_stack,"\t",string_input,"","\t",string_action)   Printing statement


    elif string_action[1] == "3":            #REDUCE3      T -> T * F
            t_temp = string_stack.rfind("T")
            op_temp = string_stack.rfind("*")
            f_temp = string_stack.rfind("F")
            if f_temp > op_temp > t_temp:
                string_stack = string_stack[:t_temp +1]
                temp = int(string_stack[t_temp -1])
                temp_ = table[temp][element_dict["T"]]
                string_stack = string_stack + temp_
                last_digit = int(temp_)
                string_action = table[last_digit][element_dict[string_list[0]]]
                #print(string_stack,"\t",string_input,"","\t",string_action)   Printing statement
            else:
                print("INVALID string entered. SYNTAX ERROR!")
                quit()
    
    
    elif string_action[1] == "4":             #REDUCE4   T -> F
        f_temp = string_stack.rfind("F")
        string_stack = string_stack[:f_temp]
        string_stack = string_stack + "T"
        temp = int(string_stack[f_temp - 1])
        temp_ = table[temp][element_dict["T"]]
        string_stack = string_stack + temp_
        last_digit = int(temp_)
        string_action = table[last_digit][element_dict[string_list[0]]]
        #print(string_stack,"\t",string_input,"","\t",string_action)   Printing statement
    
    
    elif string_action[1] == "5":             #REDUCE5    F -> (E)
        a_temp = string_stack.rfind("(")
        e_temp = string_stack.rfind("E")
        k_temp = string_stack.rfind(")")
        if k_temp > e_temp > a_temp:
            string_stack = string_stack[:a_temp]
            string_stack = string_stack +"F"
            temp = int(string_stack[a_temp -1])
            temp_ = table[temp][element_dict["F"]]
            string_stack = string_stack + temp_
            last_digit = int(temp_)
            string_action = table[last_digit][element_dict[string_list[0]]]
            #print(string_stack,"\t",string_input,"","\t",string_action)   Printing statement
        else:
            print("INVALID string entered. SYNTAX ERROR!")
            quit()        
    
    
    else:          #REDUCE6    F -> id
        i_temp = string_stack.rfind("i")
        string_stack = string_stack[:i_temp]
        string_stack = string_stack + "F"
        temp = int(string_stack[i_temp - 1])
        temp_ = table[temp][element_dict["F"]]
        string_stack = string_stack + temp_
        last_digit = int(temp_)
        string_action = table[last_digit][element_dict[string_list[0]]]
        #print(string_stack,"\t",string_input,"","\t",string_action)   Printing statement




initial()
while(string_action != "ACCEPT"):
    if string_action[0] == "S":
        shift_()
    elif string_action[0] == "R":
        reduce_()
    else:
        print("INVALID string entered. SYNTAX ERROR!")
        quit() 
print("VALID string entered. ACCEPTED!")