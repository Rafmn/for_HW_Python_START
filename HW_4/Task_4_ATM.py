# Возьмите задачу о банкомате из семинара 2. Разбейте её
# на отдельные операции — функции. Дополнительно сохраняйте
# все операции поступления и снятия средств в список.


START_SUM = 0
count = 0
history = []

def add_money(account, count):
    money = int(input("Ведите сумму пополнения, кратную 50 у.е.: "))
    if count == 3:
        count = 0
    if money % 50 == 0:
        if count < 3:
            account += money
            history.append(money)
        else:
            account += money - money * 0.03
            history.append(money - money * 0.03)
            print("При пополнении удержано 3%")
        count += 1
    else:
        print("Некорректный ввод, повторите.")
    return account, count
            
      
def pop_money(account, count):
    if count == 3:
        count = 0
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

        history.append(-(money + percent))

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
    print("История всех операций: ", history)


def nalog(account):
    account -= (account - 5_000_000) * 0.1
    return account

account = START_SUM
while True:
    achoice = input("Выберете действие: 1 - пополнить, 2 - снять, 3 - выйти: ")
    match achoice:
        case '1':
            account, count = add_money(account, count)
            if account > 5_000_000:
                account = nalog(account)
                history.append(-(account - 5_000_000) * 0.1)
            print("Сумма на счету:", account, "у.е.")
        case '2':
            account, count = pop_money(account, count)
            if account > 5_000_000:
                account = nalog(account)
                history.append(-(account - 5_000_000) * 0.1)
            print("Сумма на счету:", account, "у.е.")
        case '3':
            exit(account)
        case _:
            if account > 5_000_000:
                account = nalog(account)
                history.append(-(account - 5_000_000) * 0.1)
            print("Неверный ввод. Сумма на счету:", account, "у.е.")
