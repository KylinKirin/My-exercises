import time


def date_to_index(start, stop, *target):
    start, stop = str(start), str(stop)
    i, one_day = 0, 86400
    date_list = []
    while True:
        dat = time.strftime('%Y%m%d', time.localtime((time.mktime(time.strptime(start, "%Y%m%d"))+i*one_day)))
        # print(dat)
        if time.mktime(time.strptime(start, "%Y%m%d")) > time.mktime(time.strptime(stop, "%Y%m%d")):
            print("Wrong range")
            return
        date_list.append(str(dat))
        i += 1
        if str(dat) == stop:
            break
    # print(date_list)
    res = []
    for date in target:
        # print(date, type(date))
        try:
            index = date_list.index(str(date))
            res.append(index + 1)
        except ValueError:
            print(str(date)+" Not found")
    print("Respectively "+str(res))


if __name__ == '__main__':
    date_to_index("19980101", "19981231", "19980101", "19980329", "19980929")
