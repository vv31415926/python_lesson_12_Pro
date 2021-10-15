# Поиск вакансий
import requests
import json
import pprint
from areas_guide import get_id_Region
from statistics import Statistics

DOMAIN = 'https://api.hh.ru/'
url_vacancies =  f'{DOMAIN}vacancies'

idRegion = get_id_Region( DOMAIN, 'Россия', 'Москва' )
print( 'ID региона:',idRegion )

nFrom = 0.0
nTo = 0.0
s = 0.0
n = 0

stat = Statistics()
num = 0
for ind_page in range( 200 ):
    params = {
        #'search_field' : 'name',
        #'text' : 'NAME:(Python OR Java)',
        'text' : 'Developer',
        'per_page' : 50,
        'page' : ind_page,
        'area': idRegion
    }
    print( '>>> page=', ind_page, num )
    response = requests.get( url_vacancies, params=params ).json()

    #print( response.keys() )
    #pprint.pprint( response )

    try:
        items = response['items']
        #print( items[0].keys())
    except KeyError:
        items = []

    if len( items ) == 0:
        print( 'пустой итемс')
        break

    #pprint.pprint(items)

    for it in items:  # список словарей   -> текущий словарь
        #pprint.pprint( '-----------------> по  items:', len(it))
        #print(it.keys())

        vSnip = it['snippet']   # словарь требований/ответственности
        vr = vSnip['requirement'] # словарь требований -> строка
        #pprint.pprint( vr )
        num += stat.go_seek(  vr  )     # сбор статистики

print( stat.get_stat() )

with open( 'statistic.json', 'w' ) as f:
    json.dump( stat.get_stat(), f )

statProc = stat.processing()
pprint.pprint( statProc )

with open( 'statistic10.json', 'w' ) as f:
    json.dump( statProc[:10], f )





