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


def funker6(a, b, c, d, e):
    answer = input('Ваша страна столкнулась с нестабильностью в регионе из-за конфликта с соседним государством. '
                   'Вы можете либо увеличить бюджет на оборону и усилить армию для обеспечения безопасности страны'
                   ' либо попытаться решить конфликт мирным путем'
                   '1 - Усилить армию и оборону'
                   '0 - Решить конфликт мирным путем')
    if answer == '1':
        return [a, b - 50, c, d - 50, e + 50]
    elif answer == '0':
        return [a, b - 50, c, d + 50, e - 50]


def funker7(a, b, c, d, e):
    answer = input('Ваша страна сталкивается с экономическим кризисом из-за мировой финансовой нестабильности. '
                   'Вы можете либо сократить расходы на оборону и армию для экономии средств, '
                   'либо увеличить инвестиции в армию для обеспечения безопасности страны.'
                   '1 - Сократить расходы на армию'
                   '0 - Увеличить инвестиции в армию')
    if answer == '1':
        return [a, b + 50, c - 50, d + 50, e]
    elif answer == '0':
        return [a, b - 50, c, d - 50, e + 50]


def funker8(a, b, c, d, e):
    answer = input('В вашей стране возникла необходимость в проведении крупного инфраструктурного проекта'
                   ' для экономического развития. Вы можете либо выделить средства из казны на развитие инфраструктуры, '
                   'либо сократить расходы на развитие и увеличить бюджет на армию для обеспечения безопасности.'
                   '1 - Инвестировать в инфраструктуру'
                   '0 - Увеличить бюджет на армию')
    if answer == '1':
        return [a, b + 50, c, d - 50, e]
    elif answer == '0':
        return [a, b, c, d - 50, e + 50]


def funker9(a, b, c, d, e):
    answer = input(' Ваша страна получила предложение о заключении торгового соглашения с крупным экспортером, '
                   'что может принести дополнительные доходы. Вы можете либо подписать соглашение,'
                   ' либо отказаться от соглашения в защиту своих производителей.'
                   '1 - Подписать торговое соглашение'
                   '0 - Отказаться от соглашения')
    if answer == '1':
        return [a, b - 50, c, d + 50, e + 50]
    elif answer == '0':
        return [a, b + 50, c, d - 50, e]


def funker10(a, b, c, d, e):
    answer = input(' В вашей стране возникла угроза кибератак со стороны международных хакеров. '
                   'Вы можете либо увеличить финансирование кибербезопасности и обучение специалистов, '
                   'либо сосредоточиться на увеличении численности армии для обеспечения безопасности национальной территории.'
                   '1 - Увеличить финансирование кибербезопасности'
                   '0 - Увеличить численность армии')
    if answer == '1':
        return [a, b, c, d - 50, e + 50]
    elif answer == '0':
        return [a, b, c + 50, d - 50, e]


def funker11(a, b, c, d, e):
    answer = input('Ваша страна столкнулась с непредвиденным природным катаклизмом, '
                   'вызвавшим значительные разрушения. Вы можете либо направить финансы на восстановление городов'
                   'и помощь пострадавшим, либо использовать средства для усиления армии и подготовки к возможным будущим бедствиям.'
                   '1 - Помощь пострадавшим'
                   '0 - Усилить армию')
    if answer == '1':
        return [a, b + 50, c, d - 50, e + 50]
    elif answer == '0':
        return [a, b, c + 50, d - 50, e]


def funker12(a, b, c, d, e):
    answer = input('Ваша страна получила приглашение принять участие в миротворческой операции в конфликтной зоне.'
                   'Вы можете либо отправить часть армии для участия в миссии, '
                   'либо отказаться от участия в операции и сконцентрироваться на укреплении национальной безопасности.'
                   '1 - Участвовать в миротворческой операции'
                   '0 - Сосредоточиться на национальной безопасности')
    if answer == '1':
        return [a, b, c - 50, d, e + 50]
    elif answer == '0':
        return [a, b, c + 50, d, e - 50]


def funker13(a, b, c, d, e):
    answer = input('Страна столкнулась с эпидемией опасного вируса, и необходимо принять экстренные меры '
                   'для его контроля. Вы можете либо выделить средства на медицинскую помощь и разработку вакцины,'
                   'либо увеличить бюджет на оборону и контроль за порядком для предотвращения паники и беспорядков.'
                   '1 -  Выделить средства на медицину и вакцины'
                   '0 - Усилить контроль и бюджет на оборону')
    if answer == '1':
        return [a, b, c, d - 50, e + 50]
    elif answer == '0':
        return [a, b, c + 50, d - 50, e]


def funker14(a, b, c, d, e):
    answer = input(' В вашей стране возникла необходимость строительства новой ядерной электростанции '
                   'для обеспечения энергетической независимости. Вы можете либо выделить средства на строительство станции,'
                   'либо отказаться от строительства и направить средства на социальные программы для населения.'
                   '1 - Построить ядерную электростанцию'
                   '0 - Направить средства на социальные программы')
    if answer == '1':
        return [a, b + 50, c, d - 50, e + 50]
    elif answer == '0':
        return [a, b - 50, c + 50, d, e]


def funker15(a, b, c, d, e):
    answer = input('В вашей стране возникла потребность в создании программы нацеленной на борьбу'
                   'с бедностью и безработицей. Вы можете либо выделить часть казны на социальные выплаты '
                   'и программы поддержки малоимущих, либо использовать средства на увеличение численности армии '
                   'для обеспечения стабильности и безопасности.'
                   '1 - Создать программу борьбы с бедностью'
                   '0 - Увеличить численность армии')
    if answer == '1':
        return [a, b + 50, c, d - 50, e + 50]
    elif answer == '0':
        return [a, b, c + 50, d - 50, e]


def funker16(a, b, c, d, e):
    answer = input('Ваша страна столкнулась с необходимостью реформы образовательной системы. '
                   'Вы можете либо выделить средства на строительство новых школ и улучшение качества обучения,'
                   ' либо направить средства на оборону и укрепление армии.'
                   '1 - Реформировать образовательную систему'
                   '0 - Укрепить армию')
    if answer == '1':
        return [a, b, c, d + 10, e]
    elif answer == '0':
        return [a, b, c + 50, d - 50, e]


def funker17(a, b, c, d, e):
    answer = input(' Ваша страна получила предложение о строительстве международного моста, '
                   'который будет способствовать развитию экономики и туризма, но требует значительных финансовых затрат. '
                   'Вы можете либо согласиться на строительство моста, либо отказаться от проекта и направить средства на другие цели.'
                   '1 - Построить международный мост'
                   '0 - Отказаться от проекта')
    if answer == '1':
        return [a, b, c, d - 50, e + 50]
    elif answer == '0':
        return [a, b, c, d + 50, e - 50]


def funker18(a, b, c, d, e):
    answer = input('Ваша страна столкнулась с возросшим уровнем преступности и ростом террористических угроз. '
                   'Вы должны выбрать, улучшить обучение и оборудование полицейских для борьбы с преступностью'
                   'или увеличить финансирование армии для борьбы с террористическими угрозами.'
                   '1 - Улучшить полицию'
                   '0 - Увеличить финансирование армии')
    if answer == '1':
        return [a, b, c, d - 50, e + 50]
    elif answer == '0':
        return [a, b, c + 50, d - 50, e]


def funker19(a, b, c, d, e):
    answer = input(' Ваша страна столкнулась с серьезным экономическим кризисом из-за глобальных финансовых потрясений.'
                   'Вы можете либо ввести жесткие экономические меры, такие как сокращение социальных программ и повышение налогов,'
                   'либо обратиться к международным инвесторам и занять деньги.'
                   '1 - Ввести экономические меры'
                   '0 - Обратиться к международным инвесторам')
    if answer == '1':
        return [a, b - 50, c, d + 50, e]
    elif answer == '0':
        return [a, b, c, d - 50, e]


def funker20(a, b, c, d, e):
    answer = input(' В вашей стране нехватка воды и возникла необходимость строительства новых водохранилищ '
                   'и улучшения системы водоснабжения. Вы можете либо выделить средства на проекты водоподготовки и сбережения воды,'
                   'либо использовать средства на улучшение военной техники и вооружений.'
                   '1 - Строительство водохранилищ'
                   '0 - Улучшение военной техники')
    if answer == '1':
        return [a, b + 50, c, d - 50, e + 50]
    elif answer == '0':
        return [a, b, c + 50, d - 50, e]


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


def rand1(a, b, c, d, e):
    print('Вы упали с лестницы')
    return [a, b, c, d, e - 10]


def rand2(a, b, c, d, e):
    print('Бобры построили платину, что привело к перекрытию реки')
    return [a - 10, b, c, d, e]


def rand3(a, b, c, d, e):
    print('Запуск «Союза» к МКС отменили из-за неблагоприятного расположения звезд')
    return [a, b, c, d - 10, e - 10]


def rand4(a, b, c, d, e):
    print(
        '«Двести тысяч уже родилось, ещё миллион на подходе»: в стране зафиксирован рекорд по рождаемости после послания президента')
    return [a, b + 20, c, d, e]


def rand5(a, b, c, d, e):
    print('Из ГОСТа для блинов убрали яйца')
    return [a + 10, b - 10, c, d, e]


def rand6(a, b, c, d, e):
    print(
        'Сисадмин пролил кофе на сервер: глава материнского дата-центра Интернета объяснил глобальный сбой в работе сети')
    return [a, b - 20, c, d - 10, e]


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
functions1 = {'fun_1': funker1, 'fun_2': funker2, 'fun_3': funker3, 'fun_4': funker4, 'fun_5': funker5,
              'fun_6': funker6, 'fun_7': funker7, 'fun_8': funker8, 'fun_9': funker9, 'fun_10': funker10,
              'fun_11': funker11, 'fun_12': funker12, 'fun_13': funker13, 'fun_14': funker14, 'fun_15': funker15,
              'fun_16': funker16, 'fun_17': funker17, 'fun_18': funker18, 'fun_19': funker19, 'fun_20': funker20}
functions2 = {'funk_1': funkers1, 'funk_2': funkers2, 'funk_3': funkers3, 'funk_4': funkers4, 'funk_5': funkers5,
              'funk_6': rand1, 'funk_7': rand2, 'funk_8': rand3, 'funk_9': rand4, 'funk_10': rand5,
              'funk_11': rand6}
functions3 = {'funke_1': f1, 'funke_2': f2, 'funke_3': f3, 'funke_4': f4, 'funke_5': f5}
func_name_1 = ['fun_1', 'fun_2', 'fun_3', 'fun_4', 'fun_5',
               'fun_6', 'fun_7', 'fun_8', 'fun_9', 'fun_10',
               'fun_11', 'fun_12', 'fun_13', 'fun_14', 'fun_15',
               'fun_16', 'fun_17', 'fun_18', 'fun_19', 'fun_20']
func_name_2 = ['funk_1', 'funk_2', 'funk_3', 'funk_4', 'funk_5',
               'funk_6', 'funk_7', 'funk_8', 'funk_9', 'funk_10',
               'funk11']
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