#! /usr/bin/env python3
"""Напишите функцию, которая принимает число - таймзону от GMT (например, Киев - таймзона +2,
соответсвенно передаёте 2, или Гавайи - таймзона = -10, соответсвенно передаёте -10), и возвращает
текущую дату и время в указаной таймзоне.
Формат:
[<часов>:<минут>:<секунд>] - <день месяца>, <полное название месяца> of <год>
например: [16:22:26] - 11, March of 2021"""

from datetime import datetime, timedelta


def time_zone(num: int):
    current_time = datetime.utcnow()    # текущее время gmt +0
    result = current_time + timedelta(hours=num)
    return result.strftime("[%H:%M:%S] - %d, %B of %Y")

