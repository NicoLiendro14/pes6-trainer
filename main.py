from ReadWriteMemory import ReadWriteMemory

rwm = ReadWriteMemory()
process = rwm.get_process_by_name('PES6.exe')
process.open()


def get_home_goal():
    home_goal_pointer = process.get_pointer(0x1017B30)
    home_goal_value = process.read(home_goal_pointer)
    home_goal_pointer_visual = process.get_pointer(0x1017B38)
    home_goal_value_visual = process.read(home_goal_pointer_visual)
    return {
        "home_goal_pointer": home_goal_pointer,
        "home_goal_value": home_goal_value,
        "home_goal_pointer_visual": home_goal_pointer_visual,
        "home_goal_value_visual": home_goal_value_visual
    }


def get_away_goal():
    away_goal_pointer = process.get_pointer(0x1017E24)
    away_goal_value = process.read(away_goal_pointer)
    away_goal_pointer_visual = process.get_pointer(0x1017E2C)
    away_goal_value_visual = process.read(away_goal_pointer_visual)
    return {
        "away_goal_pointer": away_goal_pointer,
        "away_goal_value": away_goal_value,
        "away_goal_pointer_visual": away_goal_pointer_visual,
        "away_goal_value_visual": away_goal_value_visual
    }


def add_goal_home():
    data_home_goal = get_home_goal()
    home_goal_value = data_home_goal['home_goal_value'] + 5
    process.write(data_home_goal['home_goal_pointer'], home_goal_value)
    home_goal_value_visual = data_home_goal['home_goal_value_visual'] + 5
    process.write(data_home_goal['home_goal_pointer_visual'], home_goal_value_visual)


def add_goal_away():
    data_away_goal = get_away_goal()
    away_goal_value = data_away_goal['away_goal_value'] + 5
    process.write(data_away_goal['away_goal_pointer'], away_goal_value)
    away_goal_value_visual = data_away_goal['away_goal_value_visual'] + 5
    process.write(data_away_goal['away_goal_pointer_visual'], away_goal_value_visual)


def get_home_name():
    name_pointer = process.get_pointer(0x10D3C16)
    result = process.read(name_pointer)
    result_String_1 = result.to_bytes(4, byteorder='little').decode('utf-8')

    name_pointer = process.get_pointer(0x10D3C1A)
    result = process.read(name_pointer)
    result_String_3 = result.to_bytes(4, byteorder='little').decode('utf-8')

    return result_String_1 + result_String_3


def get_away_name():
    name_pointer = process.get_pointer(0x10D6E3E)
    result = process.read(name_pointer)
    result_String_1 = result.to_bytes(4, byteorder='little').decode('utf-8')

    name_pointer = process.get_pointer(0x10D6E42)
    result = process.read(name_pointer)
    result_String_3 = result.to_bytes(4, byteorder='little').decode('utf-8')
    return result_String_1 + result_String_3


def print_status():
    print(get_home_name(), ":", get_home_goal()['home_goal_value'])
    print(get_away_name(), ":", get_away_goal()['away_goal_value'])
