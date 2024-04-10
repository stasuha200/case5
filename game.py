# Case-study #5
# Developers: Denisova D., Ukhov S., Simonov A., Zlygosteva M.
#
import random
import ru_local as ru


def cows(a, b, c, d, e):
    answer = input(f'{ru.SERUM}')
    if answer == '1':
        return [a-20, b-10, c, d+20, e]
    else:
        return [a, b+10, c, d - 15, e]


def critics(a, b, c, d, e):
    answer = input(f'{ru.INTERNET}')
    if answer == '1':
        return [a, b-15, c, d+15, e]
    else:
        return [a, b+10, c, d - 10, e]


def augmentation(a, b, c, d, e):
    answer = input(f'{ru.BUDGET}')
    if answer == '1':
        return [a, b, c+15, d-20, e]
    else:
        return [a, b, c-20, d + 15, e]


def science(a, b, c, d, e):
    answer = input(f'{ru.WEAPONS}')
    if answer == '1':
        return [a-31, b-15, c, d+20, e]
    else:
        return [a+15, b+10, c, d - 15, e]


def prosperity(a, b, c, d, e):
    answer = input(f'{ru.MONEY}')
    if answer == '1':
        return [a, b, c, d+10, e]
    elif answer == '0':
        return [a, b-15, c, d + 20, e]


def conflict(a, b, c, d, e):
    answer = input(f'{ru.NESTABILITY}')
    if answer == '1':
        return [a, b - 20, c, d - 20, e + 20]
    elif answer == '0':
        return [a, b - 10, c, d + 20, e - 20]


def finances(a, b, c, d, e):
    answer = input(f'{ru.CRISIS}')
    if answer == '1':
        return [a, b + 20, c - 20, d + 20, e]
    elif answer == '0':
        return [a, b - 20, c, d - 20, e + 20]


def infrastructure(a, b, c, d, e):
    answer = input(f'{ru.PROJECT}')
    if answer == '1':
        return [a, b + 15, c, d - 20, e]
    elif answer == '0':
        return [a, b, c, d - 15, e + 20]


def exporter(a, b, c, d, e):
    answer = input(f'{ru.AGREEMENT}')
    if answer == '1':
        return [a, b - 15, c, d + 20, e + 20]
    elif answer == '0':
        return [a, b + 15, c, d - 20, e-5]


def hackers(a, b, c, d, e):
    answer = input(f'{ru.CYBERATACA}')
    if answer == '1':
        return [a, b, c, d - 25, e + 15]
    elif answer == '0':
        return [a, b, c + 20, d - 15, e]


def destructions(a, b, c, d, e):
    answer = input(f'{ru.CATACLISM}')
    if answer == '1':
        return [a, b + 20, c, d - 20, e + 25]
    elif answer == '0':
        return [a, b, c + 25, d - 25, e]


def zone(a, b, c, d, e):
    answer = input(f'{ru.OPERATION}')
    if answer == '1':
        return [a, b, c - 20, d, e + 20]
    elif answer == '0':
        return [a, b, c + 20, d, e - 20]


def epidemic(a, b, c, d, e):
    answer = input(f'{ru.VIRUS}')
    if answer == '1':
        return [a, b, c, d - 15, e + 20]
    elif answer == '0':
        return [a, b, c + 20, d - 15, e]


def energy(a, b, c, d, e):
    answer = input(f'{ru.ELECTROSTATION}')
    if answer == '1':
        return [a, b + 20, c, d - 20, e + 15]
    elif answer == '0':
        return [a, b - 20, c + 20, d, e]


def struggle(a, b, c, d, e):
    answer = input(f'{ru.PROGRAMME}')
    if answer == '1':
        return [a, b + 15, c, d - 20, e + 20]
    elif answer == '0':
        return [a, b, c + 15, d - 20, e]


def education(a, b, c, d, e):
    answer = input(f'{ru.REFORM}')
    if answer == '1':
        return [a, b, c, d + 10, e]
    elif answer == '0':
        return [a, b, c + 20, d - 20, e]


def development(a, b, c, d, e):
    answer = input(f'{ru.MOST}')
    if answer == '1':
        return [a, b, c, d - 20, e + 15]
    elif answer == '0':
        return [a, b, c, d + 20, e - 15]


def threats(a, b, c, d, e):
    answer = input(f'{ru.CRIMINALITY}')
    if answer == '1':
        return [a, b, c, d - 15, e + 10]
    elif answer == '0':
        return [a, b, c + 15, d - 15, e]


def crisis(a, b, c, d, e):
    answer = input(f'{ru.CONTRIBUTIONS}')
    if answer == '1':
        return [a, b - 20, c, d + 20, e]
    elif answer == '0':
        return [a, b, c, d - 35, e]


def reservoir(a, b, c, d, e):
    answer = input(f'{ru.WATER}')
    if answer == '1':
        return [a, b + 10, c, d - 20, e + 10]
    elif answer == '0':
        return [a, b, c + 20, d - 20, e]


def villages(a, b, c, d, e):
    print(f'{ru.FLOATING}')
    return [a-5, b-10, c-5, d-5, e]


def competition(a, b, c, d, e):
    print(f'{ru.SPORTSMEN}')
    return [a, b+5, c, d+5, e+5]


def smile(a, b, c, d, e):
    print(f'{ru.LUCK}')
    return [a+3, b+3, c+3, d+3, e]


def failure(a, b, c, d, e):
    print(f'{ru.LEG}')
    return [a-4, b-4, c-4, d-4, e]


def control(a, b, c, d, e):
    print(f'{ru.CONTROL}')
    lost = [a, b, c, d, e]
    get_fr = int(input())
    get_to = int(input())
    change = 0
    change = lost[get_fr-1]
    lost[get_fr-1] = lost[get_to-1]
    lost[get_to-1] = change
    return lost


def fall(a, b, c, d, e):
    print(f'{ru.LADDER}')
    return [a, b, c, d, e - 10]


def overlap(a, b, c, d, e):
    print(f'{ru.BOBERS}')
    return [a - 10, b, c, d, e]


def stars(a, b, c, d, e):
    print(f'{ru.STARTING}')
    return [a, b, c, d - 10, e - 10]


def record(a, b, c, d, e):
    print(f'{ru.BORN}')
    return [a, b + 20, c, d, e]


def eggs(a, b, c, d, e):
    print(f'{ru.PANCAKES}')
    return [a + 10, b - 10, c, d, e]


def server(a, b, c, d, e):
    print(f'{ru.COFFEE}')
    return [a, b - 20, c, d - 10, e]


def tourist(a, b, c, d, e):
    print(f'{ru.ALPHABIT}')
    return [a, b-10, c, d, e+20]


def international(a, b, c, d, e):
    print(f'{ru.WINNER}')
    return [a, b, c, d+20, e+10]


def soup(a, b, c, d, e):
    print(f'{ru.ECOACTIVISTS}')
    return [a, b, c, d+10, e-10]


def armament(a, b, c, d, e):
    print(f'{ru.BUNKER}')
    return [a, b, c+20, d, e]


def prohibition(a, b, c, d, e):
    print(f'{ru.JUDO}')
    return [a, b, c+10, d+10, e+20]


def advantages(a, b, c, d, e):
    print(f'{ru.LAPTOP}')
    return [a, b, c, d+20, e+10]


def assemblage(a, b, c, d, e):
    print(f'{ru.FOOTBALL}')
    return [a, b+10, c, d-10, e+20]


def sanctionss(a, b, c, d, e, f, g, h, o, p):
    answer = input(f'{ru.SANCTIONS}')
    if answer == '1':
        return [a, b, c, d-5, e+15], [f, g-5, h, o-10, p-10]
    else:
        return [a, b, c, d, e-20], [f, g, h, o, p]


def bombardment(a, b, c, d, e, f, g, h, o, p):
    answer = input(f'{ru.BOMBORDING}')
    if answer == '1':
        return [a, b-5, c+5, d-5, e-30], [f-10, g-5, h-10, o-10, p+20]
    else:
        return [a, b, c, d, e], [f, g, h, o, p]


def duty(a, b, c, d, e, f, g, h, o, p):
    answer = input(f'{ru.MUST}')
    if answer == '1':
        return [a, b, c, d-10, e+20], [f, g+5, h, o+10, p]
    else:
        return [a, b+10, c, d, e], [f, g, h, o, p]


def match(a, b, c, d, e, f, g, h, o, p):
    answer = input(f'{ru.MATCH}')
    if answer == '1':
        return [a, b+5, c, d-10, e+15], [f, g+5, h, o-10, p+15]
    else:
        return [a, b-5, c, d, e], [f, g-5, h, o, p]


def ejection(a, b, c, d, e, f, g, h, o, p):
    answer = input(f'{ru.WASTES}')
    if answer == '1':
        return [a+15, b+5, c, d+5, e-15], [f-15, g-5, h, o-5, p+10]
    else:
        return [a-10, b-5, c, d-5, e], [f, g, h, o, p]


def diplomacy(a, b, c, d, e, f, g, h, o, p):
    answer = input(f'{ru.DIPLOMATY}')
    if answer == '1':
        return [a, b, c, d+15, e+20], [f, g, h, o+15, p]
    else:
        return [a, b, c, d, e-20], [f, g, h, o, p]


def negotiations(a, b, c, d, e, f, g, h, o, p):
    answer = input(f'{ru.TRANSACTIONS}')
    if answer == '1':
        return [a+20, b, c, d-15, e+15], [f+20, g, h, o, p]
    else:
        return [a-20, b-5, c, d, e+15], [f-20, g-5, h, o, p]


def trade(a, b, c, d, e, f, g, h, o, p):
    answer = input(f'{ru.TRADING}')
    if answer == '1':
        return [a, b+5, c, d+30, e+10], [f, g+5, h, o+30, p]
    else:
        return [a, b, c, d-10, e-10], [f, g, h, o-10, p]


def project(a, b, c, d, e, f, g, h, o, p):
    answer = input(f'{ru.ECONOMIC_PROJECT}')
    if answer == '1':
        print(f'{ru.FAILURE}')
        return [a, b, c, d-20, e-10], [f, g, h, o-20, p-10]
    else:
        return [a, b, c, d, e-10], [f, g, h, o, p]


def festival(a, b, c, d, e, f, g, h, o, p):
    answer = input(f'{ru.FESTIVAL}')
    if answer == '1':
        return [a, b, c, d-20, e+20], [f, g, h, o-20, p+20]
    else:
        return [a, b, c, d, e-10], [f, g, h, o, p]


def aid(a, b, c, d, e, f, g, h, o, p):
    answer = input(f'{ru.HELP}')
    if answer == '1':
        return [a, b, c-30, d-20, e+30], [f, g, h+30, o+20, p-10]
    else:
        return [a, b, c, d, e-10], [f, g-20, h-30, o, p]


def calamity(a, b, c, d, e, f, g, h, o, p):
    answer = input(f'{ru.FURIOUSNESS}')
    if answer == '1':
        return [a, b, c, d-20, e+20], [f+15, g, h, o, p]
    else:
        return [a, b, c, d, e-20], [f-15, g-20, h, o-10, p]


def peace(a, b, c, d, e, f, g, h, o, p):
    answer = input(f'{ru.MISSIONS}')
    if answer == '1':
        return [a, b, c, d-10, e+20], [f, g, h, o, p]
    else:
        return [a, b, c, d, e-20], [f, g-20, h, o, p]


def war(a, b, c, d, e, f, g, h, o, p):
    answer = input(f'{ru.ATTACK}')
    if answer == '1':
        return [a-10, b-20, c-30, d-10, e-20], [f-10, g-20, h-30, o-10, p-20]
    else:
        return [a, b, c, d, e+30], [f, g, h, o, p]


def levy(a, b, c, d, e, f, g, h, o, p):
    answer = input(f'{ru.ECONOMICS}')
    if answer == '1':
        return [a, b, c, d+20, e-20], [f, g, h, o-20, p]
    else:
        return [a, b, c, d, e+10], [f, g, h, o, p]


def alliance(a, b, c, d, e, f, g, h, o, p):
    answer = input(f'{ru.UNION}')
    if answer == '1':
        return [a, b, c, d+20, e+20], [f, g, h, o+20, p]
    else:
        return [a, b, c, d, e-10], [f, g, h, o, p]


def sanctions(a, b, c, d, e, f, g, h, o, p):
    answer = input(f'{ru.SANCTIONS2}')
    if answer == '1':
        return [a, b, c, d, e+30], [f, g, h, o-20, p]
    else:
        return [a, b, c, d-30, e-10], [f, g, h, o, p]


def branches(a, b, c, d, e, f, g, h, o, p):
    answer = input(f'{ru.COMPANIES}')
    if answer == '1':
        return [a, b, c, d+30, e+20], [f, g, h, o+20, p]
    else:
        return [a, b, c, d, e], [f, g, h, o, p]


def reparation(a, b, c, d, e, f, g, h, o, p):
    answer = input(f'{ru.LOSS}')
    if answer == '1':
        return [a, b, c, d+20, e-20], [f, g, h, o-20, p]
    else:
        return [a, b, c, d+20, e-10], [f, g, h, o-10, p]


def military_bloc(a, b, c, d, e, f, g, h, o, p):
    answer = input(f'{ru.PROPOSAL}')
    if answer == '1':
        print(f'{ru.WAR}')
        return [a, b-10, c-30, d, e+20], [f, g-10, h+20, o, p]
    else:
        return [a, b, c, d, e-20], [f, g, h, o, p]
teams = int(input(f'{ru.TEAM}'))
years = int(input(f'{ru.DATE}'))
functions1 = {'fun_1': cows, 'fun_2': critics, 'fun_3': augmentation, 'fun_4': science, 'fun_5': prosperity,
              'fun_6': conflict, 'fun_7': finances, 'fun_8': exporter, 'fun_9': exporter, 'fun_10': hackers,
              'fun_11': destructions, 'fun_12': zone, 'fun_13': epidemic, 'fun_14': energy, 'fun_15': struggle,
              'fun_16': education, 'fun_17': development, 'fun_18': threats, 'fun_19': crisis, 'fun_20': reservoir}
functions2 = {'funk_1': villages, 'funk_2': competition, 'funk_3': smile, 'funk_4': failure, 'funk_5': control,
              'funk_6': fall, 'funk_7': overlap, 'funk_8': stars, 'funk_9': record, 'funk_10': eggs,
              'funk_11': server, 'funk_12': tourist, 'funk_13': international, 'funk_14': soup, 'funk_15': armament,
              'funk_16': prohibition, 'funk_17': advantages, 'funk_18': assemblage}
functions3 = {'funke_1': sanctionss, 'funke_2': bombardment, 'funke_3': duty, 'funke_4': match, 'funke_5': ejection,
              'funke_6': diplomacy, 'funke_7': negotiations, 'funke_8': trade, 'funke_9': project, 'funke_10': festival,
              'funke_11': aid, 'funke_12': calamity, 'funke_13': peace, 'funke_14': war, 'funke_15': levy,
              'funke_16': alliance, 'funke_17': sanctions, 'funke_18': branches, 'funke_19': reparation,
              'funke_20': military_bloc}
func_name_1 = ['fun_1', 'fun_2', 'fun_3', 'fun_4', 'fun_5',
               'fun_6', 'fun_7', 'fun_8', 'fun_9', 'fun_10',
               'fun_11', 'fun_12', 'fun_13', 'fun_14', 'fun_15',
               'fun_16', 'fun_17', 'fun_18', 'fun_19', 'fun_20']
func_name_2 = ['funk_1', 'funk_2', 'funk_3', 'funk_4', 'funk_5',
               'funk_6', 'funk_7', 'funk_8', 'funk_9', 'funk_10',
               'funk_11', 'funk_12', 'funk_13', 'funk_14', 'funk_15',
               'funk_16', 'funk_17', 'funk_18']
func_name_3 = ['funke_1', 'funke_2', 'funke_3', 'funke_4', 'funke_5',
               'funke_6', 'funke_7', 'funke_8', 'funke_9', 'funke_10',
               'funke_11', 'funke_12', 'funke_13', 'funke_14', 'funke_15',
               'funke_16', 'funke_17', 'funke_18', 'funke_19', 'funke_20']
points = [[50, 50, 50, 50, 50]] * teams
condition = ['alive'] * teams
results = [0] * teams
for i in range(years):
    if ('alive' in condition) == 0:
        print(f'{ru.SURVIVORS}')
        break
    for j in range(teams):
        if condition == 'dead':
            continue
        print(f'{ru.ANNOUNCEMENTS} {j+1}.')
        func = random.choice(func_name_2)
        points[j] = functions2[func](points[j][0], points[j][1], points[j][2], points[j][3], points[j][4])
        print(f'{ru.POINTS}: \n'
              f'{ru.ECOLOGY}: {points[j][0]} \n'
              f'{ru.RESIDENTS}: {points[j][1]} \n'
              f'{ru.ARMY}: {points[j][2]} \n'
              f'{ru.CAULDRON}: {points[j][3]} \n'
              f'{ru.REPUTATION}: {points[j][4]}')
        if (points[j][0] <= 0 or points[j][0] >= 100 or points[j][1] <= 0
                or points[j][1] >= 100 or points[j][2] <= 0
                or points[j][2] >= 100 or points[j][3] <= 0
                or points[j][3] >= 100 or points[j][4] <= 0
                or points[j][4] >= 100):
            condition[j] = 'dead'
            print(f'{ru.LIVED} {i} {ru.YEAR3}')
            continue
        func = random.choice(func_name_1)
        points[j] = functions1[func](points[j][0], points[j][1], points[j][2], points[j][3], points[j][4])
        print(f'{ru.POINTS}: \n'
              f'{ru.ECOLOGY}: {points[j][0]} \n'
              f'{ru.RESIDENTS}: {points[j][1]} \n'
              f'{ru.ARMY}: {points[j][2]} \n'
              f'{ru.CAULDRON}: {points[j][3]} \n'
              f'{ru.REPUTATION}: {points[j][4]}')
        if (points[j][0] <= 0 or points[j][0] >= 100 or points[j][1] <= 0
                or points[j][1] >= 100 or points[j][2] <= 0
                or points[j][2] >= 100 or points[j][3] <= 0
                or points[j][3] >= 100 or points[j][4] <= 0
                or points[j][4] >= 100):
            condition[j] = 'dead'
            print(f'{ru.LIVED} {i} {ru.YEAR3}')
            continue
        func = random.choice(func_name_1)
        points[j] = functions1[func](points[j][0], points[j][1], points[j][2], points[j][3], points[j][4])
        print(f'{ru.POINTS}: \n'
              f'{ru.ECOLOGY}: {points[j][0]} \n'
              f'{ru.RESIDENTS}: {points[j][1]} \n'
              f'{ru.ARMY}: {points[j][2]} \n'
              f'{ru.CAULDRON}: {points[j][3]} \n'
              f'{ru.REPUTATION}: {points[j][4]}')
        if (points[j][0] <= 0 or points[j][0] >= 100 or points[j][1] <= 0
                or points[j][1] >= 100 or points[j][2] <= 0
                or points[j][2] >= 100 or points[j][3] <= 0
                or points[j][3] >= 100 or points[j][4] <= 0
                or points[j][4] >= 100):
            condition[j] = 'dead'
            print(f'{ru.LIVED} {i} {ru.YEAR3}')
            continue
        func = random.choice(func_name_3)
        t = int(input(f'{ru.ACTION}'))
        points[j], points[t-1] = functions3[func](points[j][0], points[j][1], points[j][2], points[j][3], points[j][4],
                                    points[t-1][0], points[t-1][1], points[t-1][2], points[t-1][3], points[t-1][4])
        print(f'{ru.POINTS}: \n'
              f'{ru.ECOLOGY}: {points[j][0]} \n'
              f'{ru.RESIDENTS}: {points[j][1]} \n'
              f'{ru.ARMY}: {points[j][2]} \n'
              f'{ru.CAULDRON}: {points[j][3]} \n'
              f'{ru.REPUTATION}: {points[j][4]}')
        if (points[j][0] <= 0 or points[j][0] >= 100 or points[j][1] <= 0
                or points[j][1] >= 100 or points[j][2] <= 0
                or points[j][2] >= 100 or points[j][3] <= 0
                or points[j][3] >= 100 or points[j][4] <= 0
                or points[j][4] >= 100):
            condition[j] = 'dead'
            print(f'{ru.LIVED} {i} {ru.YEAR3}')
            continue
        results[j] += 1
print(f'{ru.RESULTS}')
for k in range(teams):
    if 11 <= (results[k] % 100) <= 19:
        print(f'{ru.NUMBER} {k+1} {ru.LIVED} - {results[k]} {ru.YEARS}')
    elif results[k] % 10 == 1:
        print(f'{ru.NUMBER} {k + 1} {ru.LIVED} - {results[k]} {ru.YEAR}')
    elif results[k] % 10 == 2 or results[k] % 10 == 3 or results[k] % 10 == 4:
        print(f'{ru.NUMBER} {k + 1} {ru.LIVED} - {results[k]} {ru.YEAR2}')
    elif (results[k] % 10 == 5 or results[k] % 10 == 6 or results[k] % 10 == 7
          or results[k] % 10 == 8 or results[k] % 10 == 9 or results[k] % 10 == 0):
        print(f'{ru.NUMBER} {k + 1} {ru.LIVED} - {results[k]} {ru.YEARS}')
