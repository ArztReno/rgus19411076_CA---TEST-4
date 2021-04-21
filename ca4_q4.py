'''
nci programme: BSHDS 
program: pointer class with its instances pickled
author: Renato Gusani
studentID: x19411076
date: 06/05/2020

'''
# creating the pointer class
import pickle # package to serialize and deserialize the list of Point instances.
class Point:

    def __init__(self, x=0, y=0):
    # coordinates set to x and y 
        self.x = x
        self.y = y

    def range_from_pointer(self):
    # Computes the range from the pointer
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

# these are the instances for the point class
p = Point(1, 3)
p.x
p.y
p.range_from_pointer()
q = Point(8, 11)
q.x
q.y
q.range_from_pointer()
r = Point()
r.x
r.y
r.range_from_pointer()

# putting the instances into a list
instances = {1:"1, 3",2:"8, 11"}

# pickling the list
pickle_out = open("instances.pickle","wb")
pickle.dump(instances, pickle_out)
pickle_out.close()

# opening the pickled instances and loading onto var
pickle_in = open("instances.pickle","rb")
instances = pickle.load(pickle_in)

# shows what is retained the intances data-type.
print(instances)
print(instances[2])