friends_users = {
    'Joey':'howyoudoin96',
    'Chandler': 'nagnagnag96',
    'Ross': 'wewereonabreak96',
    'Rachel': 'whineeeeeeee96',
    'Monica': 'cleanhell96',
    'Phoebe': 'sillycat96',
}

office_users = {
    'Michael' : 'fucktoby96',
    'Jim' : 'screwdwight96',
    'Dwight': 'screwjim96',
    'Pam' : 'artschool96',
    'Angela': 'partyplanner96',
    'Phyllis': 'bobvance96',
    'Stanley': 'didistutter96',
    'Oscar': 'actually96',
    'Andy': 'rududududu96',
    'Kevin': 'johnmellencamp96',
    'Creed': 'qualityassurance96',
    'Ryan': 'hiimryan96',
    'Kelly': 'omgryan',
}

always_sunny_users = {
    'Mac': 'helloworld96',
    'Charlie': 'thechick96',
    'Dennis': 'dennis96',
    'Deandra': 'deandra96',
    'Frank': 'frankie96',
}

family_guy_users = {
    'Peter': 'fatass96',
    'Lois': 'dumbhoe96',
    'Chris': 'dumbass96',
    'Meg': 'uglyass96',
    'Stewie': 'fruityass96',
    'Bryan': 'pretentiousass96',
}

# from django.contrib.auth.models import User
# from users.models import GigzWorkerUserProfile
# import random
# for i, user in enumerate(always_sunny_users):
#     # all going to be workers
#     username = user
#     password = always_sunny_users[user]
#     user = User.objects.filter(username=user)[0]
#     lat = 43.629702 + (random.random()-0.5)*2
#     lng =  -111.068024 + (random.random()-0.5)*2
#     GigzWorkerUserProfile.objects.create(user=user,location_lat=lat, location_lng=lng, completed_jobs = int(random.random()*10),worker_rating=int(random.random()*5),worker_description="")

# from django.contrib.auth.models import User
# from users.models import GigzEmployerUserProfile
# import random
# for i, user in enumerate(always_sunny_users):
#     # all going to be workers
#     username = user
#     password = always_sunny_users[user]
#     user = User.objects.filter(username=user)[0]
#     lat = 35.423773+ (random.random()-0.5)*2
#     lng =  -85.117176  + (random.random()-0.5)*2
#     GigzEmployerUserProfile.objects.create(user=user,location_lat=lat, location_lng=lng, posted_jobs = int(random.random()*10),employer_rating=int(random.random()*5),employer_description="")

breaking_bad_users = {
    'Walter' : 'white96',
    'Jesse' : 'pinkman96',
    'Gus' : 'fring96',
    'Hank' : 'schrader96',
    'Skyler' : 'white96',
    'Mike' : 'ehrmantraut96',
}

from django.contrib.auth.models import User
from users.models import GigzWorkerUserProfile
import random
for user in breaking_bad_users:
    # all going to be workers
    username = user
    password = breaking_bad_users[user]
    user = User.objects.create(username=user, password = password)  
    lat = 39.139783 + (random.random()-0.5)*7
    lng = -102.154984 + (random.random()-0.5)*7
    GigzWorkerUserProfile.objects.create(user=user,location_lat=lat, location_lng=lng, completed_jobs = int(random.random()*10),worker_rating=int(random.random()*5),worker_description="")


cities = {
    'NYC': [40.730610, -73.935242],
    'LAX': [34.052235, -118.243683],
    'ORD': [41.881832, -87.623177],
    'MSP': [44.986656, -93.258133],
    'DAL': [32.779167, -96.808891],
    'SEA': [47.608013, -122.335167]
}


job_addresses = [
    '15357 Eagle Creek Way, Apple Valley MN, 55124',
    '233 S Wacker Dr, Chicago IL, 60606',
    '20 W 34th St, New York, NY 10001',
    '300 Reunion Blvd E, Dallas, TX 75207',
    '400 Broad St, Seattle, WA 98109',
    '1601 Biscayne Blvd, Miami, FL 33132',
]

job_titles = [
    'Python Developer',
    'Java Developer',
    'Database Administrator',
    'DevOps Engineer',
    'Business Analyst',
    'Product Manager',
    'Program Manager',
]

# from users.models import *
# from django.contrib.auth.models import User
# from jobs.models import *
# import random

# users = User.objects.all()
# workers = []
# employees = []

# for i, user in enumerate(users):
#     city = random.choice(list(cities.keys()))
#     location_lat = cities[city][0] + (random.random() -0.5)/10
#     location_lng = cities[city][1] + (random.random() -0.5)/10
#     if i%2==0:
#         workers.append(user)
#         GigzWorkerUserProfile.objects.create(user=user, location_lat=location_lat, location_lng=location_lng,completed_jobs=int(random.random()*10),worker_rating=int(random.random()*5),worker_description='')
#     else:
#         employees.append(user)
#         GigzEmployerUserProfile.objects.create(user=user, location_lat=location_lat, location_lng=location_lng,posted_jobs=int(random.random()*10),employer_rating=int(random.random()*5),employer_description='')
