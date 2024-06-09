grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list=list(students) #переводим неупорядоченное множество в упорядоченный список
students_list.sort() #сортируем список по алфавиту
stud_grades = {} #создаём пустой словарь, в который будут добавляться имена студентов из упорядоченного списка и средняя оценка учеников
for i in range(len(grades)): #этот цикл будет добавлять ключи и значения в словарь, количество циклов равно количеству объектов в списке, вычесленному с помощью len
    stud_grades.update({students_list[i]: sum(grades[i])/len(grades[i])})
print(stud_grades)