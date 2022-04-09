from daily_sales import daily_sales


def refactor_data():
    daily_sales_replaced = daily_sales.replace(";,;", "#")
    daily_transactions = daily_sales_replaced.strip().split(",")
    daily_transactions_splitted = []
    for word in daily_transactions:
        daily_transactions_splitted.append(word.replace("\n", "").split("#"))
    return daily_transactions_splitted


def list_of_values(data):
    values = []
    for value in data:
        values.append(value[1])
    return values


def refactor_colors(data):
    colors = []
    for color in data:
        colors.append(color[2].strip())
    return colors


def sum_of_items(values):
    total_amount = 0
    for value in values:
        total_amount += float(value.replace("$", ""))
    return total_amount


def list_of_colors(colors):
    color_list = []
    for i in colors:
        if i.__contains__("&"):
            x = i.split("&")
            color_list.extend(x)
        else:
            color_list.append(i)
    return color_list


def count_colors(color_list):
    colors_dict = dict()
    for color in color_list:
        if color in colors_dict:
            colors_dict[color] += 1
        else:
            colors_dict[color] = 1
    return colors_dict


daily_transactions_split = refactor_data()
total_sum = sum_of_items(list_of_values(daily_transactions_split))
colors_dictionary = count_colors(list_of_colors(refactor_colors(daily_transactions_split)))
