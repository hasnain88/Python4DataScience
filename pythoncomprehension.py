# ------------- List Comprehension------------------

l = [1,2,3,4,5,6,7,8,9,10]
l1 = []
for i in l:
    l1.append(i**2)
print(l1)


l2 = [i**2 for i in l]
print(l2)


l3 = [i**2 for i in l if i%2==0]
print(l3)

list1 = ['a','b','c','d','f']
print([i.upper() for i in list1])


# ------------- Tuple Comprehension------------------

print(list(i**2 for i in l))
# ------------- Dictionary Comprehension------------------

d = {"k1":1,"k2":2,"k3":3,"k4":4,"k5":5}
print({k:v**2 for k,v in d.items()})

print({k:v**2 for k,v in d.items() if v>1})

