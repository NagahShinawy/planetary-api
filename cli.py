from models import db, Planet, User
from config import app   # old

session = db.session


@app.cli.command('db_create')
def create_db():
    db.create_all()
    print("Database created successfully!")


@app.cli.command('db_drop')
def drop_db():
    db.drop_all()
    print("Database dropped")


@app.cli.command('db_seed')
def seed():
    mercury = Planet(
        planet_name="Mercury",
        planet_type="Class D",
        home_star="Sol",
        mass=3.258e23,
        radius=1516,
        distance=35.98e6
    )

    venus = Planet(
        planet_name="Venus",
        planet_type="Class K",
        home_star="Sol",
        mass=4.867e24,
        radius=3760,
        distance=67.24e6
    )

    earth = Planet(
        planet_name="Earth",
        planet_type="Class M",
        home_star="Sol",
        mass=5.972e24,
        radius=3959,
        distance=92.96e6
    )

    john = User(fname='John', lname='Smith', email='john@gmail.com', password='pwd123456')
    leon = User(fname='Leaon', lname='Eric', email='leaon@gmail.com', password='pwd123456')
    session.add(mercury)
    session.add(venus)
    session.add(earth)
    session.add(john)
    session.add(leon)
    session.commit()  # saving changes to db
    print("Rows added successfully to db")



