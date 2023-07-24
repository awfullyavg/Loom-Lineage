from app import app
from models import db, User, Family, Loom, Event
from faker import Faker

fake = Faker()

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
                    ),

                User(
                    fname = 'Jennifer',
                    lname = 'Smith',
                    email = 'jennifer.smith@example.com',
                    password = 'jsmith123'
                    ),

                User(
                    fname = 'Matthew',
                    lname = 'Johnson',
                    email = 'matthew.johnson@example.com',
                    password = 'mattPass789'
                    ),

                User(
                    fname = 'Olivia',
                    lname = 'Anderson',
                    email = 'olivia.anderson@example.com',
                    password = 'anderson456'
                    ),
                
                User(
                    fname = 'James',
                    lname = 'Martinez',
                    email = 'james.martinez@example.com',
                    password = 'jmartinez789'
                    ),

                User(
                    fname = 'Emma',
                    lname = 'Thomas',
                    email = 'emma.thomas@example.com',
                    password = 'thomasEmma45'
                    ),

                User(
                    fname = 'Alexander',
                    lname = 'Robinson',
                    email = 'alexander.robinson@example.com',
                    password = 'arobinson123'
                    ),

                User(
                    fname = 'Ava',
                    lname = 'Murphy',
                    email = 'ava.murphy@example.com',
                    password = 'murphyPass567'
                    ),
                
                User(
                    fname = 'Michael',
                    lname = 'Garcia',
                    email = 'michael.garcia@example.com',
                    password = 'garcia1234'
                    ),

                User(
                    fname = 'Charlotte',
                    lname = 'Hall',
                    email = 'charlotte.hall@example.com',
                    password = 'hallChar123'
                    ),

                User(
                    fname = 'Noah',
                    lname = 'Taylor',
                    email = 'noah.taylor@example.com',
                    password = 'taylorNoah789'
                    ),

                User(
                    fname = 'Emily',
                    lname = 'Brown',
                    email = 'emily.brown@example.com',
                    password = 'emilyB5678'
                    ),
                
                User(
                    fname = 'Logan',
                    lname = 'Wang',
                    email = 'logan.wang@example.com',
                    password = 'wangLog456'
                    ),

                User(
                    fname = 'Abigail',
                    lname = 'Gomez',
                    email = 'abigail.gomez@example.com',
                    password = 'gomezAbi567'
                    ),

                User(
                    fname = 'Grace',
                    lname = 'Nguyen',
                    email = 'grace.nguyen@example.com',
                    password = 'nguyenG123'
                    ),

                User(
                    fname = 'Elijah',
                    lname = 'Rodriguez',
                    email = 'elijah.rodriguez@example.com',
                    password = 'eliRod7890'
                    )
                 ]
        db.session.add_all('users')

        families = [
            Family(
            name = 'Doe',
            parents = 'Matthew and Laura',
            partner = 'Emma',
            children = 'Olivia and Liam',
            sibling = 'Jacob'
            ),

            Family(
            name = 'Smith',
            parents = 'David and Jennifer',
            partner = 'Sophia',
            children = 'Noah and Isabella',
            sibling = ''
            ),

            Family(
            name = 'Johnson',
            parents = 'Andrew and Rebecca',
            partner = 'James',
            children = 'Ella, Benjamin, and Mia',
            sibling = 'Lucas'
            ),

            Family(
            name = 'Williams',
            parents = 'Michael and Sarah',
            partner = 'Ethan',
            children = 'Ava and Daniel',
            sibling = 'Emily and Tiffany'
            ),

            Family(
            name = 'Smalls',
            parents = 'Christopher and Jessica',
            partner = 'Christopher',
            children = 'Jacob, Lily, and Sophia',
            sibling = 'William'
            ),

            Family(
            name = 'Brown',
            parents = 'Daniel and Elizabeth',
            partner = 'Aiden',
            children = 'Harper and Caleb',
            sibling = 'Abigail'
            ),

            Family(
            name = 'Murphy',
            parents = 'John and Melissa',
            partner = 'Grace',
            children = '',
            sibling = 'Benjamin'
            ),

            Family(
            name = 'Scott',
            parents = 'Robert and Katherine',
            partner = 'Ella',
            children = 'Jacob and Lily',
            sibling = 'Matteo'
            ),

            Family(
            name = 'Lee',
            parents = 'William and Kayla',
            partner = 'Noah',
            children = 'Emma and Benjamin',
            sibling = 'Ava'
            ),

            Family(
            name = 'Carter',
            parents = 'Matthew and Sarah',
            partner = 'Isabella',
            children = 'Lucas',
            sibling = 'Ella'
            )
        ]


