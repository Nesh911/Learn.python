def get_answer():
    answer = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}

    question = (input(":")).lower()

    if question in answer:
        print(answer[question])
    else:
        print("Сложна!")
    # if question == "как дела":
    #     print(answer["Лучше всех"])
    # if question == "пока":
    #     print(answer["Увидимся" ])
    # if question != 'привет' or 'как дела' or 'пока':
    #     print('Сложна!')

get_answer()