students = set()
doubles = set()

n_eng = int(input())
m_deu = int(input())
k_fra = int(input())

counter = 0

for _ in range(n_eng + m_deu +k_fra):
    student_name = input()
    if student_name in students:
        counter += 1
        doubles.add(student_name)
    students.add(student_name)