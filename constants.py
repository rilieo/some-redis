# level of parsing
columns = {
    "first_name": 1,
    "last_name": 1,
    "email": 1,
    "marital_status": 1,
    "relationship": 2,
    "spouse": 2
}

# first_names to choose from
first_name = [
    "Mylo",
    "Gui",
    "Benedicta",
    "Sibley",
    "Patsy",
    "Carlynn",
    "Urson",
    "Eugenia",
    "Dalston",
    "Tori",
    "Lianne",
    "Kasper",
    "Deane",
    "Kenton",
    "Laurie"
]

# last names to choose from
last_name = [
    "Fassbindler",
    "Escalero",
    "Francesco",
    "Normanville",
    "Daulton",
    "Cloy",
    "Managh",
    "Mathelon",
    "Antao",
    "Readhead",
    "Wagon",
    "Mellings",
    "Kimberly",
    "Wurst",
    "Truman"
]

# emails to choose from
emails = [
    "syakubowicz0@devhub.com",
    "mrixon1@si.edu",
    "hpock2@nhs.uk",
    "hdanielsson3@cocolog-nifty.com",
    "gambrogioni4@ca.gov",
    "gkrause5@illinois.edu,"
    "hpalatini6@xinhuanet.com",
    "cblagden7@ox.ac.uk",
    "mmcpharlain8@msn.com",
    "vpoytres9@shinystat.com",
    "kgaskoina@phpbb.com",
    "lbaxendaleb@fotki.com",
    "dbrugmannc@go.com",
    "rcappineerd@virginia.edu",
    "dtebbite@cocolog-nifty.com",
    "gmulrooneyf@symantec.com"
]

# relationship statuses
relationship = [
    "Single",
    "Married",
    "Divorced"
]

# spouses to choose from
spouse = [
    "Luis Tyrrell",
    "Trudey Dury",
    "Germaine Seldon",
    "Doris Colchett",
    "Aileen Derl",
    "Tommy Driuzzi",
    "Vivienne Mitkin",
    "Chaddy Venney",
    "Adelice Farnell",
    "Engracia Corcoran",
    "Gill Jerdein",
    "Madelena Bonifazio",
    "Bette Klich",
    "Florentia Candie",
    "Lyndell Medforth"
]

# list of people to add
people = [
    {"first_name": "Janith", "last_name":"Jickles", "email":"jjickles0@nba.com", "marital_status":{"relationship": "Single", "spouse":None}},
    {"first_name": "Jereme", "last_name":"Dotson", "email":"jdotson1@bigcartel.com", "marital_status":{"relationship": "Single", "spouse":None}},
    {"first_name": "Orran", "last_name":"Pinches", "email":"opinches2@businessweek.com","marital_status":{"relationship": "Married", "spouse":"Danr Slusser"}},
    {"first_name": "Katlin", "last_name":"McGloin", "email":"kmcgloin3@ucoz.ru", "marital_status":{"relationship": "Married", "spouse":"Andrej Hermansson"}},
    {"first_name": "Elysia", "last_name":"Hinners", "email":"ehinners4@irs.gov", "marital_status":{"relationship": "Single", "spouse":None}}
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

# what columns can be changed
to_change = [
    "first_name",
    "last_name",
    "email",
    "marital_status",
    "relationship",
    "spouse"
]


