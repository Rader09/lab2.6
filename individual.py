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
            date = list(map(int, input("Введите дату рождения> ").split(" ")))

            temp = {
                'last_name': last_name,
                'name': name,
                'tel': tel,
                'date': date
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
                        ".".join(map(str, worker.get('date')))
                    )
                )
            print(line)

        elif command == "task":
            check = list(map(int, input("Введите дату рождения с пробелом> ").split(" ")))
            task_list = []
            iz = 0
            for worker in workers:
                if ''.join(map(str, worker.get('date'))) == ''.join(map(str, check)):
                    task_list.append(worker)
                    iz += 1

            if iz == 0:
                print("Workers not found")
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
                            ".".join(map(str, worker.get('date')))
                        )
                    )
                print(line)


        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить работника;")
            print("list - вывести список работников;")
            print("task - вывести сотрудников определенной даты рождения")
            print('help - отобразить справку')
            print("exit - выход из программы;")

        else:
            print("Неизвестная команда {command}", file=sys.stderr)