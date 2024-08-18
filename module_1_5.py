from idlelib.replace import replace
a = 'Ответы: '
def out_red(text):
    print("\033[36m{}".format(text))
out_red("Неизменяемые и изменяемые объекты. Кортежи и списки:")
immutable_var = 1, 2, 'table', 'icon', 3, 4, 5
print (immutable_var)
# immutable_var [0] = 33 // Не получится , ибо он не изменяет готовый не изменяемый текст
mutable_list = ([1, 2, 'table'], 'icon', 3, 4, 5)
temp_list = list(mutable_list) #Создали список и добавили туда уже строку
temp_list.append('Richard') # Да, я добавил возможно не так , как нужно , но этот способ тоже рабочий :), но это добавление, а просили изменить. ещё одна функция ниже
mutable_list = tuple(temp_list)
print (mutable_list)
mutable_list[0][0] = 'char' # Тут вот мы заменили уже , обратились к порядковому номеру списка и достали оттуда элемент с индексем 0 и поменяли на char
mutable_list[0][1] = 'school' # Укажи мы без '' , было бы ошибочно , ибо было int(число) , нам нужен str(строку)
print (mutable_list)
# Я всегда меняю цвет, ибо так глазам комфортнее , спасибо за уделённое время :)