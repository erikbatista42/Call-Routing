
'''
*************************************************
*    Title: Creating a dictionary from a .txt file using Python
*    Author: miloJ
*    Date: 2017
*    Code version: python 3
*    Availability: https://stackoverflow.com/questions/17714571/creating-a-dictionary-from-a-txt-file-using-python
*****************************************************
'''

def CheckPrice(spreadsheet, number):
    num_dict = []

    # read spreadsheet and put it in dictionary
    with open(spreadsheet, 'r') as cost_file:
            for line in cost_file:
                elements = line.rstrip().split(",")
                num_dict.append((dict(zip(elements[::2], elements[1::2]))))
    

    # write the number taken and the price in output.txt  
    output_file = open("output.txt", "a") 
    for i in num_dict:
        for key, value in i.items():
            if key == number:
                output_file.write("\nNUM: {}   COST: {}".format(key,value))
                output_file.close
            
    
if __name__ == "__main__":
    CheckPrice("costs-10.txt", "+449916707")




    




    