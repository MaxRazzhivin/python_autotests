import requests, pytest

URL = 'https://api.pokemonbattle.ru/v2'

TOKEN = '94fa6361fcd6bbdc8d1650a29256f0c4'

HEADER = {
    "Content-type": "application/json",
    "trainer_token": TOKEN
}

TRAINER_ID = "4822"

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', headers=HEADER)
    assert response.status_code == 200

def test_status_code2():
    response = requests.get(url = f'{URL}/trainers', headers=HEADER, params={"trainer_id":TRAINER_ID})
    assert response.json()["data"][0]["trainer_name"] == "Кот Леопольд"


# def test_part_of_responce():
#     response_get = requests.get(url = f'{URL}/pokemons', headers=HEADER, params={"trainer_id":TRAINER_ID})
#     assert response_get.json()["data"][0]["name"] == "New Keyonchester" 

# @pytest.mark.parametrize('key, value', [('name', 'New Keyonchester'), ('trainer_id', TRAINER_ID), ('id', '47158')])

# def test_parametrize(key, value):
#     response_parametrize = requests.get(url = f'{URL}/pokemons', headers=HEADER, params={"trainer_id":TRAINER_ID})
#     assert response_parametrize.json()["data"][0][key] == value


#Создаем нового покемона со случайным именем и картинкой (метод POST)
def test_status_code_create():
    response_create = requests.post(url = f'{URL}/pokemons', headers=HEADER, json = {"name": "generate", "photo_id": -1
}) 
    assert response_create.status_code == 201

#Изменяем имя конкретного покемона и фото (метод PUT)
def test_status_code_put():
    response_put = requests.put(url = f'{URL}/pokemons', headers=HEADER, json = {"pokemon_id": "61291","name": "Homelander", "photo_id": -1
}) 
    assert response_put.status_code == 200