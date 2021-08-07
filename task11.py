#! /usr/bin/env python3

"""Сгенерируйте рандомное число при помощи модуля рандом:
import random

random_number = random.randint(1, 10)

При помощи модуля time засеките время ожидания программы и выведите его в консоль

start_time = <ваш код здесь>
"усыпите" выполнение программы на <random_number> секунд
end_time = <ваш код здесь>"""

import random
import time

random_number = random.randint(1, 10)
start_time = time.time()
time.sleep(random_number)
end_time = time.time()

print(end_time - start_time)
