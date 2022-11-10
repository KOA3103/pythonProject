import requests

list_of_superhero = ['Hulk', 'Captain America', 'Thanos', 'Apocalypse', 'Iron Man', 'Joker', 'Rambo', 'Thor']
base_url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
sorted_list_of_intelligence = list()

def who_is_smartest(list_of_superhero: list):
    list_of_intelligence = list()
    response = requests.get(base_url, 'rb')
    intelligence = response.json()
    for hero in list_of_superhero:
        for body in intelligence:
            # print(body['name'])
            if body['name'] == hero:
                hero_intelligence = list()
                hero_intelligence.append(body['name'])
                hero_intelligence.append(body['powerstats']['intelligence'])
                hero_intelligence.append(body['appearance']['weight'])
                list_of_intelligence.append(hero_intelligence)
    sorted_list_of_intelligence.append(sorted(list_of_intelligence, key=lambda k: k[1], reverse=True))
    smartest_hero = sorted(list_of_intelligence, key=lambda k: k[1], reverse=True)[0]
    print(f'\nСамый умный супергерой это {smartest_hero[0]}.\n')
    return


def list_of_raitng():
    print(f'\n Рейтинг по интеллекту: ')
    for item in sorted_list_of_intelligence:
        n = 1
        for i in item:
            print(f'{n} место {i[0]} - {i[1]} балов, вес {i[2][1]}')
            n += 1


if __name__ == '__main__':
    who_is_smartest(list_of_superhero)
    list_of_raitng()