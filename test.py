
weather1 = {'city': 'Москва', 'temperature': '20', 'wind': 'восточный', 'date': '12.05.2017'}
weather2 = {'city': 'Рейкьявик', 'temperature': '20', 'wind': 'восточный', 'date': '12.05.2017'}
weather3 = {'city': 'Лахнасъярви', 'temperature': '20', 'wind': 'восточный', 'date': '12.05.2017'}

user = {'name1': weather1, 'name2': weather2, 'name3': weather3}

a = input('введите имя:')
if a not in user:
    print('A ты кто такой? C какого района будешь?')
else:
    print(a + ' ' + ' '.join(user[a].values()))