from sys import argv


__all__ = ['is_valid_date']


def _is_leap_year(year):
    return not (year % 4 != 0 or year % 100 == 0 and year % 400 != 0)

def is_valid_date(date_str):
    try:
        day, month, year = map(int, date_str.split('.'))
        if 1 > year > 9999:
            return False
        if 1 > month > 12:
            return False
        if month in [4, 6, 9, 11]  and day > 30:
            return False
        if month == 2:
            if _is_leap_year(year):
                if day > 29:
                    return False
                elif day > 28:
                    return False
        else:
            return True
    except:
        return False

# print(is_valid_date('22.06.2023'))

if __name__ == '__main__':
    print(is_valid_date(argv[1]))
