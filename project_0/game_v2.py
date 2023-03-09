"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def random_predict(data,number):
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """  
    data = list(range(1,101))   # задаем список чисел , в котором будет искать загнаданное
    low = 0                     # начальный индекс интервала списка
    high = len(data)            # конечный индекс интервала списка
    count = 0
    while low <= high:          
              count += 1
              middle = (low + high)//2
       
              if data[middle] == number:
                 break
              elif data[middle] > number:
                 high = middle - 1
              else:
                 low = middle + 1
    return count 
   
data = list(range(1,101))
def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(data,number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
