from app import app
from models import db, User, Family, Loom, Event
from faker import Faker

fake = Faker()

def create_families():
    families = []
    for _ in range(4):
        f = Family(
            name= fake.name(),
            mother = fake.name(),
            father = fake.name(),
            partner = fake.name(),
            children= fake.name(),
            sibling= fake.name()
        )
        families.append(f)

    return families

if __name__ == '__main__':
    with app.app_context():
        print('clearing db...')
        User.query.delete()
        Family.query.delete()
        Loom.query.delete()
        Event.query.delete()

        print("seeding services")

        users = [
                User(
                    fname = 'John',
                    lname = 'Doe',
                    email = 'john.doe@example.com',
                    password = 'hello123'
                    ),

                User(
                    fname = 'Jane',
                    lname = 'Smith',
                    email = 'jane.smith@example.com',
                    password = 'password123'
                    ),

                User(
                    fname = 'Michael',
                    lname = 'Johnson',
                    email = 'michael.johnson@example.com',
                    password = 'securepass'
                    ),

                User(
                    fname = 'Sarah',
                    lname = 'Williams',
                    email = 'sarah.williams@example.com',
                    password =  'mysecretpass'
                    ),
                
                User(
                    fname = 'David',
                    lname = 'Brown',
                    email = 'david.brown@example.com',
                    password = 'brown1234'
                    )
                 ]
        db.session.add_all(users)

        print('seeding families...')
        families = create_families()
        db.session.add_all(families)
        db.session.commit()


