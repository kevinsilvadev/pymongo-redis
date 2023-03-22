from model.Person import Person
from faker import Faker
import random
from BD.Connection import Connection

def main():
    def generatorPerson():
            fake = Faker("pt_BR")
            courses = ['Engenharia de Software', 'Engenharia da Computação', 'Arquitetura', 'Física', 'Educação Física', 'Ciencia da Computação']
            years = [2023, 2024]
            approved_list = []
            for i in range(5000):
                name = fake.name()
                cpf = fake.cpf()
                years = random.choice(years)
                aproved_course = random.choice(courses)
                Person(name, cpf, years, aproved_course)
                candidate = {
                     'name': name,
                     'cpf': cpf,
                     'years': years,
                     'cursos_aprovados': aproved_course
                }
                approved_list.append(candidate)
            Connection.connection().insert_many(approved_list)
    generatorPerson()
main()
                