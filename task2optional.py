"""Необов'язкове завдання.
Дано k відсортованих списків цілих чисел. 
Ваше завдання — об'єднати їх у один відсортований список. 
Використати мінімальну купу.
Реалізуйте функцію, яка приймає на вхід список відсортованих списків та повертає відсортований список.
"""
import heapq

def merge_k_lists(lists:list[list])-> list:
    """Функція для сортування списку списків. 
    Приймає на вхід список відсортованих списків та повертає відсортований список"""

    #розпаковуємо список списків, щоб отримати єдиний список і позбутись вкладеності
    l = []
    sorted_list = []

    for i in lists:
        l+=i

    heapq.heapify(l)
    while l:
        heapq.heappush(sorted_list, heapq.heappop(l))
    return sorted_list



lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
lists2 = [[1, 4, 5, 8, 15], [1, 3, 4, 21, 23], [2, 6, 8, 17], [3, 4], [1, 7, 56]]
print(merge_k_lists(lists))
print(merge_k_lists(lists2))
