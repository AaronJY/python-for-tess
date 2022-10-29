my_list = []

while len(my_list) < 5:
    print("Gimmie a number")
    user_input = input()

    try:
        my_int = int(user_input)
        my_list.append(my_int)
    except:
        print("Input must be an integer")
    
print("All done!")
print(my_list)