# Define a procedure, stamps, which takes as its input a positive integer in
# pence and returns the number of 5p, 2p and 1p stamps (p is pence) required
# to make up that value. The return value should be a tuple of three numbers
# (that is, your return statement should be followed by the number of 5p,
# the number of 2p, and the nuber of 1p stamps).
#
# Your answer should use as few total stamps as possible by first using as
# many 5p stamps as possible, then 2 pence stamps and finally 1p stamps as
# needed to make up the total.
#
# (No fair for USians to just say use a "Forever" stamp and be done with it!)
#

def stamps(amount):
    # Your code here
    fives = amount // 5
    twos = (amount - (5*fives)) // 2
    ones = (amount - (5*fives) - (2*twos)) // 1
    return fives, twos, ones


####################
#      TESTS       #
####################
print(stamps(8))
print(stamps(5))
print(stamps(29))
print(stamps(0))