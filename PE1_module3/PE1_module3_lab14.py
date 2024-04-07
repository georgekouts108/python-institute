my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Write your code here.
#

no_dups = []
for ml in my_list:
    if ml not in no_dups:
        no_dups.append(ml)
my_list = no_dups

print("The list with unique elements only:")
print(my_list)
