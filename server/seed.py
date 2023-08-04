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

        # users = [
        #         User(
        #             fname = 'John',
        #             lname = 'Doe',
        #             email = 'john.doe@example.com',
        #             username = 'johndoe',
        #             password = 'hello123'
        #             ),

        #         User(
        #             fname = 'Jane',
        #             lname = 'Smith',
        #             email = 'jane.smith@example.com',
        #             username = 'janesmith',
        #             password = 'password123'
        #             ),

        #         User(
        #             fname = 'Michael',
        #             lname = 'Johnson',
        #             email = 'michael.johnson@example.com',
        #             username = 'mjohnson',
        #             password = 'securepass'
        #             ),

        #         User(
        #             fname = 'Sarah',
        #             lname = 'Williams',
        #             email = 'sarah.williams@example.com',
        #             username = 'sarawilliams',
        #             password =  'mysecretpass'
        #             ),
                
        #         User(
        #             fname = 'David',
        #             lname = 'Brown',
        #             email = 'david.brown@example.com',
        #             username = 'davidbrown',
        #             password = 'brown1234'
        #             )
        #          ]
        
        user1 = User(
            fname = 'John',
            lname = 'Doe',
            email = 'john.doe@example.com',
            username = 'johndoe',
            _password_hash = 'hello123'
            )

        user2 = User(
                    fname = 'Jane',
                    lname = 'Smith',
                    email = 'jane.smith@example.com',
                    username = 'janesmith',
                    _password_hash = 'password123'
                    )

        user3 = User(
                    fname = 'Michael',
                    lname = 'Johnson',
                    email = 'michael.johnson@example.com',
                    username = 'mjohnson',
                    _password_hash = 'securepass'
                    )

        user4 = User(
                    fname = 'Sarah',
                    lname = 'Williams',
                    email = 'sarah.williams@example.com',
                    username = 'sarawilliams',
                    _password_hash =  'mysecretpass'
                    )
        
        user5 = User(
                    fname = 'David',
                    lname = 'Brown',
                    email = 'david.brown@example.com',
                    username = 'davidbrown',
                    _password_hash = 'brown1234'
                    )

        db.session.add(user1)
        db.session.add(user2)
        db.session.add(user3)
        db.session.add(user4)
        db.session.add(user5)
        # db.session.add_all(users)

        print('seeding families...')
        families = create_families()
        db.session.add_all(families)
        db.session.commit()


