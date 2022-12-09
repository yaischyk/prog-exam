w1 = input("Введіть перше слово: ")
w2 = input("Введіть друге слово: ")

if w1 == "word1" and w2 == "word2":
    try:
        file = open("data.txt")
        text = file.read()

        result = text.replace(w1, w2)
        print(result)
    except Exception as e:
        print("Помилка: " + str(e))
else:
    print("Ви ввели неправильні параметри.")
