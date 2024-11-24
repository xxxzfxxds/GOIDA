import random

def wicz():
    q = int(input('колько раз ты хочешь сыграть '))
    Famous_people = {"Саня":"01.01.1999",
                     "Борис":"09.11.2012",
                     "Кто то 3":"02.12.2077",
                     "Хазбик":"20.11.1234",
                     "Виталик":"01.06.1939",
                     "Ахмед":"11.09.2001"}
    for i in range(q):
        name,date = random.choice(list(Famous_people.items()))
        answer = input(f"Когда родился {name} ")
        if answer == date:
            print("Ура")
        else:
            print("Неправильно")
    print('Пока')

