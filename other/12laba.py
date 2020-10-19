import random #Импортируем библиотеку "Random" для случаного выбора букв
all_letters = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
def randomletter():
    s =""
    for i in range (5):
        s += random.choice (all_letters) #С помощью этой функции выбираем из строки 5 случайных букв и возвращаем слово
    return s

def letter(string):
    s=0
    for i in range (5):
        if string[i] in all_letters: #Функция проверяет, что каждый символ строки из 5 элементов - латинская буква
            s = s + 1
    if s == 5:
        return True
    else:
        return False
        
while True: #Бесконечный цикл, ждущий от пользователя верного ввода
    try:
        M = float(input("Введите размер матрицы (число в диапазоне от 2 до 5): ")) #На вход получает тип данных float
    except (ValueError, KeyboardInterrupt, EOFError): #Здесь исключаются ошибка типа "введено не число", комбинации ctrl+c, "enter"
        print("Неверный формат ввода")
    else:
        if (M - int(M) != 0.0) or not (2 <= M <= 5): #Проверка, является ли введенное число целым.
            print("Неверный формат ввода")
        else:
            print("Матрица задана корректно ")
            M = int(M) #И наконец число задано
            break

answer = -1
while answer not in (0, 1): #Аналогичен циклу выше, от пользователя требуется вверный вод(0 или 1)
    try:
        answer = float(input("Нажмите 0, если хотите заполнить матрицу случайными латинскими буквами. Если хотите заполнить матрицу самостоятельно, нажмите 1: "))
    except (ValueError, KeyboardInterrupt, EOFError):
        print("Неверный формат ввода")
    else:
        if (answer not in (0, 1)) or (answer - int(answer) !=0.0):
            print("Неверный формат ввода")
        else:
            print("Ответ получен")
            answer = int (answer)
            

a = [randomletter() for i in range(M ** 2)] #Заполнение списка случайными словами при заданной матрице

if answer == 1: #Заполнение матрицы вручную
    for i in range(M ** 2):
        while True:
            try:
                slovo = input("Введите слово из 5 латинских букв: ")
            except (KeyboardInterrupt, EOFError):
                print("Неверный формат ввода")

            else:
                if len (slovo) != 5:
                    print("Неверный формат ввода. Слово должно содержать 5 букв.") 
                elif len (slovo) == 5 and letter (slovo) is False:
                    print("Неверный формат ввода. Слово должно состоять из букв латинского алфавита") #Применяется функция для проверки всех символов
                else:
                    print ("Слово введено")
                    a[i] = slovo
                    break
letters = {"A", "a", "E", "e", "I", "i", "O", "o", "U", "u"} #Заведем множество, содержащее все гласные буквы латинского алфавита
s = 0
for i in range (0, M**2, M):
    for j in range (M):
        print (a[i+j], end = " ") #Вывод заданной матрицы
    print ()

for i in range (M**2):
    slovo = a[i]
    for j in range (5):
        if slovo[j] in letters: #Проверка каждой буквы на присутсвие ее в словаре "letters"
            s = s + 1
    a[i] = s * 10 + (5 - s) #Заменяем элемент матрицы на сумму, он нам больше не нужен
    s = 0
k=[]
for i in range (0, M**2, M): #Вывод матрицы из сумм.
    for j in range (M):
        k.append (a[i+j])
    k = sorted(k, reverse=False) #Каждую строку матрицы сортируем по возрастанию с помощью встроенной фукнции "sorted"
    for l in range (M):
        print (k[l], end =" ")
    print()
    k =[]
