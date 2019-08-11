from basicModelApp import db, Puppy

db.create_all() #create all the tables

sam = Puppy('sammy', 3)
frank = Puppy('frankie', 2)

print(sam.id) # we should see None
print(frank.id) # None here too, no ids yet

db.session.add_all([sam,frank])
db.session.commit()

print(sam.id) # we should see ids now
print(frank.id)