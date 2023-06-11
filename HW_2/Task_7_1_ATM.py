# Задание №6
# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег


from secrets import choice


START_SUM = 0
count = 0

def add_money(account, count):
    money = int(input("Ведите сумму пополнения, кратную 50 у.е.: "))
    if money % 50 == 0:
        if count < 3:
            account += money
        else:
            account += money - money * 0.03
            print("При пополнении удержано 3%")
        count += 1
    else:
        print("Некорректный ввод, повторите.")
    return account, count
            
      
def pop_money(account, count):
    money = int(input("Ведите сумму снятия, кратную 50 у.е.: "))
    if money % 50 == 0 and money < account:
        if count < 3:
            percent = money * 0.015
            if percent <= 30:
                percent = 30
            elif percent >= 600:
                percent = 600
            balance = account - money - percent
        else:
            percent = money * 0.03
            if percent <= 30:
                percent = 30
            elif percent >= 600:
                percent = 600
            balance = account - money - percent

        if balance > account:
            print('Недостаточно денег для снятия.')
            return account, count
        else:
            account = balance
            return account, count
    else:
        print('Недостаточно денег для снятия.')
        return account, count


def exit(account):
    print("Сумма на счету:", account, "у.е.")
    

account = START_SUM
while True:
    choice = input("Выберете действие: 1 - пополнить, 2 - снять, 3 - выйти: ")
    if account > 5_000_000:
        account -= account * 0.1
    match choice:
        case '1':
            account, count = add_money(account, count)
            print("Сумма на счету:", account, "у.е.")
        case '2':
            account, count = pop_money(account, count)
            print("Сумма на счету:", account, "у.е.")
        case '3':
            exit(account)
            break
        case _:
            print("Неверный ввод. Сумма на счету:", account, "у.е.")
