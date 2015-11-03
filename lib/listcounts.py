def sum(listofnumbers):
    if len(listofnumbers) == 0:
        raise ValueError

    result = 0
    for number in listofnumbers:
        result = result + number
    return result


def min(listofnumbers):
    if len(listofnumbers) == 0:
        raise ValueError

    mini = None

    for i in listofnumbers:
        if mini is None or i < mini:
            mini = i

    return mini
