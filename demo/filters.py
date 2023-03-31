def custom_filter(some_list: list) -> bool:
    sum: int = 0
    for x in some_list:
        if isinstance(x,int) and x%7==0:
            sum += x
    if sum < 83: return True
    else: return False

#def anonymous_filter(text: str) -> bool:
anonymous_filter = lambda text: text.lower().count('я') >= 23

print(custom_filter([2, 3, 5, 49, 23, 75]))
print(custom_filter([7, 14, 28, 32, 32, 56]))
print(custom_filter([7, 14, 28, 32, 32, '56']))

print(anonymous_filter('Я - последняя буква в алфавите!'))
print(anonymous_filter('яяяяяяяяяяяяяяяяяяяяяяяя, яяяяяяяяяяяяяяяя и яяяяяяяя тоже!'))