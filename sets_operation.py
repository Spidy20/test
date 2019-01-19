thisset = {"apple", "banana", "cherry"}
print(thisset)
#
# ##Add method-add new member in set
thisset.add(15)
print('after add',thisset)
#
##remove -remove a specified item,but it will raise error if specified item not in the set
thisset.remove("banana")
print('after removing',thisset)
#
# ###discard method also remove the item but it will not raise the error if the item not in the set
thisset.discard('kk')
print('after discard',thisset)
#
# ####POP-it remmove any item from set because set is unordered
thisset.pop()
print('after pop',thisset)
#
###diffrence-give the diffrence between values in set
x = {"apple", "google", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print('diffrence-',z)
#
# ###Diffrence update-method removes the items that exist in both sets
x.difference_update(y)
print('diffrence update',x)
#
# ###Intersection-return the same itemm which are exists in both sets
a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}
c = a.intersection(b)
print('intersection',c)
#
# ###intersection_update-Remove the items that is not present in both x, and set y
a.intersection_update(b)
print('intersection_update',a)
#
####Issubset-if d values are in e sets than its show True
d = {"a", "b", "c"}
e = {"f", "e", "d", "c", "b", "a"}
f = d.issubset(e)
print('issubset-',f)
#
# ###Isusperset-True if all items set y are present in set x
g=d.issuperset(e)
print('issuperset-',g)

#isdisjoint-Return True if no items in set x is present in set y
x1 = {"apple", "banana", "cherry"}
y1 = {"google", "microsoft", "facebook"}
#
z = x1.isdisjoint(y1)
print('isdisjoint',z)

###symmetric_difference-return the diffrent items from diffrent set
x2 = {"apple", "banana", "cherry"}
y2 = {"google", "microsoft", "apple"}
#
z1= x2.symmetric_difference(y2)
print('symmetric_difference',z1)
#

###symmetric_difference_update-Remove the items that are present in both sets
x2.symmetric_difference_update(y2)
print('symmetric_difference_update',x2)
#
# ####Union-Return a set that contains all items from both sets
x3 = {"apple", "banana", "cherry"}
y3 = {"google", "microsoft", "apple"}

z3 = x3.union(y3)
print('after union',z3)
#
# ###Update-Insert the items from set y into set x
x3.update(y3)
print('after update',x3)