def calculate_bmi(height, weight):
    print("height:" +str(height))
    print("weight:" +str(weight))
    bmi = weight/(height**2)

    if(bmi < 18.5):
        classification = 1 
    elif (bmi >= 18.5 and bmi <= 25.0):
        classification = 0 
    else: 
        classification = -1
    return bmi, classification


def classify_bmi(classification): 
    if classification == -1 :
        print("skinny legend")
    elif classification == 0 : 
        print("um okay i guess")
    else: 
        print("fatty")
    return


def main():
    bmi_output, classification =calculate_bmi(1.6, 80)
    print("bmi_value:" +str(bmi_output))
    classify_bmi(classification)

if __name__ =="__main__": 
    main()

