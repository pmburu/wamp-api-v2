# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

def difference (list1, list2):
   list_dif = [i for i in list1 + list2 if i not in list2]
   return list_dif

# Initializing list 1 and list 2
all_drivers = [10, 15, 20, 25, 30, 35, 40]
allocated_drivers = [25]

print ("List of all drivers: " + str(all_drivers))
print ("List of allocated drivers: " + str(allocated_drivers))

# Take difference of list 1 and list 2
z = difference (all_drivers, allocated_drivers)

print("Remaining drivers: " + str(z))

# if lists are equal
if not z:
    print("First and Second list are Equal")
# if lsts are not equal
else:
    print("First and Second list are Not Equal")

# https://www.geeksforgeeks.org/randomly-select-n-elements-from-list-in-python/
