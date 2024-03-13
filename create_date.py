"""
    Скрипт для создания первичных данных в базе данных.

    Этот скрипт использует Django ORM для создания тэгов,
    кодов мобильных операторов и timezone в базе данных.
"""

import os
import pytz
from typing import List

import django
from django.db import IntegrityError

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from apps.client.models import Tag, MobileOperatorCode, TimeZone


def create_tags(tags: List[str]) -> None:
    for tag_name in tags:
        if not Tag.objects.filter(client_filter_tag=tag_name).exists():
            Tag.objects.create(client_filter_tag=tag_name)
        else:
            print("Произошла ошибка.", tag_name)
            break


def create_mobile_operator_code(codes: List[int]) -> None:
    for code in codes:
        if not MobileOperatorCode.objects.filter(operator_code=code).exists():
            MobileOperatorCode.objects.create(operator_code=code)
        else:
            print("Произошла ошибка.", code)
            break


def get_russian_timezones() -> None:
    for tz in pytz.all_timezones:
        if (
            tz.startswith("Europe/Moscow")
            or tz.startswith("Europe/Simferopol")
            or tz.startswith("Europe/Kirov")
            or tz.startswith("Europe/Astrakhan")
            or tz.startswith("Europe/Volgograd")
            or tz.startswith("Europe/Saratov")
            or tz.startswith("Europe/Ulyanovsk")
            or tz.startswith("Europe/Samara")
            or tz.startswith("Asia/Yekaterinburg")
            or tz.startswith("Asia/Omsk")
            or tz.startswith("Asia/Novosibirsk")
            or tz.startswith("Asia/Barnaul")
            or tz.startswith("Asia/Tomsk")
            or tz.startswith("Asia/Novokuznetsk")
            or tz.startswith("Asia/Krasnoyarsk")
            or tz.startswith("Asia/Irkutsk")
            or tz.startswith("Asia/Chita")
            or tz.startswith("Asia/Yakutsk")
            or tz.startswith("Asia/Khandyga")
            or tz.startswith("Asia/Vladivostok")
            or tz.startswith("Asia/Ust-Nera")
            or tz.startswith("Asia/Magadan")
            or tz.startswith("Asia/Sakhalin")
            or tz.startswith("Asia/Srednekolymsk")
            or tz.startswith("Asia/Kamchatka")
            or tz.startswith("Asia/Anadyr")
        ):
            try:
                TimeZone.objects.create(timezone=tz)
            except IntegrityError:
                print("Could not create ", tz)
                break


if __name__ == "__main__":
    female_tags = [
        "Мода",
        "Красота",
        "Здоровье и фитнес",
        "Кулинария",
        "Дизайн интерьера",
        "Путешествия",
        "Любовь к животным",
        "Искусство и рукоделие",
        "Литература и книги",
        "Фильмы и сериалы",
        "Спорт и активный отдых",
        "Технологии и компьютеры",
        "Автомобили и мотоциклы",
        "Путешествия и приключения",
        "Фотография и видеосъемка",
        "Музыка и музыкальные инструменты",
        "Пивоварение и виноделие",
        "Военная история и оружие",
        "Кулинария и гриль",
        "Финансы и инвестиции",
    ]
    # fmt: off
    numbers = [
        900, 901, 902, 903, 904, 905, 906, 910, 911, 912, 913, 914,
        915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926,
        927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938,
        939, 958, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969,
        977, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 991,
        992, 993, 995, 996, 997, 998, 999,
    ]

    try:
        create_tags(female_tags)
        create_mobile_operator_code(numbers)
        get_russian_timezones()
        print("-" * 30)
        print("Тэги успешно созданы!")
        print("-" * 30)
        print("Коды операторов успешно созданы!")
        print("-" * 30)
        print("Часовые пояса успешно созданы")
        print("-" * 30)
    except Exception as e:
        print(e)
