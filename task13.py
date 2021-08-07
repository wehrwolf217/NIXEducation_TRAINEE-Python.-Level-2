#! /usr/bin/env python3
"""Напишите скрипт, который пишет в консоль "Hello, <имя> <фамилия>! Nice to see you here!"
На вход скрипт принимает имя и фамилию, которые в последствии и используются в скрипте."""

full_name = input("Enter name and second name: ")
name = full_name.split(' ')[0]
second_name = full_name.split(' ')[1]
print(f"Hello, {name} {second_name}! Nice to see you here!")

