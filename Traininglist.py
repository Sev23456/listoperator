commands = '' # переменная для введения команд в цикле while
# предустановленный список
traning_list = [['Гарри Поттер и философский камень', 'Джоан Роулинг'], ['Убить пересмешника', 'Харпер Ли'], ['Война и мир', 'Лев Толстой'], ['Мцыри', 'Михаил Лермонтов']]
    
def view_list():
    print(traning_list)
    return

def add_element():
    user_input=input("Введите добавляемый элемент в формате: название, автор: ")
    index=user_input.find(',')
    #print(index)
    #print(user_input.count(','))
    if user_input.count(',') > 1 or user_input.count(',')==0:
        print("Неверный формат ввода")
        return 
    #if index == -1:
    #    print("Неверный формат ввода")
    #    return 
    name=user_input[:index]
    if name == '':
        print("Неверный формат ввода")
        return
    authors_name=user_input[(index+2):]
    if authors_name == '':
        print("Неверный формат ввода")
        return
    user_input_2=input("Введите команду: начало - для добавления в начало списка, конец - для добавления в конец списка или номер позиции (число) - для добавления в указанную позицию: ")
    try:
        user_input_2=int(user_input_2)
        idx=user_input_2
    except ValueError:
        if user_input_2 == 'начало':
            idx=0
        elif user_input_2 == 'конец':
            idx=-1
        else:
            print("Неверный формат ввода")
            return
    traning_list.insert(idx, [name, authors_name])
    print("Элемент ", user_input, 'добавлен. Список обновлен')
    return traning_list

def delete_element():
    user_input = int(input("Введите номер элемента: "))
    if user_input > len(traning_list):
        print('Элемента с номером ', user_input, ' нет в списке')
        return
    traning_list.pop(user_input-1)
    return traning_list

def change_element():
    view_list()
    user_input = int(input("Введите номер элемента: "))
    if user_input > len(traning_list):
        print('Элемента с номером ', user_input, ' нет в списке')
        return
    user_input_2=input("Введите добавляемый элемент в формате: название, автор: ")
    index=user_input_2.find(',')
    #print(index)
    #print(user_input.count(','))
    if user_input_2.count(',') > 1 or user_input_2.count(',')==0:
        print("Неверный формат ввода")
        return 
    #if index == -1:
    #    print("Неверный формат ввода")
    #    return 
    name=user_input_2[:index]
    if name == '':
        print("Неверный формат ввода")
        return
    authors_name=user_input_2[(index+2):]
    if authors_name == '':
        print("Неверный формат ввода")
        return
    traning_list[user_input-1] = [name, authors_name]
    return traning_list

def view_element():
    user_input = int(input("Введите номер элемента: "))
    if user_input-1 > len(traning_list):
        print('Элемента с номером ', user_input, ' нет в списке')
        return
    print(traning_list[user_input-1])

while commands != 'стоп':
    print('Список команд для работы с программой: Вывести - просмотреть весь список Значение - просмотреть значение элемента в списке Добавить - добавить элемент в список Удалить - удалить элемент из списка Изменить - изменить значение элемента в списке Стоп - завершить работу программы')
    commands = input('Введите команду: ')
    commands = commands.lower()
    commands = commands.strip(' ')
    if commands == 'вывести':
        view_list()
    elif commands == 'значение':
        view_element()
    elif commands == 'добавить':
        add_element()
    elif commands == 'удалить':
        delete_element()
    elif commands == 'изменить':
        change_element()
    elif commands == 'стоп':
        break