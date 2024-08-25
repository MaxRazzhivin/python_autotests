import requests

URL = 'https://api.pokemonbattle.ru/v2'

TOKEN = '94fa6361fcd6bbdc8d1650a29256f0c4'

HEADER = {
    "Content-type": "application/json",
    "trainer_token": TOKEN
}

body_registration = {
    "trainer_token": TOKEN,
    "email": "some_mail@gmail.com",
    "password": "Iloveqa123"
}

trainer_token = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "generate",
    "photo_id": -1
}

catch_in = {
    "pokemon_id": "61304"
}

knockout_pokemon = {
    "pokemon_id": "47150"
}



# 1) Создание нового тренера
# requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)

# 2) Подтверждение почты для нового тренера
# response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = trainer_token)

# 3) Создание нового со случайным ником и случайной фото (метод POST)
# response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
# print(response_create.status_code)
# print(response_create.text)

# 4) #Изменяем имя конкретного покемона (по id) и фото (метод PUT)
# response_put = requests.put(url = f'{URL}/pokemons', headers=HEADER, json = {"pokemon_id": "61306","name": "Homelander", "photo_id": -1
# }) 
# print(response_put.text)

#5) Поймать в покеболл

catch_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = catch_in)
print(catch_pokeball.text)
print('Статус код ответа - ', catch_pokeball.status_code)

# 6) Отправить в нокаут

# knockout = requests.post(url = f'{URL}/pokemons/knockout', headers = HEADER, json = knockout_pokemon)
# print('Покемон', knockout_pokemon["pokemon_id"], 'был отправлен в нокаут')
