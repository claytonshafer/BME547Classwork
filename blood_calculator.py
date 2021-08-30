def interface():
    print("Blood calculator")
    keep_running = True
    while keep_running: 
        print("Make a choice")
        print("9 - Quit")
        choice = input("Make a choice: ")
        if int(choice) == 9:
            keep_running = False
        elif int(choice) == 1:
            HDL_Driver()
        elif int(choice) == 2:
            LDL_Driver()
    print(choice)
    return choice



def LDL_Driver():
    LDL_value = ldl_input()
    LDL_character = ldl_analysis(LDL_value)
    ldl_output(LDL_value, LDL_character)

def ldl_input():
    ldl_value = int(input(("Enter LDL Value: ")))
    return ldl_value

def ldl_analysis(LDL_value):
    if LDL_value <= 130:
        return "Normal"
    elif 131 <= LDL_value < 160:
        return "Borderline high"
    elif 161 <= LDL_value < 190:
        return "High"
    else:
        return "Extremely high"

def ldl_output(LDL_value, LDL_answer):
    print("The LDL value of {} is considered {}".format(LDL_value, LDL_answer))
    return


def HDL_Driver():
    HDL_value = hdl_input()
    HDL_character = hdl_analysis(HDL_value)
    hdl_output(HDL_value, HDL_character)

def hdl_input():
    hdl_value = int(input(("Enter HDL Value: ")))
    return hdl_value

def hdl_analysis(HDL_value):
    if HDL_value >= 60:
        return "Normal"
    elif 40 <= HDL_value < 60:
        return "Borderline low"
    else:
        return "Low"

def hdl_output(HDL_value, HDL_answer):
    print("The HDL value of {} is considered {}".format(HDL_value, HDL_answer))
    return

interface()
