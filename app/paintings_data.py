import json

def retrieve_all_paintings():
    with open('paintings.json', 'r') as json_file:
        all_paintings = json.load(json_file)
    return all_paintings


def retrieve_requested_paintings(painting_id):
    requested_painting = [el for el in retrieve_all_paintings() if el['Id'] == painting_id]
    print(requested_painting)
    return requested_painting
