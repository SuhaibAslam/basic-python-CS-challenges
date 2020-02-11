# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a
# list, and returns the element in the list that has the most
# consecutive repetitions. If there are multiple elements that
# have the same number of longest repetitions, the result should
# be the one that appears first. If the input list is empty,
# it should return None.

def longest_repetition(lst):
    if lst == []: return None
    global_repeated_element = 0
    global_number_of_repitions = 0
    local_repeated_element = 0
    local_number_of_repitions = 0
    for idx, element in enumerate(lst):
        if idx == len(lst) - 1:
            return global_repeated_element
        if element == lst[idx+1]:
            local_repeated_element = element
            local_number_of_repitions += 1
        else:
            local_repeated_element = element
            local_number_of_repitions = 1
        if local_number_of_repitions > global_number_of_repitions:
            global_number_of_repitions = local_number_of_repitions
            global_repeated_element = local_repeated_element

####################
#      TESTS       #
####################

print(longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1]))
print(longest_repetition([1, 2, 3, 4, 5]))
print(longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd']))
print(longest_repetition([]))


