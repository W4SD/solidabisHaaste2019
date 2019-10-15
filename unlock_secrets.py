import requests

all_the_shit = []

secret_url = requests.get('https://koodihaaste-api.solidabis.com/secret').json()
get_shit = requests.get(secret_url['bullshitUrl'], headers={'Authorization': secret_url['jwtToken']})

if get_shit.status_code == 200:
    print("Getting shit done!")
    for msg in get_shit.json()['bullshits']:
        print(msg['message'])
        all_the_shit.append(msg['message'])
else:
    print("Cant do shit!")