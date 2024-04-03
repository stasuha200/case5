import random


def funker1(a, b, c, d, e):
    answer = input('Мы разрабатываем сыворотку, способную повысить продуктивность коров. '
                   'Можно ее протестировать ? \n'
                   '1 - Да \n'
                   '0 - Нет')
    if answer == '1':
        return [a-20, b-10, c, d+20, e]
    else:
        return [a, b+10, c, d - 15, e]


def funker2(a, b, c, d, e):
    answer = input('В интернете вас высмеивают и критикуют.'
                   'Наказать виновных? \n'
                   '1 - Да \n'
                   '0 - Нет'
                   )
    if answer == '1':
        return [a, b-15, c, d+15, e]
    else:
        return [a, b+10, c, d - 10, e]


def funker3(a, b, c, d, e):
    answer = input('Нужно увеличить военный бюджет? \n'
                   '1 - Да \n'
                   '0 - Нет'
                   )
    if answer == '1':
        return [a, b, c+15, d-20, e]
    else:
        return [a, b, c-20, d + 15, e]


def funker4(a, b, c, d, e):
    answer = input('Испытания ядерного оружия могли бы существенно продвинуть науку вперед. \n'
                   '1 - Да \n'
                   '0 - Нет'
                   )
    if answer == '1':
        return [a-31, b-15, c, d+20, e]
    else:
        return [a+15, b+10, c, d - 15, e]


def funker5(a, b, c, d, e):
    answer = input('Население процветает, а правительству нужны деньги. Поднять налоги? \n'
                   '1 - Поднять немного \n'
                   '0 - Удвоить'
                   )
    if answer == '1':
        return [a, b, c, d+10, e]
    elif answer == '0':
        return [a, b-15, c, d + 20, e]


def funker6(a, b, c, d, e):
    answer = input('Ваша страна столкнулась с нестабильностью в регионе из-за конфликта с соседним государством. \n '
                   'Вы можете либо увеличить бюджет на оборону и усилить армию для обеспечения безопасности страны'
                   ' либо попытаться решить конфликт мирным путем \n'
                   '1 - Усилить армию и оборону \n'
                   '0 - Решить конфликт мирным путем')
    if answer == '1':
        return [a, b - 20, c, d - 20, e + 20]
    elif answer == '0':
        return [a, b - 10, c, d + 20, e - 20]


def funker7(a, b, c, d, e):
    answer = input('Ваша страна сталкивается с экономическим кризисом из-за мировой финансовой нестабильности. \n '
                   'Вы можете либо сократить расходы на оборону и армию для экономии средств, '
                   'либо увеличить инвестиции в армию для обеспечения безопасности страны. \n'
                   '1 - Сократить расходы на армию \n'
                   '0 - Увеличить инвестиции в армию')
    if answer == '1':
        return [a, b + 20, c - 20, d + 20, e]
    elif answer == '0':
        return [a, b - 20, c, d - 20, e + 20]


def funker8(a, b, c, d, e):
    answer = input('В вашей стране возникла необходимость в проведении крупного инфраструктурного проекта'
                   ' для экономического развития. \n Вы можете либо выделить средства из казны на развитие инфраструктуры, '
                   'либо сократить расходы на развитие и увеличить бюджет на армию для обеспечения безопасности. \n'
                   '1 - Инвестировать в инфраструктуру \n'
                   '0 - Увеличить бюджет на армию')
    if answer == '1':
        return [a, b + 15, c, d - 20, e]
    elif answer == '0':
        return [a, b, c, d - 15, e + 20]


def funker9(a, b, c, d, e):
    answer = input(' Ваша страна получила предложение о заключении торгового соглашения с крупным экспортером, '
                   'что может принести дополнительные доходы. \n Вы можете либо подписать соглашение,'
                   ' либо отказаться от соглашения в защиту своих производителей. \n'
                   '1 - Подписать торговое соглашение \n'
                   '0 - Отказаться от соглашения')
    if answer == '1':
        return [a, b - 15, c, d + 20, e + 20]
    elif answer == '0':
        return [a, b + 15, c, d - 20, e-5]


def funker10(a, b, c, d, e):
    answer = input(' В вашей стране возникла угроза кибератак со стороны международных хакеров. \n '
                   'Вы можете либо увеличить финансирование кибербезопасности и обучение специалистов, '
                   'либо сосредоточиться на увеличении численности армии для обеспечения безопасности национальной территории. \n'
                   '1 - Увеличить финансирование кибербезопасности \n'
                   '0 - Увеличить численность армии')
    if answer == '1':
        return [a, b, c, d - 25, e + 15]
    elif answer == '0':
        return [a, b, c + 20, d - 15, e]


def funker11(a, b, c, d, e):
    answer = input('Ваша страна столкнулась с непредвиденным природным катаклизмом, '
                   'вызвавшим значительные разрушения. \n Вы можете либо направить финансы на восстановление городов'
                   'и помощь пострадавшим, либо использовать средства для усиления армии и подготовки к возможным будущим бедствиям. \n'
                   '1 - Помощь пострадавшим \n'
                   '0 - Усилить армию')
    if answer == '1':
        return [a, b + 20, c, d - 20, e + 25]
    elif answer == '0':
        return [a, b, c + 25, d - 25, e]


def funker12(a, b, c, d, e):
    answer = input('Ваша страна получила приглашение принять участие в миротворческой операции в конфликтной зоне. \n'
                   'Вы можете либо отправить часть армии для участия в миссии, '
                   'либо отказаться от участия в операции и сконцентрироваться на укреплении национальной безопасности. \n'
                   '1 - Участвовать в миротворческой операции \n'
                   '0 - Сосредоточиться на национальной безопасности')
    if answer == '1':
        return [a, b, c - 20, d, e + 20]
    elif answer == '0':
        return [a, b, c + 20, d, e - 20]


def funker13(a, b, c, d, e):
    answer = input('Страна столкнулась с эпидемией опасного вируса, и необходимо принять экстренные меры '
                   'для его контроля. \n Вы можете либо выделить средства на медицинскую помощь и разработку вакцины,'
                   'либо увеличить бюджет на оборону и контроль за порядком для предотвращения паники и беспорядков. \n'
                   '1 -  Выделить средства на медицину и вакцины \n'
                   '0 - Усилить контроль и бюджет на оборону')
    if answer == '1':
        return [a, b, c, d - 15, e + 20]
    elif answer == '0':
        return [a, b, c + 20, d - 15, e]


def funker14(a, b, c, d, e):
    answer = input(' В вашей стране возникла необходимость строительства новой ядерной электростанции '
                   'для обеспечения энергетической независимости. \n Вы можете либо выделить средства на строительство станции,'
                   'либо отказаться от строительства и направить средства на социальные программы для населения. \n'
                   '1 - Построить ядерную электростанцию \n'
                   '0 - Направить средства на социальные программы')
    if answer == '1':
        return [a, b + 20, c, d - 20, e + 15]
    elif answer == '0':
        return [a, b - 20, c + 20, d, e]


def funker15(a, b, c, d, e):
    answer = input('В вашей стране возникла потребность в создании программы нацеленной на борьбу'
                   'с бедностью и безработицей. \n Вы можете либо выделить часть казны на социальные выплаты '
                   'и программы поддержки малоимущих, либо использовать средства на увеличение численности армии '
                   'для обеспечения стабильности и безопасности.'
                   '1 - Создать программу борьбы с бедностью \n'
                   '0 - Увеличить численность армии')
    if answer == '1':
        return [a, b + 15, c, d - 20, e + 20]
    elif answer == '0':
        return [a, b, c + 15, d - 20, e]


def funker16(a, b, c, d, e):
    answer = input('Ваша страна столкнулась с необходимостью реформы образовательной системы. \n'
                   'Вы можете либо выделить средства на строительство новых школ и улучшение качества обучения,'
                   ' либо направить средства на оборону и укрепление армии. \n'
                   '1 - Реформировать образовательную систему \n'
                   '0 - Укрепить армию')
    if answer == '1':
        return [a, b, c, d + 10, e]
    elif answer == '0':
        return [a, b, c + 20, d - 20, e]


def funker17(a, b, c, d, e):
    answer = input(' Ваша страна получила предложение о строительстве международного моста, '
                   'который будет способствовать развитию экономики и туризма, но требует значительных финансовых затрат. \n'
                   'Вы можете либо согласиться на строительство моста, либо отказаться от проекта и направить средства на другие цели. \n'
                   '1 - Построить международный мост \n'
                   '0 - Отказаться от проекта')
    if answer == '1':
        return [a, b, c, d - 20, e + 15]
    elif answer == '0':
        return [a, b, c, d + 20, e - 15]


def funker18(a, b, c, d, e):
    answer = input('Ваша страна столкнулась с возросшим уровнем преступности и ростом террористических угроз. \n'
                   'Вы должны выбрать, улучшить обучение и оборудование полицейских для борьбы с преступностью'
                   'или увеличить финансирование армии для борьбы с террористическими угрозами. \n'
                   '1 - Улучшить полицию \n'
                   '0 - Увеличить финансирование армии')
    if answer == '1':
        return [a, b, c, d - 15, e + 10]
    elif answer == '0':
        return [a, b, c + 15, d - 15, e]


def funker19(a, b, c, d, e):
    answer = input(' Ваша страна столкнулась с серьезным экономическим кризисом из-за глобальных финансовых потрясений. \n'
                   'Вы можете либо ввести жесткие экономические меры, такие как сокращение социальных программ и повышение налогов,'
                   'либо обратиться к международным инвесторам и занять деньги. \n'
                   '1 - Ввести экономические меры \n'
                   '0 - Обратиться к международным инвесторам')
    if answer == '1':
        return [a, b - 20, c, d + 20, e]
    elif answer == '0':
        return [a, b, c, d - 35, e]


def funker20(a, b, c, d, e):
    answer = input(' В вашей стране нехватка воды и возникла необходимость строительства новых водохранилищ '
                   'и улучшения системы водоснабжения. \n Вы можете либо выделить средства на проекты водоподготовки и сбережения воды,'
                   'либо использовать средства на улучшение военной техники и вооружений. \n'
                   '1 - Строительство водохранилищ \n'
                   '0 - Улучшение военной техники')
    if answer == '1':
        return [a, b + 10, c, d - 20, e + 10]
    elif answer == '0':
        return [a, b, c + 20, d - 20, e]


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
    answer = input('Ввести санкции? \n'
                   '1 - Да \n'
                   '0 - Нет'
                   )
    if answer == '1':
        return [a, b, c, d-5, e+15], [f, g-5, h, o-10, p-10]
    else:
        return [a, b, c, d, e-20], [f, g, h, o, p]


def f2(a, b, c, d, e, f, g, h, o, p):
    answer = input('Устроить бомбордировку? \n'
                   '1 - Да \n'
                   '0 - Нет'
                   )
    if answer == '1':
        return [a, b-5, c+5, d-5, e-30], [f-10, g-5, h-10, o-10, p+20]
    else:
        return [a, b, c, d, e], [f, g, h, o, p]


def f3(a, b, c, d, e, f, g, h, o, p):
    answer = input('Дать в долг? \n'
                   '1 - Да \n'
                   '0 - Нет'
                   )
    if answer == '1':
        return [a, b, c, d-10, e+20], [f, g+5, h, o+10, p]
    else:
        return [a, b+10, c, d, e], [f, g, h, o, p]


def f4(a, b, c, d, e, f, g, h, o, p):
    answer = input('Провести товарищеский матч? \n'
                   '1 - Да \n'
                   '0 - Нет'
                   )
    if answer == '1':
        return [a, b+5, c, d-10, e+15], [f, g+5, h, o-10, p+15]
    else:
        return [a, b-5, c, d, e], [f, g-5, h, o, p]


def f5(a, b, c, d, e, f, g, h, o, p):
    answer = input('Выбросить отходы? \n'
                   '1 - Да \n'
                   '0 - Нет'
                   )
    if answer == '1':
        return [a+15, b+5, c, d+5, e-15], [f-15, g-5, h, o-5, p+10]
    else:
        return [a-10, b-5, c, d-5, e], [f, g, h, o, p]


def diplomacy(a, b, c, d, e, f, g, h, o, p):
    answer = input('Близлежащая страна предложила установить дипломатические отношения. \n'
                   '1 - Поддержать дипломатические отношения \n'
                   '0 - Отказаться от предложения')
    if answer == '1':
        return [a, b, c, d+15, e+20], [f, g, h, o+15, p]
    else:
        return [a, b, c, d, e-20], [f, g, h, o, p]


def negotiations(a, b, c, d, e, f, g, h, o, p):
    answer = input('Союз стран предложил провести переговоры для решения глобальной экологической проблемы.'
                   'Он нуждается в финансировании другими странами.\n'
                   '1 - Согласиться на переговоры\n'
                   '0 - Отказаться от переговоров')
    if answer == '1':
        return [a+20, b, c, d-15, e+15], [f+20, g, h, o, p]
    else:
        return [a-20, b-5, c, d, e+15], [f-20, g-5, h, o, p]


def trade(a, b, c, d, e, f, g, h, o, p):
    answer = input('Появилась возможность развить новые торговые отношения с соседней страной.\n'
                   '1 - Расширить торговые связи\n'
                   '0 - Оставить прежние торговые отношения')
    if answer == '1':
        return [a, b+5, c, d+30, e+10], [f, g+5, h, o+30, p]
    else:
        return [a, b, c, d-10, e-10], [f, g, h, o-10, p]


def project(a, b, c, d, e, f, g, h, o, p):
    answer = input('Вашей стране поступило предложение принять участие в рискованном экономическом проекте.\n'
                   '1 - Согласиться на авантюру\n'
                   '0 - Отказаться от предложения')
    if answer == '1':
        print('Экономический проект провалился.')
        return [a, b, c, d-20, e-10], [f, g, h, o-20, p-10]
    else:
        return [a, b, c, d, e-10], [f, g, h, o, p]


def festival(a, b, c, d, e, f, g, h, o, p):
    answer = input('Граждане просят у вас разрешение провести международный фестиваль'
                   ' с целью обмена культурами в соотрудничестве с народами других стран \n'
                   '1 - Дать добро \n'
                   '0 - Отказать')
    if answer == '1':
        return [a, b, c, d-20, e+20], [f, g, h, o-20, p+20]
    else:
        return [a, b, c, d, e-10], [f, g, h, o, p]


def aid(a, b, c, d, e, f, g, h, o, p):
    answer = input('Вас просят о военной помощи ваш союзник. \n'
                   '1 - Помочь \n'
                   '0 - Отказать')
    if answer == '1':
        return [a, b, c-30, d-20, e+30], [f, g, h+30, o+20, p-10]
    else:
        return [a, b, c, d, e-10], [f, g-20, h-30, o, p]


def calamity(a, b, c, d, e, f, g, h, o, p):
    answer = input('Во многих странах произошло стихийное бедствие. \n'
                   '1 - Предоставить гуманитарную помощь \n'
                   '0 - Не помогать')
    if answer == '1':
        return [a, b, c, d-20, e+20], [f+15, g, h, o, p]
    else:
        return [a, b, c, d, e-20], [f-15, g-20, h, o-10, p]


def peace(a, b, c, d, e, f, g, h, o, p):
    answer = input('Вы можете принять участие в миротворческих миссиях '
                   'для предотвращения конфликтов между странами. \n'
                   '1 - Принять участие \n'
                   '0 - Не принимать участия')
    if answer == '1':
        return [a, b, c, d-10, e+20], [f, g, h, o, p]
    else:
        return [a, b, c, d, e-20], [f, g-20, h, o, p]


def war(a, b, c, d, e, f, g, h, o, p):
    answer = input('На вас напала соседняя страна своими вооружёнными силами. \n'
                   '1 - Напасть в ответ \n'
                   '0 - Защищаться и предложить мирные переговоры')
    if answer == '1':
        return [a-10, b-20, c-30, d-10, e-20], [f-10, g-20, h-30, o-10, p-20]
    else:
        return [a, b, c, d, e+30], [f, g, h, o, p]


def levy(a, b, c, d, e, f, g, h, o, p):
    answer = input('В вашей стране кризисная ситуация в экономике. '
                   'Вы можете поднять таможенную пошлину для других стран. \n'
                   '1 - Увеличить налог \n'
                   '0 - Оставить прежнюю ставку')
    if answer == '1':
        return [a, b, c, d+20, e-20], [f, g, h, o-20, p]
    else:
        return [a, b, c, d, e+10], [f, g, h, o, p]


teams = int(input('Здравствуйте! Введите количество команд '))
years = int(input('Здравствуйте! Введите необходимый срок правления '))
functions1 = {'fun_1': funker1, 'fun_2': funker2, 'fun_3': funker3, 'fun_4': funker4, 'fun_5': funker5,
              'fun_6': funker6, 'fun_7': funker7, 'fun_8': funker8, 'fun_9': funker9, 'fun_10': funker10,
              'fun_11': funker11, 'fun_12': funker12, 'fun_13': funker13, 'fun_14': funker14, 'fun_15': funker15,
              'fun_16': funker16, 'fun_17': funker17, 'fun_18': funker18, 'fun_19': funker19, 'fun_20': funker20}
functions2 = {'funk_1': funkers1, 'funk_2': funkers2, 'funk_3': funkers3, 'funk_4': funkers4, 'funk_5': funkers5,
              'funk_6': rand1, 'funk_7': rand2, 'funk_8': rand3, 'funk_9': rand4, 'funk_10': rand5,
              'funk_11': rand6}
functions3 = {'funke_1': f1, 'funke_2': f2, 'funke_3': f3, 'funke_4': f4, 'funke_5': f5,
              'funke_6': diplomacy, 'funke_7': negotiations, 'funke_8': trade, 'funke_9': project, 'funke_10': festival,
              'funke_11': aid, 'funke_12': calamity, 'funke_13': peace, 'funke_14': war, 'funke_15': levy}
func_name_1 = ['fun_1', 'fun_2', 'fun_3', 'fun_4', 'fun_5',
               'fun_6', 'fun_7', 'fun_8', 'fun_9', 'fun_10',
               'fun_11', 'fun_12', 'fun_13', 'fun_14', 'fun_15',
               'fun_16', 'fun_17', 'fun_18', 'fun_19', 'fun_20']
func_name_2 = ['funk_1', 'funk_2', 'funk_3', 'funk_4', 'funk_5',
               'funk_6', 'funk_7', 'funk_8', 'funk_9', 'funk_10',
               'funk11']
func_name_3 = ['funke_1', 'funke_2', 'funke_3', 'funke_4', 'funke_5',
               'funke_6', 'funke_7', 'funke_8', 'funke_9', 'funke_10',
               'funke_11', 'funke_12', 'funke_13', 'funke_14', 'funke_15']
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
