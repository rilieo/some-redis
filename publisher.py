import redis
import json
import time
from random import randint
from assets.constants import *
from assets.people import *

KEY_INDEX = '0'

# inserts a person's information
def insert_info(db, data) -> None:
    print("Inserting")
    p = db.pipeline()
    json_data = json.dumps(data)
    db.publish('inserting', json_data)
    p.multi()
    db.incr(KEY_INDEX)
    id = int(db.get(KEY_INDEX))
    db.json().set(id, '$', data)
    p.execute()

# updates info of person
def update_info(db, id, data, column=None) -> None:
    print("Updating")
    json_data = json.dumps(data)
    db.publish(f'{column}', json_data)
    # updates all info
    if not column:
        db.json().set(id, '$', data)
    # updates given column
    else:
        path = "$" + ("." * columns[column]) + column
        db.json().set(id, f"{path}", data)

# to test
def update_randomly(db) -> None:
    random_id = randint(1, int(db.get(KEY_INDEX))) # retrieve random person
    random_attribute = to_change[randint(0, 5)] # retrieve random attribute to update

    # updates both "relationship" and "spouse" components
    if random_attribute == "marital_status":
        random, another_rand = randint(0, 14), randint(0, 2) # picks indices of random "relationship" and "spouse"
        relation = options[random_attribute][0][another_rand]
        spouse = options[random_attribute][1][random] if relation != "Single" else None
        new_info = {"relationship": relation, "spouse": spouse}
        update_info(db, random_id, new_info, random_attribute)
    # updates given attribute with random value
    else:
        another_rand = randint(0, 5) if random_attribute == "relationship" else randint(0, 14)
        update_info(db, random_id, options[random_attribute][another_rand], random_attribute)
    
# displays id & info of people
def read_info(db, column=None) -> None:
    length = int(db.get(KEY_INDEX)) # get length of database

    # reads all info of people
    if not column: 
        for i in range(1, length+1):
            print(i, end=" ")
            print(db.json().get(i, '$'))
    # reads all info of a given column
    else:
        path = "$" + ("." * columns[column]) + column
        for i in range(1, length+1):
            print(i, end=", ")
            info = db.json().get(i, f'{path}')  
            print(str(info).strip("'[]'"))

# erases database
def flushall(db) -> None:
    db.flushall()

def main() -> None:
    # sets up database
    r = redis.Redis(
        host='localhost',
        port=6379,
        decode_responses=True
        )
    
    while True:
        # inserts people into given database
        for person in people:
            insert_info(r, person)
            time.sleep(1)
    
        # reads all info of people
        read_info(r)

        # updates a random characteristic of a random person
        update_randomly(r)
        
        # to slow things down
        time.sleep(5)
    
if __name__ == "__main__":
    main()
