#print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
def display_main_menu(): 
    print("Enter a number and separate each number with a comma") 
    return

def get_user_input(): 
    temper = input() 
    temper = temper.split(",")
    temper = [float(index) for index in temper]
    print ('temperatures are:' + str(temper))
    return temper

def calc_average(temper_list): 
    total_temp = 0
    for index in temper_list: 
        total_temp = total_temp + index
    avg_temp = total_temp / len(temper_list)
    return avg_temp

def find_min_max(temper_list): 
    min_max_temp = [min(temper_list), max(temper_list)]
    print ("this is [min,max]:", min_max_temp)
    return min_max_temp 

def sort_temp(temper_list): 
    ascending_sorted = sorted(temper_list)
    print ("temperatures in ascending order:", ascending_sorted)
    return ascending_sorted

def calc_median_temperature(temper_list): 
    import statistics 
    median_temp = statistics.median(temper_list)
    print ("the median temp is", median_temp)

display_main_menu()
temper = get_user_input()
print ("average is " + str(calc_average(temper)))
find_min_max(temper)
sort_temp(temper)
calc_median_temperature(temper)