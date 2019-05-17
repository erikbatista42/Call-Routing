
'''
*************************************************
*    Title: Creating a dictionary from a .txt file using Python
*    Author: miloJ
*    Date: 2017
*    Code version: python 3
*    Availability: https://stackoverflow.com/questions/17714571/creating-a-dictionary-from-a-txt-file-using-python
*****************************************************
'''
# Reading file and putting into dictionary => O(n+k+k) -> O(n^3) 
def CheckPrice(spreadsheet, number):
    num_dict = []
    # O(n) because we are iterating throught each line
    # read spreadsheet and put it in dictionary
    with open(spreadsheet, 'r') as cost_file:
            for line in cost_file:
                elements = line.rstrip().split(",")
                num_dict.append((dict(zip(elements[::2], elements[1::2])))) # O(k+K) k is the slice size. The zip is an O(1) operation.
    

    # BEST + WORST: O(n^2) - because we have two iterations whih both takes n time 
    # write the number taken and the price in output.txt  
    output_file = open("output.txt", "a") 
    for i in num_dict: # O(n) - iterate through n dictionaries
        for key, value in i.items(): # O(n) - have to go through n entries to find
            if key == number: # O(1)
                output_file.write("\nNUM: {}   COST: {}".format(key,value))
                output_file.close
            
    
if __name__ == "__main__":
    CheckPrice("costs-10.txt", "+449916707")




    




    