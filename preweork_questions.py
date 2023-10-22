import math



#Question 1

def hello_name(user_name):
    print("hello " + user_name + "!")

hello_name('matt')




#Question 2

def first_odds():
    for i in range(1,101,2):
        print(i)
        
first_odds()




#Question 3

def max_num_in_list(a_list_3):
    if len(a_list_3) == 0:
        return None 
    else:
        max_num = a_list_3[0] 
        for num in a_list_3:
            if num > max_num:
                max_num = num
        return max_num
    

my_list_3 = [3, 6, 1, 15, 2, 8]

result_3 = max_num_in_list(my_list_3)

print(result_3)




# Question 4

def is_leap_year(a_year):
    if (a_year % 4 == 0 and a_year % 100 != 0) or (a_year % 400 == 0):
        return True
    else:
        return False


year = 2023
result_4 = is_leap_year(year)
print(result_4)




# Question 5
def is_consecutive(a_list_5):
    if len(a_list_5) <= 1:
        return True  
    
    a_list_5.sort() 
    for i in range(1, len(a_list_5)):
        if a_list_5[i] != a_list_5[i - 1] + 1:
            return False 
    return True  

my__list = [2, 3, 4, 5, 6, 7]
result_5 = is_consecutive(my__list)
print(result_5)  

my__list = [1, 2, 4, 5]
result_5 = is_consecutive(my__list)
print(result_5)  
