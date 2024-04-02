import random


def funker1(a, b, c, d, e):
    answer = input('Мы разрабатываем сыворотку, способную повысить продуктивность коров. '
                   'Можно ее протестировать ?')
    if answer == 'yes':
        return [a-20, b-10, c, d+20, e]
    else:
        return [a, b+10, c, d - 15, e]


def funker2(a, b, c, d, e):
    answer = input('В интернете вас высмеивают и критикуют.'
                   'Наказать виновных?')
    if answer == 'yes':
        return [a, b-15, c, d+15, e]
    else:
        return [a, b+10, c, d - 10, e]


def funker3(a, b, c, d, e):
    answer = input('Нужно увеличить военный бюджет?')
    if answer == 'yes':
        return [a, b, c+15, d-20, e]
    else:
        return [a, b, c-20, d + 15, e]


def funker4(a, b, c, d, e):
    answer = input('Испытания ядерного оружия могли бы существенно продвинуть науку вперед.')
    if answer == 'yes':
        return [a-31, b-15, c, d+20, e]
    else:
        return [a+15, b+10, c, d - 15, e]


def funker5(a, b, c, d, e):
    answer = input('Население процветает, а правительству нужны деньги. Поднять налоги?')
    if answer == 'Поднять немного':
        return [a, b, c, d+10, e]
    elif answer == 'Удвоить':
        return [a, b-15, c, d + 20, e]


def funkers1(a, b, c, d, e):
    print('Прорвало платину и затопило несколько крупных деревень')
    return [a-5, b-10, c-5, d-5, e]


def funkers2(a, b, c, d, e):
    print('Ваши спортсмены выйграли крупное соревнование!')
    return [a, b+5, c, d+5, e+5]


def funkers3(a, b, c, d, e):
    print('Удача улыбается вам!')
    return [a+3, b+3, c+3, d+3, e]


def funkers4(a, b, c, d, e):
    print('Вы явно встали не с той ноги')
    return [a-4, b-4, c-4, d-4, e]


def funkers5(a, b, c, d, e):
    print('Кажется, вы контролируете ситуацию!')
    lost = [a, b, c, d, e]
    get_fr = int(input())
    get_to = int(input())
    change = 0
    change = lost[get_fr-1]
    lost[get_fr-1] = lost[get_to-1]
    lost[get_to-1] = change
    return lost


def f1(a, b, c, d, e, f, g, h, o, p):
    answer = input('Ввести санкции?')
    if answer == 'Да':
        return [a, b, c, d-5, e+15], [f, g-5, h, o-10, p-10]
    else:
        return [a, b, c, d, e-20], [f, g, h, o, p]


def f2(a, b, c, d, e, f, g, h, o, p):
    answer = input('Устроить бомбордировку?')
    if answer == 'Да':
        return [a, b-5, c+5, d-5, e-30], [f-10, g-5, h-10, o-10, p+20]
    else:
        return [a, b, c, d, e], [f, g, h, o, p]


def f3(a, b, c, d, e, f, g, h, o, p):
    answer = input('Дать в долг?')
    if answer == 'Да':
        return [a, b, c, d-10, e+20], [f, g+5, h, o+10, p]
    else:
        return [a, b+10, c, d, e], [f, g, h, o, p]


def f4(a, b, c, d, e, f, g, h, o, p):
    answer = input('Провести товарищеский матч?')
    if answer == 'Да':
        return [a, b+5, c, d-10, e+15], [f, g+5, h, o-10, p+15]
    else:
        return [a, b-5, c, d, e], [f, g-5, h, o, p]


def f5(a, b, c, d, e, f, g, h, o, p):
    answer = input('Выбросить отходы?')
    if answer == 'Да':
        return [a+15, b+5, c, d+5, e-15], [f-15, g-5, h, o-5, p+10]
    else:
        return [a-10, b-5, c, d-5, e], [f, g, h, o, p]


teams = int(input('Здравствуйте! Введите количество команд '))
years = int(input('Здравствуйте! Введите необходимый срок правления '))
functions1 = {'fun_1': funker1, 'fun_2': funker2, 'fun_3': funker3, 'fun_4': funker4, 'fun_5': funker5}
functions2 = {'funk_1': funkers1, 'funk_2': funkers2, 'funk_3': funkers3, 'funk_4': funkers4, 'funk_5': funkers5}
functions3 = {'funke_1': f1, 'funke_2': f2, 'funke_3': f3, 'funke_4': f4, 'funke_5': f5}
func_name_1 = ['fun_1', 'fun_2', 'fun_3', 'fun_4', 'fun_5']
func_name_2 = ['funk_1', 'funk_2', 'funk_3', 'funk_4', 'funk_5']
func_name_3 = ['funke_1', 'funke_2', 'funke_3', 'funke_4', 'funke_5']
points = [[50, 50, 50, 50, 50]] * teams
condition = ['alive'] * teams
results = [0] * teams
for i in range(years):
    if ('alive' in condition) == 0:
        print('К сожалению, выживших не осталось')
        break
    for j in range(teams):
        if condition == 'dead':
            continue
        print(f'Приветствую, команда номер {j+1}.')
        print(f'Ваши очки: \n'
              f'Экология: {points[j][0]} \n'
              f'Жители: {points[j][1]} \n'
              f'Армия: {points[j][2]} \n'
              f'Казна: {points[j][3]} \n'
              f'Репутация: {points[j][4]}')
        func = random.choice(func_name_1)
        points[j] = functions1[func](points[j][0], points[j][1], points[j][2], points[j][3], points[j][4])
        print(f'Ваши очки: \n'
              f'Экология: {points[j][0]} \n'
              f'Жители: {points[j][1]} \n'
              f'Армия: {points[j][2]} \n'
              f'Казна: {points[j][3]} \n'
              f'Репутация: {points[j][4]}')
        if (points[j][0] <= 0 or points[j][0] >= 100 or points[j][1] <= 0
                or points[j][1] >= 100 or points[j][2] <= 0
                or points[j][2] >= 100 or points[j][3] <= 0
                or points[j][3] >= 100 or points[j][4] <= 0
                or points[j][4] >= 100):
            condition[j] = 'dead'
            print(f'Поздравляю, вы прожили {i} лет!')
            continue
        func = random.choice(func_name_2)
        points[j] = functions2[func](points[j][0], points[j][1], points[j][2], points[j][3], points[j][4])
        print(f'Ваши очки: \n'
              f'Экология: {points[j][0]} \n'
              f'Жители: {points[j][1]} \n'
              f'Армия: {points[j][2]} \n'
              f'Казна: {points[j][3]} \n'
              f'Репутация: {points[j][4]}')
        if (points[j][0] <= 0 or points[j][0] >= 100 or points[j][1] <= 0
                or points[j][1] >= 100 or points[j][2] <= 0
                or points[j][2] >= 100 or points[j][3] <= 0
                or points[j][3] >= 100 or points[j][4] <= 0
                or points[j][4] >= 100):
            condition[j] = 'dead'
            print(f'Поздравляю, вы прожили {i} лет!')
            continue
        func = random.choice(func_name_1)
        points[j] = functions1[func](points[j][0], points[j][1], points[j][2], points[j][3], points[j][4])
        print(f'Ваши очки: \n'
              f'Экология: {points[j][0]} \n'
              f'Жители: {points[j][1]} \n'
              f'Армия: {points[j][2]} \n'
              f'Казна: {points[j][3]} \n'
              f'Репутация: {points[j][4]}')
        if (points[j][0] <= 0 or points[j][0] >= 100 or points[j][1] <= 0
                or points[j][1] >= 100 or points[j][2] <= 0
                or points[j][2] >= 100 or points[j][3] <= 0
                or points[j][3] >= 100 or points[j][4] <= 0
                or points[j][4] >= 100):
            condition[j] = 'dead'
            print(f'Поздравляю, вы прожили {i} лет!')
            continue
        func = random.choice(func_name_3)
        t = int(input('Введите номер команды, с которой хотите произвести действие: '))
        points[j], points[t-1] = functions3[func](points[j][0], points[j][1], points[j][2], points[j][3], points[j][4],
                                    points[t-1][0], points[t-1][1], points[t-1][2], points[t-1][3], points[t-1][4])
        print(f'Ваши очки: \n'
              f'Экология: {points[j][0]} \n'
              f'Жители: {points[j][1]} \n'
              f'Армия: {points[j][2]} \n'
              f'Казна: {points[j][3]} \n'
              f'Репутация: {points[j][4]}')
        if (points[j][0] <= 0 or points[j][0] >= 100 or points[j][1] <= 0
                or points[j][1] >= 100 or points[j][2] <= 0
                or points[j][2] >= 100 or points[j][3] <= 0
                or points[j][3] >= 100 or points[j][4] <= 0
                or points[j][4] >= 100):
            condition[j] = 'dead'
            print(f'Поздравляю, вы прожили {i} лет!')
            continue
        results[j] += 1
print(f'Результаты команд:')
for k in range(teams):
    if 11 <= (results[k] % 100) <= 19:
        print(f'Команда номер {k+1} прожила - {results[k]} лет')
    elif results[k] % 10 == 1:
        print(f'Команда номер {k + 1} прожила - {results[k]} год')
    elif results[k] % 10 == 2 or results[k] % 10 == 3 or results[k] % 10 == 4:
        print(f'Команда номер {k + 1} прожила - {results[k]} года')
    elif (results[k] % 10 == 5 or results[k] % 10 == 6 or results[k] % 10 == 7
          or results[k] % 10 == 8 or results[k] % 10 == 9 or results[k] % 10 == 0):
        print(f'Команда номер {k + 1} прожила - {results[k]} лет')
