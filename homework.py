#!/usr/bin/env python
# coding: utf-8

# In[313]:


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def lect_rate(self, lecturer, course, grade):
        if isinstance(lecturer,Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress  and grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def avg_grade(self):
        sum_1 = 0
        count_1 = 0
        for grades in self.grades.values():
            sum_1 +=  sum(grades)
            count_1 += len(grades)
            return round(sum_1/count_1)
        
    def __str__(self):
        result = f'Имя: {self.name}\n'             f'Фамилия: {self.surname}\n'             f'Средняя оценка за домашние задания: {self.avg_grade()}\n'             f'Курсы в процессе изучения: {self.courses_in_progress}\n'             f'Завершенные курсы: {self.finished_courses}'
        return print(result)
    
    def __lt__(self, stud_2):
        if not isinstance(stud_2,Student):
            print('Такого студентa нет!')
        else:
            compare = self.avg_grade() < stud_2.avg_grade()
            if compare:
                print(f'У студента {stud_2.name} {stud_2.surname} средняя оценка выше, чем у {self.name} {self.surname}.')
            else:
                print(f'У студента {self.name} {self.surname} средняя оценка выше, чем у {stud_2.name} {stud_2.surname}.')


# In[314]:


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


# In[315]:


class Lecturer(Mentor):
    def __init__(self ,name, surname):
        super().__init__(name, surname)
        self.grades = {}
        
    def avg_grade_l(self):
        sum_1 = 0
        count_1 = 0
        for grades in self.grades.values():
            sum_1 +=  sum(grades)
            count_1 += len(grades)
            return round(sum_1/count_1)
            
        
    def __str__(self):
        resul = f'Имя: {self.name}\n'                f'Фамилия: {self.surname}\n'                f'Средняя оценка за лекции: {self.avg_grade_l()}\n'
        return print(resul)
    def __lt__(self, lect_2):
        if not isinstance(lect_2, Lecturer):
            print('Такого лектора нет!')
            return
        else:
            comp = self.avg_grade_l() < lect_2.avg_grade_l()
            if comp:
                print(f'У лектора  {lect_2.name} {lect_2.surname} средняя оценка выше, чем у {self.name} {self.surname}.')
            else:
                print(f'У лектора  {self.name} {self.surname} средняя оценка выше, чем у {lect_2.name} {lect_2.surname}.')
            
        


# In[316]:


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        res = f'Имя: {self.name}\n'              f'Фамилия: {self.surname}'
        return print(res)
        


# In[317]:


best_student = Student('Thomas', 'Miller', 'm')
best_student.courses_in_progress += ['Java', 'Git']
best_student.finished_courses += ['Python']

good_student = Student('Anna','Frank', 'f')
good_student.courses_in_progress += ['Git', 'Java']
good_student.finished_courses += ['C++']


# In[318]:


lecturer_1 = Lecturer('Paul','Geiger')
lecturer_1.courses_attached += ['Java','Git']

lecturer_2 = Lecturer('Maja','Kunzt')
lecturer_2.courses_attached += ['Python','C++','Java', 'Git']


# In[319]:


reviewer_1 = Reviewer('Richard', 'Friedrich')
reviewer_1.courses_attached += ['Python', 'Git', 'Java','C++']

reviewer_2 = Reviewer ('Betta', 'Golz')
reviewer_2.courses_attached += ['Python', 'Git', 'Java','C++']


# In[320]:


reviewer_1.rate_hw(best_student, 'Java', 10)
reviewer_1.rate_hw(best_student, 'Git',8)
reviewer_2.rate_hw(good_student, 'Git', 8)
reviewer_2.rate_hw(good_student,'Java', 6)


# In[321]:


best_student.lect_rate(lecturer_1, 'Java', 10)
best_student.lect_rate(lecturer_1, 'Git', 8)
good_student.lect_rate(lecturer_2, 'Java', 9)
good_student.lect_rate(lecturer_2,'Git', 7)


# In[322]:


best_student.avg_grade()


# In[323]:


best_student.__str__()


# In[324]:


best_student.__lt__(good_student)


# In[325]:


lecturer_1.avg_grade_l()


# In[326]:


lecturer_1.__str__()


# In[327]:


lecturer_1.__lt__(lecturer_2)


# In[328]:


reviewer_1.__str__()


# In[333]:


def avg_all_stud(stud_list,course):
    total = 0
    for student in stud_list:
        for course_name,grade in student.grades.items():
            if course_name == course:
                total += sum(grade)/len(grade)
    return round(total/len(stud_list),2)


# In[334]:


def avg_all_lect(lect_list,course):
    total = 0
    for lect in lect_list:
        for course_name,grade in lect.grades.items():
            if course_name == course:
                total += sum(grade)/len(grade)
    return round(total/len(lect_list),2)


# In[335]:


print(avg_all_stud([best_student,good_student],'Java'))


# In[336]:


print(avg_all_lect([lecturer_1,lecturer_2],'Java'))


# In[ ]:




