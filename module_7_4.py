team1 = 'Мастера кода'
team2 = 'Волшебники данных'
team1_num = 4
names_team1 = 'Den', 'Max','Olga', 'Dina'
names_team2 = 'Mille', 'Masha','Nic', 'Rob', 'Ron', 'Veronica'
team2_num = 6
score_1 = 50
score_2 = 48
team1_time = 2040
team2_time = 2096
tasks_total = score_1 + score_2
time1_avg = team1_time/score_1
time2_avg = team2_time/score_2
time_avg = ((time1_avg + time2_avg))/2

if score_1 >= score_2 and time1_avg < time2_avg:
    result = 'Победа команды Мастера кода!'
elif score_1 <= score_2 and team1_time > team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'


print(time_avg)
print("В команде %s участников: %s !" % (team1, team1_num))
print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))
print('В команде Мастера кода были: %s, %s, %s, %s !'% (names_team1))
print('Команда {} решила задач: {} !'.format(team2, score_2))
print('Волшебники данных решили задачи за {} с !'.format(team2_time))
print('В команде Волшебники были {} !'.format(names_team2))
print(f'Команды решили {score_1} и {score_2} задач!')
print(f'Команды решили {tasks_total} задач за {team1_time + team2_time} секунд!')
print(f'Среднее время решения {tasks_total} задач составило {time_avg} секунд!')
print(f'Мастера кода молодцы, в составе {team1_num} человек за {team1_time} секунд решили целых {score_1} задач!!!')
print(result)