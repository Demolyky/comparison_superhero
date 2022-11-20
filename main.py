import requests

heroes = requests.get('https://akabab.github.io/superhero-api/api/all.json').json()

heroes_names = list(filter(lambda hero: hero['name'] in ['Hulk', 'Captain America', 'Thanos'], heroes))
intelligence_heroes = [hero['powerstats']['intelligence'] for hero in heroes_names]
intelligence_heroes.sort()
max_int_in_hero = ''
for hero in heroes_names:
    if hero['powerstats']['intelligence'] == intelligence_heroes[-1]:
        max_int_in_hero = hero['name']

print(f'Самый умный герой: {max_int_in_hero}')
