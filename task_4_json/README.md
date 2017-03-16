# Prettify JSON

Cкрипт принимает на вход путь до файла, в котором хранится json и выводит его содержимое в консоль в удобном формате.

# Quickstart

Пример запуска скрипта в среде Linux, под Python 3.5:

```#!bash
$ python pprint_json.py <path to file>
```
# Example

```#!bash

$ python pprint_json.py shops.json
#     {
        "Address": "Малый Гнездниковский переулок, дом 12",
        "AdmArea": "Центральный административный округ",
        "District": "Тверской район",
        "ID": "00106095",
        "IsNetObject": "нет",
        "Latitude_WGS84": "55.7624120211734460",
        "Longitude_WGS84": "37.6069280165764180",
        "Name": "Все твои друзья",
        "PublicPhone": [
            {
                "PublicPhone": "(495) 233-40-88",
                "global_id": 22302.0,
                "global_object_id": 20672648.0,
                "system_object_id": "00106095 _1"
            }
        ],
        "SeatsCount": 24,
        "SocialPrivileges": "нет",
        "TypeObject": "бар",
        "geoData": {
            "coordinates": [
                37.606928016535285,
                55.76241202098007
            ],
            "type": "Point"
        },
        "global_id": 20672648,
        "system_object_id": "00106095"
    },
    {
        "Address": "Неглинная улица, дом 4",
        "AdmArea": "Центральный административный округ",
        "District": "Мещанский район",
        "ID": "00106437",
        "IsNetObject": "нет",
        "Latitude_WGS84": "55.7600773125159320",
        "Longitude_WGS84": "37.6216014330373340",
        "Name": "Суши-бар Эноки ( при гостинице Арарат Парк Хаятт",
        "PublicPhone": [
            {
                "PublicPhone": "(495) 783-12-34",
                "global_id": 22319.0,
                "global_object_id": 20673748.0,
                "system_object_id": "00106437 _1"
            }
        ],
        "SeatsCount": 22,
        "SocialPrivileges": "нет",
        "TypeObject": "бар",
        "geoData": {
            "coordinates": [
                37.6216014334577,
                55.76007731251748
            ],
            "type": "Point"
        },

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
