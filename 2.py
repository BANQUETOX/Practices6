# Haga un programa que lea una lista de números reales que guarda las notas definitivas de un grupo de
# estudiantes, e imprima: las notas de todos los estudiantes, la nota mayor y la nota menor del grupo. El programa
# debe pedirle al usuario el número de estudiantes del grupo y reservar memoria suficiente para que la lista pueda
# guardar todas las notas.
total_students = int(input("Cuantos estudiantes hay? "))
students_gardes = []
best_grade = 0
worst_grade = 0
for student in range(0,total_students):
    student_grade = int(input(f"Cual es la nota del estudiante {student + 1} "))
    students_gardes.append(student_grade) 
worst_grade = students_gardes[0]
for student_grade in students_gardes:
    print(f"La nota del estudiante {students_gardes.index(student_grade) + 1} es {student_grade}")
    if student_grade > best_grade:
        best_grade = student_grade
    if student_grade < worst_grade:
        worst_grade = student_grade
print(f"La mejor nota fue un {best_grade}")
print(f"La peor nota fue un {worst_grade}")
    
