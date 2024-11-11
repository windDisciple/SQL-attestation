# Задача 1. Создайте функцию, которая принимает кол-во сек и формат их в кол-во дней часов. Пример: 123456 ->'1 days 10 hours 17 minutes 36 seconds '

# def format_time(seconds):  
#     days = seconds // 86400   
#     seconds %= 86400          
#     hours = seconds // 3600    
#     seconds %= 3600            
#     minutes = seconds // 60    
#     seconds %= 60            
#     return f"{days} days {hours} hours {minutes} minutes {seconds} seconds"  

# result = format_time(123456)  
# print(result)

# Задача 2. Выведите только чётные числа от 1 до 10.

def print_even_numbers():  
    even_numbers = [num for num in range(1, 11) if num % 2 == 0]  
    return even_numbers  

result = print_even_numbers()  
print(result)