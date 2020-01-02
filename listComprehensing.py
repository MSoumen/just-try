# we can use  List comprehensing to make list 
names=['kaushik','Kelo','Voga','Maobadi','Protik','Bandoo']
friends=[]
# for people in names:
#     friends.append(people) # for i in range(len(names))-->friends[i]=people
# print(friends)

print([friends for friends in names])

# for people in names:
#     friends.append(people + ' Feeling Good')
# print(friends)

print([friends+' Felling good' for friends in names])

# # Banddooo is a crazy man so he alwayas felling crazy--
# for people in names:
#     if people=='Bandoo':
#         friends.append(people +' feeling Crazy!')
#     else:
#         friends.append(people +' feeling Good!')
# print(friends)

print([friends+' feeling Crazy' for friends in names if friends=='Bandoo'])
