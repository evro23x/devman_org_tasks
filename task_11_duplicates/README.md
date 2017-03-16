# Anti-Duplicator

Скрипт принимает на вход папку, просматривает все файлы в ней (и всех подпапках и под-под-...папках) и сообщает, если находит дубликаты. Дубликаты – это два файла с одинаковым именем и размером.


# Quickstart

Пример запуска скрипта в среде Linux, под Python 3.5:

```#!bash
$ python duplicates.py <path to file>
```
# Example

```#!bash

$ python duplicates.py .
Duplicate files found: First file - './test1/test11/test111/1111/1' and second file - './test2/testj2j/1'
Duplicate files found: First file - './test1/test11/test111/1111/1' and second file - './test2/testj2j/dkdkdkd/1'
Duplicate files found: First file - './test2/testj2j/1' and second file - './test2/testj2j/dkdkdkd/1'

```
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
