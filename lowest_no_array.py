# my_array = eval(input("Enter a list with numbers:"))

# min_val = my_array[0]

# for i in my_array:
#     if i < min_val:
#         min_val = i

# print("Lowest value is:", min_val)

def min_val(my_array):
    min_val = my_array[0]
    for i in my_array:
        if i < min_val:
            min_val = i

    return f"Lowest value is: {min_val}"

my_list = eval(input("Enter a list with numbers:"))

print(min_val(my_list))