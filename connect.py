import pymongo
url="mongodb://localhost:27017"
c = pymongo.MongoClient(url)
db = c["college"]
coll = db["studlist"]

print("\n\nQ1:\n")
for x in coll.find({"gender":"female","course":"MCA"},{"_id":0,"name.fname":1,"name.lname":1,"course":1,"gender":1}):
	print(x)

print("\n\nQ2:\n")
for x in coll.find({"gender":"male","grade":"A+"},{"_id":0,"name.fname":1,"name.lname":1,"grade":1,"gender":1}):
	print(x)

print("\n\nQ3:\n")
for m in coll.find({"course":"MCA"}).sort("mark",-1).limit(1):
	print(m)

print("\n\nQ4:\n")
for s in coll.find().sort("course","Mechanical").sort("mark",-1).limit(3):
	print(s)

print("\n\nQ5:\n")
for i in coll.find({"gender":"female"},{"_id":0,"name.fname":1,"name.lname":1,"mark":1}):
	print(i)

print("\n\nQ6:\n")
for i in coll.find({"mark":{'$gt':80,'$lt':90}},{"_id":0,"name.fname":1,"name.lname":1,"course":1,"mark":1}):
	print(i)

print("\n\nQ7:\n")
for i in coll.find({"name.fname":{'$regex': '^V'}},{"_id":0,"name.fname":1,"name.lname":1}):
	print(i)

print("\n\nQ8:\n")
for x in coll.find({"address.city":"Kollam"},{"_id":0,"name.fname":1,"address.city":1}):
	print(x)

print("\n\nQ9:\n")
for x in coll.find({'$nor':[{"address.city":'Kollam'},{"address.city":'Thiruvananthapuram'}]},{"_id":0,"name.fname":1,"address.city":1}):
	print(x)

print("\n\nQ10:\n")

for x in coll.find({"gender":"female",'$nor':[{"address.city":'Kollam'},{"address.city":'Thiruvananthapuram'}]},{"_id":0,"name.fname":1,"address.city":1,"gender":1}):
	print(x["name"]["fname"])

