from typing import Tuple







class CheckPrice():

    def __init__(self, spreadsheet, number):
        self.spreadsheet = spreadsheet
        self.number = number

        self.num_dict = []
        with open(spreadsheet, 'r') as f:
            for line in f:
                elements = line.rstrip().split(",")
                self.num_dict.append((dict(zip(elements[::2], elements[1::2]))))
                # self.num_dict[list(zip(elements[::2]))] = list(zip(elements[1::2]))

    def price(self):
        for i in self.num_dict:
            print(i)
            # if self.number == i[0][0]:
            #     print("found: ", i[1])
            # else:
            #     print("notingggg")

# class TrieNode:

#     def __init__(self, char: str):
#         self.char = char
#         self.children = []
#         # Is it the last character of the word.`
#         self.word_finished = False
#         # How many times this character appeared in the addition process
#         self.counter = 1


class TrieNode(object):
    """
    Our trie node implementation. Very basic. but does the job
    """
    
    def __init__(self, data):
        self.data = data
        self.children = []
        # Is it the last character of the word.`
        self.word_finished = False
        # How many times this character appeared in the addition process
        self.counter = 1

class TrieTree():

    def __init__(self, items=None):
        """Initialize this binary tree node with the given data."""
        self.left = None
        self.right = None

        if items is not None:
            for item in items:
                self.add(item)

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        if self.left is None and self.right is None:
            return True
        else:
            return False
    
    def add(self, root, word):
        node = root
        for char in word:
            found_in_child = False
            # Search for the character in the children of the present `node`
            for child in node.children:
                if child.char == char:
                    # We found it, increase the counter by 1 to keep track that another
                    # word has it as well
                    child.counter += 1
                    # And point the node to the child that contains this char
                    node = child
                    found_in_child = True
                    break
            # We did not find it so add a new chlid
            if not found_in_child:
                new_node = TrieNode(char)
                node.children.append(new_node)
                # And then point node to the new child
                node = new_node
        # Everything finished. Mark it as the end of a word.
        node.word_finished = True

    def find_prefix(self, root, prefix: str) -> Tuple[bool, int]:
        """
        Check and return 
        1. If the prefix exsists in any of the words we added so far
        2. If yes then how may words actually have the prefix
        """
        prefix = str(prefix)
        node = root
        # If the root node has no children, then return False.
        # Because it means we are trying to search in an empty trie
        if not root.children:
            return False, 0
        for char in prefix:
            char_not_found = True
            # Search through all the children of the present `node`
            for child in node.children:
                if child.char == char:
                    # We found the char existing in the child.
                    char_not_found = False
                    # Assign node as the child containing the char and break
                    node = child
                    break
            # Return False anyway when we did not find a char.
            if char_not_found:
                return False, 0
        # Well, we are here means we have found the prefix. Return true to indicate that
        # And also the counter of the last node. This indicates how many words have this
        # prefix
        return True, node.counter

    
if __name__ == "__main__":
    print("")
    root = TrieNode('*')
    add(root, 3476414125)
    add(root, 3476415980)
    add(root, 3476410000)

    trie = TrieTree()

    # test = CheckPrice("costs-10.txt", 347641)
    # print(test.price())
    # print(find_prefix(root, 'hac'))
    print(find_prefix(root, 347641))
    print(root.word_finished)
    # print(find_prefix(root, 'hackathon'))
    # print(find_prefix(root, 'ha'))
    # print(find_prefix(root, 'hammer'))


    