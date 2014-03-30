from app import app
from flask import render_template
from app import collection




#dummy data for testing against db
known_good= [

{
   "_id": 1,
    "name": "John Doe",
    "id": 2,
    "date_of_birth": "1/2/1972",
    "ins": "blue cross"
},
{
   "_id": 2,
    "name": "Jane Doe",
    "id": 2,
    "date_of_birth": "1/2/1973",
    "ins": "green cross"
},
{
   "_id": 3,
    "name": "Bill Doed",
    "id": 2,
    "date_of_birth": "1/2/1974",
    "ins": "that other one"
},
{
   "_id": 4,
    "name": "John Doe",
    "id": 2,
    "date_of_birth": "1/2/1975",
    "ins": "orange cross"
},

]

@app.route('/')
@app.route('/index')
def index():
  #db insert test
  item_dict = {}
  item_list = []
  results = []

  item=collection.find()
  print type(item)

  for i in item:
    item_list.append(i)

  print "len of item_list is:", len(item_list)
  for record in known_good:
    for i in item_list:
      if record["_id"] == i["_id"]:
        # ids match. now check everything else
        if record == i:
          results.append([i,True])
        else:
          results.append([i,False])

  for item in results:
    print item
  # for key,value in item_dict.iteritems():
  #   print "key", key
  #   print "value", value

  #return "hi"
  return render_template("index.html",data=results)
