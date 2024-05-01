# домашние животные и вьючные животные, в составы которых в случае домашних
# животных войдут классы: собаки, кошки, хомяки, а в класс вьючные животные
# войдут: Лошади, верблюды и ослы
# . Написать программу, имитирующую работу реестра домашних животных.
# В программе должен быть реализован следующий функционал:
# 14.1 Завести новое животное
# 14.2 определять животное в правильный класс
# 14.3 увидеть список команд, которое выполняет животное
# 14.4 обучить животное новым командам
# 14.5 Реализовать навигацию по меню
# 15.Создайте класс Счетчик, у которого есть метод add(), увеличивающий̆
# значение внутренней̆int переменной̆на 1 при нажатие “Завести новое
# животное” Сделайте так, чтобы с объектом такого типа можно было работать в
# блоке try-with-resources. Нужно бросить исключение, если работа с объектом
# типа счетчик была не в ресурсном try и/или ресурс остался открыт. Значение
# считать в ресурсе try, если при заведения животного заполнены все поля
pets = []  # Список для хранения животных

# Класс родительский класс животных
class Animal:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date

# Классы домашних животных
class PetAnimal(Animal):
    def __init__(self, name, birth_date, animal_type):
        super().__init__(name, birth_date)
        self.animal_type = animal_type
        self.commands = []

    def get_commands(self):
        return self.commands

    def learn_command(self, new_command):
        self.commands.append(new_command)

# Классы вьючных животных
class WorkingAnimal(Animal):
    def __init__(self, name, birth_date, animal_type):
        super().__init__(name, birth_date)
        self.animal_type = animal_type

    def get_commands(self):
        if self.animal_type == 'Лошадь':
            return ["Тянуть плуг", "Переносить грузы", "Прыжки"]
        elif self.animal_type == 'Осел':
            return ["Переносить грузы", "Пасти стадо", "Чесать копыта"]

# Класс Счетчик
class Counter:
    def __enter__(self):
        self.count = 0
        return self

    def add(self):
        self.count += 1

    def __exit__(self, exc_type, exc_value, traceback):
        if self.count == 0 or exc_type is not None:
            raise Exception("Ошибка: работа с объектом счетчика не была в блоке try-with-resources или ресурс остался открыт.")
        
class ManageAnimals:
    @staticmethod
    def add_animal(name, birth_date, animal_type):
        if animal_type in ['Собака', 'Кошка', 'Хомяк', 'Лошадь', 'Осел']:
            if animal_type in ['Собака', 'Кошка', 'Хомяк']:
                pets.append(PetAnimal(name, birth_date, animal_type))
            else:
                pets.append(WorkingAnimal(name, birth_date, animal_type))
            print(f"Новое животное {name} ({animal_type}) успешно добавлено!")
        else:
            print("Ошибка: Некорректный тип животного.")
        
def main():
    with Counter() as counter:
        print("Добро пожаловать в реестр домашних животных!")
        while True:
            print("\nМеню:")
            print("1. Завести новое животное")
            print("2. Просмотреть список команд животного")
            print("3. Обучить животное новым командам")
            print("4. Выход")

            choice = input("Выберите действие: ")

            if choice == '1':
                new_pet_name = input("Введите имя нового животного: ")
                new_pet_type = input("Укажите тип нового животного (Собака, Кошка, Хомяк): ")
                new_birth_date = input("Введите дату рождения животного (гггг-мм-дд): ")

                if all([new_pet_name, new_pet_type, new_birth_date]):
                    ManageAnimals.add_animal(new_pet_name, new_birth_date, new_pet_type)
                    counter.add()  
                    print("Новое животное успешно добавлено!")
                else:
                    print("Ошибка: Заполните все поля.")

            elif choice == '2':
                print("Просмотреть список команд животного:")
                animal_name = input("Введите имя животного: ")
                found = False

                for pet in pets:
                    if pet.name == animal_name:
                        print(f"Команды для животного {animal_name}:")
                        print(pet.get_commands())
                        found = True
                        break

                if not found:
                    print(f"Животное с именем {animal_name} не найдено.")

            elif choice == '3':
                print("Обучить животное новым командам:")
                animal_name = input("Введите имя животного: ")
                found = False

                for pet in pets:
                    if pet.name == animal_name:
                        new_command = input("Введите новую команду для обучения животного: ")
                        pet.learn_command(new_command)
                        print(f"Животное {animal_name} успешно обучено новой команде: {new_command}")
                        found = True
                        break

                if not found:
                    print(f"Животное с именем {animal_name} не найдено.")

            elif choice == '4':
                print("Выход из программы.")
                break

if __name__ == "__main__":
    main()