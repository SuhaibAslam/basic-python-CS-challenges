# Question 9: Deep Reverse
# Define a procedure, deep_reverse, that takes as input a list,
# and returns a new list that is the deep reverse of the input list.
# This means it reverses all the elements in the list, and if any
# of those elements are lists themselves, reverses all the elements
# in the inner list, all the way down.

# Note: The procedure must not change the input list.

# The procedure is_list below returns True if
# p is a list and False if it is not.

def is_list(p):
    return isinstance(p, list)

def deep_reverse(lst):
    index = len(lst) - 1
    reversed_list = []
    while index >= 0:
        current_element = lst[index]
        if is_list(current_element):
            reversed_sub_list = deep_reverse(current_element)
            reversed_list.append(reversed_sub_list)
        else:
            reversed_list.append(current_element)
        index -= 1
    return reversed_list



####################
#      TESTS       #
####################

print(deep_reverse([1,2,3,[1,2,3]]))
print(deep_reverse([1, [2, 3, [4, [5, 6]]]]))
print(deep_reverse([1, [2,3], 4, [5,6]]))


