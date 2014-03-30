from app import app
from flask import render_template
from app import collection




#dummy data for testing against db
known_good= [

{
   "_id": 1,
    "name": "John Doe",
    "date_of_birth": "1/2/1972",
    "ins": "blue cross"
},
{
   "_id": 2,
    "name": "Jane Doe",
    "date_of_birth": "1/2/1973",
    "ins": "green cross"
},
{
   "_id": 3,
    "name": "Bill Doed",
    "date_of_birth": "1/2/1974",
    "ins": "that other one"
},
{
   "_id": 4,
    "name": "John Doe",
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
  #fix this to be list comprehension later
  good_results = 0
  bad_results = 0
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
          good_results += 1
        else:
          results.append([i,False])
          bad_results += 1



  return render_template("index.html",data=results,good=good_results,bad=bad_results)
