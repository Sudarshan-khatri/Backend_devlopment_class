# what is difference between list ,dictionary,tuple and set with example (create,delete item
# ,access item,add item)
list_item=[1,2,3,3,3,3,4]
print(list_item[0])

def lst_append(list_2,value):
    list_2.append(value)


list_1=[1,2,3,"hi","hello"]
print(lst_append(list_1,"ok"))

tuple_1=(1,2,3,4,5,6,8)
print(type(tuple_1))
print(tuple_1[0])
tuple_2=("hi","hello","hjr")
tuple_3=tuple_1+tuple_2
print(tuple_3)
print(tuple_3)



# create a dictionary
dict_1={
    "name":"sudarshan",
    "cast":"khatri",
    "age":"20",
    "level":"Bachelor"
}
print(dict_1)

# add the dictionary value 
dict_1["color"]="brown_white"
print(dict_1)

# get key from dictionary
x=dict_1.keys()
print(x)
#get values from dictionary
y=dict_1.values()
print(y)

# remove the key and value from dictionary 
dict_1.pop("name")
print(dict_1)

# delete all the keys and values from the dictionary
dict_1.clear()
print(dict_1)



# create the set in python
set_1={1,2,3,4,"bana","papya","hostel"}
print(set_1)

# access the set    
for i in set_1:
    print(i)

# add the set in this list 
set_1.add("hello")
print(set_1)