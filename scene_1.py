# from typing import Tuple


def CheckPrice(spreadsheet, number):
    num_dict = []

    # read spreadsheet and put it in dictionary
    with open(spreadsheet, 'r') as f:
            for line in f:
                elements = line.rstrip().split(",")
                num_dict.append((dict(zip(elements[::2], elements[1::2]))))

    # write the number taken and the price in output.txt  
    g = open("output.txt", "a") 
    for i in num_dict:
        for key, value in i.items():
            if key == number:
                g.write("\nNUM: {}   COST: {}".format(key,value))
                g.close
                print(value)
            
    
if __name__ == "__main__":
    CheckPrice("costs-10.txt", "+449916707")




    