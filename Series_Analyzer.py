def series_list(int_l_series):
    while True:
        series = input("enter at least 3 numbers: ")
        l_series = series.split(" ")
        if len(l_series) < 3:
            continue
        try:
            for i in l_series:
                float(i)
                if int(i) <= 0:
                    raise ValueError
        except:
            continue
        break

    for i in l_series:
        if "." in i:
            int_l_series.append(float(i))
        else:
            int_l_series.append(int(i))
    return int_l_series

def print_menu(user_list):
    flag = True
    while flag:
        menu = input('''
        enter a number for choose:
        ==========================
        1. for input a new series
        2. for display the series(original order)
        3. for display the series (reversed order
        4. for display the series (sorted from low to high)
        5. for display the max value
        6. for display the min value
        7. for display the average value
        8. for display the number of element
        9. for display the sum of the series
        0. for exit
        ==========================
        ''')
        try:
            int(menu)
            if int(menu) < 0 or int(menu) > 9:
                raise ValueError
        except:
            print("try again")
            continue
        match menu:
            case "1":
                flag = False
                init_program()
            case "2":
                for i in user_list:
                    print(i, end=" ")
            case "3":
                print(user_list[::-1])
            case "4":
                print(sorted(user_list))
            case "5":
                print(max(user_list))
            case "6":
                print(min(user_list))
            case "7":
                sum_l = 0
                for i in user_list:
                    sum_l += i
                print(sum_l / len(user_list))
            case "8":
                print(len(user_list))
            case "9":
                print(sum(user_list))
            case "0":
                flag = False



def init_program():
    user_list = []
    series_list(user_list)
    print_menu(user_list)

init_program()