# hashtable
from hashtable import HashTable
from time import time

class CheckPrice(object):

    def __init__(self, file_path):
        # instance variables
        self.number_and_cost = self.store_routes_cost(file_path)

    # store cost of routes into the hash table
    def store_routes_cost(self, file_path):
        hash_cost_route = HashTable(100000)  # O(n) space complexity
        with open(file_path, "r") as file:
            for line in file:  # O(n) time complexity
                line = line[:-1]
                # split the incoming route and cost
                route_cost = line.split(",")
                # store the route and cost into it's own variable
                route = route_cost[0]
                cost = route_cost[1]
                # check if the route is already in our hashtable O(1)
                if hash_cost_route.contains(route):
                    old_cost = hash_cost_route.get(route)
                    if old_cost > cost:  # check if the cost already in greater than the new cost coming in
                        hash_cost_route.set(route, cost)  # O(1)
                else:
                    hash_cost_route.set(route, cost)  # O(1)
        return hash_cost_route

    # find cost of the phone number input
    def find_cost(self, phone_number):
        for _ in range(len(phone_number)-1):  # O(n) time complexity
            if self.number_and_cost.contains(phone_number):
                # O(1) space complexity
                return self.number_and_cost.get(phone_number)
            else:
                phone_number = phone_number[:len(phone_number)-1]
        return 0

    # write to a new file function
    def write_results(self, phone_number, cost):
        with open("call-costs-2.txt", "a") as file:
            file.write("NUM: {}, COSTS: {}\n".format(phone_number, cost))


if __name__ == "__main__":
    start_timer = time()
    print("Working over time, I better get paid...")
    file_path = "route-costs-106000.txt"  # 10600 routes with costs
    check_price = CheckPrice(file_path)
    print("This took {}".format(round(time() - start_timer, 4)))
    start_second_timer = time()
    with open("phone-numbers-10000.txt", "r") as file:  # file for the 10000 numbers
        for phone_number in file:
            phone_number = phone_number[:-1]
            cost = check_price.find_cost(phone_number)
            check_price.write_results(phone_number, cost)
    print("Finding cost took: {}".format(round(time() - start_second_timer, 4)))