import logging
import random as ran
logging.basicConfig(level=logging.DEBUG, filename='logs_guess.log', format='%(levelname)s (%(asctime)s): %(message)s', datefmt='%d/%m/%Y %I:%M:%S', encoding='utf-8')
logging.info("Программа была запущена")
quant = int(input("Промежуток для загадывания числа (введите значение): от 1 до "))
while quant <= 1:
    logging.error("Пользователь ввёл некорректное значение")
    quant = int(input("Вы ввели некорректный промежуток, попробуйте ещё раз: от 1 до "))
logging.info("Промежуток для загадывания числа: от 1 до " + str(quant))
attempts = int(input("Введите количество попыток для того, чтобы угадать число из промежутка, загаданное программой - "))
while attempts < 1:
    logging.error("Пользователь ввёл некорректное значение")
    attempts = int(input("Вы ввели некорректное количество попыток, попробуйте ещё раз - "))
logging.info("Количество попыток: " + str(attempts))
numb = ran.randint(1, quant)
logging.info("Программа загадала число " + str(numb))
N = int(input("Угадайте число от 1 до " + str(quant) + " - "))
logging.info("Пользователь ввел число " + str(N))
if N == numb:
    print("Вы угадали с первой попытки! Я загадал", numb)
    logging.info("Пользователь угадал число с первой попытки. Загаданное число - " + str(numb))
else:
    attempts -= 1
    while N != numb:
        logging.info("Пользователь не угадал число")
        logging.info("Количество оставшихся попыток: " + str(attempts))
        if N > numb:
            N = int(input("Попробуйте ещё раз (загаданное число меньше " + str(N) + ") - "))
        elif N < numb:
            N = int(input("Попробуйте ещё раз (загаданное число больше " + str(N) + ") - "))
        logging.info("Пользователь ввел число " + str(N))
        attempts -= 1
        if N == numb:
            print("Вы угадали число, я загадал", numb)
            logging.info("Пользователь угадал число. Загаданное число - " + str(numb))
        elif attempts == 0:
            print('Закончились попытки, загаданное число -', numb)
            logging.info("У пользователя закончились попытки. Загаданное число - " + str(numb))
            break
logging.info("Программа была завершена\n\n\n")