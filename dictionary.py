aDictionary={
    'Sam':'+91-98345-87456',
    'Ram':'+91-99330-20202',
    'Som':'+91-96478-38682'
}
bDictionary={
    1:'ONE',
    2:'Two',
    3:'Three',
    4:aDictionary
}
print(aDictionary)

#dict_items
print(aDictionary.items())
#dict_keys
print(aDictionary.keys())
#dict_value
print(aDictionary.values())

#print single item_values
print(aDictionary.get('Som'))
#Add multiple values of a key
aDictionary['Sam']={'phNo':'987654321','mail':'SamMail@info.com','DOB':'14-12-2000','BloodGroup':'O-ve'}
aDictionary['Mun']=35,36,37,28,10
print(aDictionary['Mun'])

# REmove something from the dictionary
print(aDictionary)
aDictionary.pop('Mun') # del aDictionary['Mun']
print(aDictionary)
print(aDictionary.popitem())
print(aDictionary)
del aDictionary['Sam']['DOB']
print(aDictionary)

# Clear the whole dictionary
aDictionary.clear()
print(aDictionary)

print(bDictionary)
