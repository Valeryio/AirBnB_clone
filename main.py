#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
print("NAME ADDED")
my_model.my_number = 89
print("NUMBER ADDED")
#print(":::::::::::::::::::::::::>>>>>>>>> ", my_model.to_dict())


my_model.save()
print(my_model)