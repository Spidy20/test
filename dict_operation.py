thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict['model'])####Access particular value

##Copy
x=thisdict.copy()
print(x)
#
###fromkey - create new dict with same value
y=['key1','key2','key']
z=[0],[1],[2]
new_dict=dict.fromkeys(y,z)
print('new dict',new_dict)
#
# ##GET method
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.get("brand")
print('GET method=',x)
#
###Items
ab=car.items()
print('Items method=',ab)
#
###Keys-return the keys of dictionary
cd=car.keys()
print('keys=',cd)
#
#POP-remove particalar item
# ef=car.pop('model')
# print('After POP=',car)
# #
# ###POPItem-remove the last item
gh=car.popitem()
print('pop item',car)

#####Setdefault-add new key and value
hi= car.setdefault("color", "white")
print(car)

#
# ####Update-insert new key and value
car.update({'top_speed':300})
print('update',car)
#
####VALUES-return values of dictionary
car.values()
print('values are:',car)