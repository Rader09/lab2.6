# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys



if __name__ == '__main__':
    workers = []
    while True:
        command = input("Введите команду> ").lower()

        if command == "exit":
            break

        elif command == "add":
            last_name = str(input("Введите фамилию>  "))
            name = str(input("Введите имя> "))
            tel = int(input("Введите телефон> +"))
            date1 = list(map(int, input("Введите дату рождения c пробелом> ").split(" ")))
            date2 = list(map(int, input("Введите месяц рождения> ").split(" ")))
            date3 = list(map(int, input("Введите год рождения> ").split(" ")))
            temp = {
                'last_name': last_name,
                'name': name,
                'tel': tel,
                'date1': date1,
                'date2': date2,
                'date3': date3,
            }
            workers.append(temp)
            # Отсортировать список в случае необходимости.
            if len(workers) > 1:
                workers.sort(key=lambda item: item.get('last_name', ''))

        elif command == "list":
            line = "+-{}-+-{}-+-{}-+-{}-+-{}-+".format(
                '-' * 4,
                '-' * 15,
                '-' * 15,
                '-' * 20,
                '-' * 20
            )
            print(line)
            print(
                "| {:^4} | {:^15} | {:^15} | {:^20} | {:^20} |".format(
                    "№",
                    "Фамилия",
                    "Имя",
                    "Телефон",
                    "Дата рождения"
                )
            )
            print(line)
            for idx, worker in enumerate(workers, 1):
                print(
                    '| {:>4} | {:<15} | {:<15} | {:>20} | {:^20} |'.format(
                        idx,
                        worker.get('last_name', ''),
                        worker.get('name', ''),
                        worker.get('tel', 0),
                        ".".join(map(str, worker.get('date1'))),
                        ".".join(map(str, worker.get('date2'))),
                        ".".join(map(str, worker.get('date3'))),
                    )
                )
            print(line)

        elif command == "task":
            check = list(map(int, input("Введите месяц рождения> ").split(" ")))
            task_list = []
            iz = 0
            for worker in workers:

                if ''.join(map(str, worker.get('date2'))) == ''.join(map(str, check)):
                    task_list.append(worker)
                    iz += 1


            if iz == 0:
                print("Работники не найдены")
            else:
                line = "+-{}-+-{}-+-{}-+-{}-+-{}-+".format(
                    '-' * 4,
                    '-' * 15,
                    '-' * 15,
                    '-' * 20,
                    '-' * 20
                )
                print(line)
                print(
                    "| {:^4} | {:^15} | {:^15} | {:^20} | {:^20} |".format(
                        "№",
                        "Фамилия",
                        "Имя",
                        "Телефон",
                        "Дата рождения"
                    )
                )
                print(line)
                for idx, worker in enumerate(task_list, 1):
                    print(
                        '| {:>4} | {:<15} | {:<15} | {:>20} | {:^20} |'.format(
                            idx,
                            worker.get('last_name', ''),
                            worker.get('name', ''),
                            worker.get('tel', 0),
                            ".".join(map(str, worker.get('date1'))),
                            ".".join(map(str, worker.get('date2'))),
                            ".".join(map(str, worker.get('date3'))),

                        )
                    )
                print(line)


        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить работника;")
            print("list - вывести список работников;")
            print("task - вывести сотрудников c определенным месяцем рождения")
            print('help - отобразить справку')
            print("exit - выход из программы;")

        else:
            print("Неизвестная команда {command}", file=sys.stderr)