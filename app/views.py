from app import app
from flask import render_template
from app import collection





known_good= {
   "_id": 1,
    "name": "John Doe",
    "id": 2,
    "date_of_birth": "1/2/1972",
    "ins": "blue cross"
}



@app.route('/')
@app.route('/index')
def index():
  #db insert test
  item_dict = {}
  item=collection.find()
  for i in item:
    item_dict = i
  equal = False
  if item_dict == known_good:
    print "equal"
    equal = True

  # for key,value in item_dict.iteritems():
  #   print "key", key
  #   print "value", value

  return render_template("index.html",data=item_dict,equals=equal)
