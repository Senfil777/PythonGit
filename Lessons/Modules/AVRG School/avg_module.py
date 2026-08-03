school = {}
menu = """________________________________________________
                School v0.20
            Меню:
        1 - добавить оценку студенту
        2 - считаем средний балл
        3 - вывести все оценки и всех студентов
        0 - выйти из программы
________________________________________________
"""

def add_grade_by_name():
    """
    
    
    """
    
    name = input("Введи имя студента:")
    grade = int(input("Введи оценку студента"))

    if name in school:
        school.get(name).append(grade)
    else:
        school.update({name:[grade,]})


def show_school():
    """
    
    
    """
    for k, v in school.items():
        print(k, v)


def calc_avg_by_name():
    """

    """
    
    if len(school) == 0:
        print("Нету студентов!")
        return None
    
    name = input("Введи имя студента:")
    
    if name in school and len(school.get(name)) > 0:
        avg = sum(school.get(name))/len(school.get(name))
        
        print("Средний балл студента - ", name)
        print(avg)
    else:
        print("студента нет в школе или у него нет оценок!")

    
def runApp():
    """
    
    
    """
    
    print(menu)
    operation_number = input("--->")
    
    while operation_number != "0":
        if operation_number == "1":
            add_grade_by_name()
        elif operation_number == "2":
            calc_avg_by_name()
        elif operation_number == "3":
            show_school()
        else:
            print("Не понял операцию. введи новер в соотвесвии с меню.")
        
        print()
        print(menu)
        operation_number = input("--->")
        
    print("Программа завершила работу! Пока.")


runApp()