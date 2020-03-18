n_deu = int(input())
m_eng = int(input())

set_deu = set()
set_eng = set() 

for _ in range(n_deu):
    set_deu.add(input())

for _ in range(m_eng):
    set_eng.add(input())

total = set_eng ^ set_deu 
pritn(len(total))