from assets.first_name import first_name
from assets.last_name import last_name
from assets.email import emails
from assets.marital_status import relationship, spouse

# level of parsing
columns = {
    "first_name": 1,
    "last_name": 1,
    "email": 1,
    "marital_status": 1,
    "relationship": 2,
    "spouse": 2
}

# what columns can be changed
to_change = [
    "first_name",
    "last_name",
    "email",
    "marital_status",
    "relationship",
    "spouse"
]

# makes my life easier
options = {
    "first_name": first_name,
    "last_name": last_name,
    "email": emails,
    "marital_status": [relationship, spouse],
    "relationship": relationship,
    "spouse": spouse

}





