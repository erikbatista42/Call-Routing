
class TrieNode():

    def __init__(self, data):
        self.data = data
        # make 10 children nodes because 0-9 digits
        self.children = [for node in range(10)]


class TrieTree():

    def __init__(self):
        self.root = TrieNode("*")


if __name__ == "__main__":
    print(123)