from app import app
from flask.ext.script import Manager

from faker import Faker
fake = Faker()
import random

from faker.providers import BaseProvider


manager = Manager(app)
insurance_list = ['blue cross','green cross','yellow cross','orange cross','black cross','white cross', ]

# create new provider class
class MyProvider(BaseProvider):
  def insurance(self):
    return insurance_list[random.randint(0,5)]


fake.add_provider(MyProvider)
@manager.command
def test_fake():
  for i in range(10):
    print fake.name()
    print fake.address()
    print fake.insurance()
    print fake.company()
    print

@manager.command
def populate_db():
  pass

if __name__ == "__main__":
  manager.run()
