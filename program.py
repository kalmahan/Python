time = int(input("Ввести время"))
if time >= 1 and time <= 6:
    print("Ночь")
elif time >= 6 and time <= 9:
    print("утро")
elif time >= 9 and time <= 12:
    print("Полдень")
elif time >= 12 and time <= 15:
    print("Обед")
elif time >= 15 and time <= 18:
    print("Вечер")
elif time >= 18 and time <= 24:
    print("Полночь")
