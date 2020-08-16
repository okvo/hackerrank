# https://www.hackerrank.com/challenges/collections-counter/problem
from collections import Counter
number_shoes = int(raw_input())
shoes_sizes_list = raw_input().split(' ')
customer_number = int(raw_input())


total_price = 0
for i in range(0, customer_number):
    shoes_list = (raw_input().split(' '))

    shoes_size = shoes_list[0]
    price = int(shoes_list[-1])

    shoes_size_counter = Counter(shoes_sizes_list)
    
    if shoes_size in Counter(shoes_sizes_list).keys():
        shoes_sizes_list.remove(shoes_size)
        total_price = total_price+price
        
print total_price
