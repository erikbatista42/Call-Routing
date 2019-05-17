# hashtable
import hashtable

class CheckPrice():

    def __init__(self, file_to_read, number, output_file):
        # instance variables
        self.file_to_read = file_to_read
        self.number = number
        self.output_file = output_file
        self.number_and_cost = hashtable.HashTable()

        # read each line in file_to_read and put phone # and cost in a dictionary
        with open(self.file_to_read, "r") as cost_file:
            for line in cost_file:
                elements = line.rstrip().split(",")
                phone_number = elements[::2][0] # key
                new_cost = elements[1::2][0] # value
                if self.number_and_cost.contains(phone_number):
                    old_cost = self.number_and_cost.get(phone_number)
                    if new_cost < old_cost:
                        self.number_and_cost.set(phone_number, new_cost)
                else:
                    self.number_and_cost.set(phone_number, new_cost)

    def price(self):
        # write the number taken and the price in the output file
        with open(self.output_file, "a+") as output_file:
            for key, value in self.number_and_cost.items():
                if self.number == key:
                    output = "\n{} - ${}".format(key,value)
                    output_file.write(output)
                    return output


if __name__ == "__main__":
    check_price = CheckPrice("costs-10.txt", "+4928843955", "output.txt")
    print(check_price.price())
    # table = hashtable.HashTable()




    