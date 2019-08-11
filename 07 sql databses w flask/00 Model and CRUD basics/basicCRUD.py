from basicModelApp import db, Puppy

## create
my_puppy = Puppy('Rufus', 5)
db.session.add(my_puppy)
db.session.commit()

## read
all_puppies = Puppy.query.all() #list of Puppy objects in the table
print(all_puppies)

## select by id
puppy_one = Puppy.query.get(1) # this databases IDs start at 1 not 0
print(puppy_one.name)

## filter
puppy_frank = Puppy.query.filter_by(name='frankie')
print(puppy_frank.all()) # print a list with all the puppies named 'frankie'

## update
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()

## delete
second_pup = Puppy.query.get(2)
db.session.delete(second_pup)
db.session.commit()

## print all
all_puppies = Puppy.query.all() #list of Puppy objects in the table
print(all_puppies)
