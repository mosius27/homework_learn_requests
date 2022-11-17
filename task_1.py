# -*- coding: utf-8 -*-

import requests
import json

class Heroes():
    # Получение списка всех супергероев
    def __init__(self):
        response = requests.get('https://akabab.github.io/superhero-api/api/all.json')
        self.heroes_list = json.loads(response.content)

    def find_select_heroew_power(self, heroes: list, powerstat: str) -> dict:
        heroes_powerstat = {}
        for hero in heroes:
            hero = hero.strip().title()
            for h in self.heroes_list:
                if hero == h['name']:
                    heroes_powerstat[hero] = h['powerstats'][self.powerstats[powerstat]]

        return heroes_powerstat

    def show_possible_stats(self):
        response = requests.get('https://akabab.github.io/superhero-api/api/powerstats/1.json')
        powerstats = json.loads(response.content)
        self.powerstats = {}
        for i, powerstat in enumerate(powerstats.keys()):
            print(f'{i+1} - {powerstat}')
            self.powerstats[str(i + 1)] = powerstat

if __name__ == '__main__':
    heroes = Heroes()
    heroes_for_compare = input('Введите через запятую героев для сравнения: ').split(',')
    heroes.show_possible_stats()
    powerstat = input('Выберите по какому параметру сравнивать героев: ')
    heroes_powerstat = heroes.find_select_heroew_power(heroes_for_compare, powerstat)
    print(f'Самый высокий показатель {heroes.powerstats[powerstat]} у героя {sorted(heroes_powerstat, key=heroes_powerstat.get)[-1]}')