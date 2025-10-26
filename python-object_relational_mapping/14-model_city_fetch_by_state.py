#!/usr/bin/python3
"""
Next, write a script 14-model_city_fetch_by_state.py that prints
 all City objects from the database hbtn_0e_14_usa:

Your script should take 3 arguments: mysql username,
 mysql password and database name
You must use the module SQLAlchemy
You must import State and Base from model_state
 - from model_state import Base, State
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by cities.id
Results must be display as they are in the example below
 (<state name>: (<city id>) <city name>)
Your code should not be executed when imported
"""
if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from model_city import City
    import sys

    username = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{passwd}@localhost:3306/{db_name}"
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State, City).join(City,
                                              State.id == City.state_id).all()

    for state, city in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
