# КОСТЯНТИН ЛЕМЕШОК, ДЗ № 7 З КУРСУ PYTHON CORE

# Завдання 1

# По перше додамо додатковий функціонал до класів:

#     Додайте поле birthday для дня народження в клас Record . Це поле має бути класу Birthday. Це поле не обов'язкове, але може бути тільки одне.

# class Birthday(Field):
#     def __init__(self, value):
#         try:
#             # Додайте перевірку коректності даних
#             # та перетворіть рядок на об'єкт datetime
#         except ValueError:
#             raise ValueError("Invalid date format. Use DD.MM.YYYY")

# class Record:
#     def __init__(self, name):
#         self.name = Name(name)
#         self.phones = []
#         self.birthday = None

#     Додайте функціонал роботи з Birthday у клас Record, а саме функцію add_birthday, яка додає день народження до контакту.
#     Додайте функціонал перевірки на правильність наведених значень для полів Phone, Birthday.
#     Додайте та адаптуйте до класу AddressBook нашу функцію з четвертого домашнього завдання, тиждень 3, get_upcoming_birthdays, яка для контактів адресної книги повертає список користувачів, яких потрібно привітати по днях на наступному тижні.


# Тепер ваш бот повинен працювати саме з функціоналом класу AddressBook. Це значить, що замість словника contacts ми використовуємо book = AddressBook()

# Завдання 2

# Для реалізації нового функціоналу також додайте функції обробники з наступними командами:

#     add-birthday - додаємо до контакту день народження в форматі DD.MM.YYYY
#     show-birthday - показуємо день народження контакту
#     birthdays - повертає список користувачів, яких потрібно привітати по днях на наступному тижні

# @input_error
# def add_birthday(args, book):
#     # реалізація

# @input_error
# def show_birthday(args, book):
#     # реалізація

# @input_error
# def birthdays(args, book):
#     # реалізація


# Тож в фіналі наш бот повинен підтримувати наступний список команд:
#     add [ім'я] [телефон]: Додати або новий контакт з іменем та телефонним номером, або телефонний номер к контакту який вже існує.
#     change [ім'я] [старий телефон] [новий телефон]: Змінити телефонний номер для вказаного контакту.
#     phone [ім'я]: Показати телефонні номери для вказаного контакту.
#     all: Показати всі контакти в адресній книзі.
#     add-birthday [ім'я] [дата народження]: Додати дату народження для вказаного контакту.
#     show-birthday [ім'я]: Показати дату народження для вказаного контакту.
#     birthdays: Показати дні народження, які відбудуться протягом наступного тижня.
#     hello: Отримати вітання від бота.
#     close або exit: Закрити програму.

# def main():
#     book = AddressBook()
#     print("Welcome to the assistant bot!")
#     while True:
#         user_input = input("Enter a command: ")
#         command, *args = parse_input(user_input)

#         if command in ["close", "exit"]:
#             print("Good bye!")
#             break

#         elif command == "hello":
#             print("How can I help you?")

#         elif command == "add":
#             # реалізація

#         elif command == "change":
#             # реалізація

#         elif command == "phone":
#             # реалізація

#         elif command == "all":
#             # реалізація

#         elif command == "add-birthday":
#             # реалізація

#         elif command == "show-birthday":
#             # реалізація

#         elif command == "birthdays":
#             # реалізація

#         else:
#             print("Invalid command.")


# Для прикладу розглянемо реалізацію команди add [ім'я] [телефон]. В функції main ми повинні додати обробку цієї команди, в відповідне місце:

#          elif command == "add":
#             print(add_contact(args, book))

# Сама реалізація функції add_contact може виглядати наступним чином:

# @input_error
# def add_contact(args, book: AddressBook):
#     name, phone, *_ = args
#     record = book.find(name)
#     message = "Contact updated."
#     if record is None:
#         record = Record(name)
#         book.add_record(record)
#         message = "Contact added."
#     if phone:
#         record.add_phone(phone)
#     return message


# Наша функція add_contact має два призначення - додавання нового контакту або оновлення телефону для контакту, що вже існує в адресній книзі.

# Параметри функції це список аргументів args та сама адресна книга book.

#     Спочатку функція розпаковує список args, отримуючи ім'я name і телефон phone з перших двох елементів списку. Решта аргументів ігнорується завдяки використанню *_. Далі метод find об'єкта book виконує пошук запису з іменем name. Якщо запис з таким іменем існує, метод повертає цей запис, інакше повертається None.
#     Якщо запис не знайдено, то це новий контакт і функція створює новий об'єкт Record з іменем name і додає його до book викликом методу add_record. Після додавання нового запису змінній message присвоюється повідомлення "Contact added." успішності операції.
#     Далі незалежно від того, чи був запис знайдений або створений новий, до цього запису додається телефонний номер за допомогою методу add_phone, якщо він був наданий. На завершення функція повертає повідомлення про результат своєї роботи: "Contact updated.", якщо контакт був оновлений, або "Contact added.", якщо контакт був доданий. Для перехоплення помилок вводу та виведення відповідного повідомлення про помилку використовуємо декоратор @input_error.


# Критерії оцінювання:
# 1. Реалізувати всі вказані команди до бота
# 2. Всі дані повинні виводитися у зрозумілому та зручному для користувача форматі
# 3. Всі помилки, такі як неправильний ввід чи відсутність контакту, повинні оброблятися інформативно з відповідним повідомленням для користувача
# 4. Валідація даних:
#     Дата народження має бути у форматі DD.MM.YYYY.
#     Телефонний номер має складатися з 10 цифр.
# 5. Програма повинна закриватися коректно після виконання команд close або exit


from collections import UserDict
import logging
from datetime import datetime, timedelta
from functools import wraps


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Field:
    """
    Base class for all record fields.
    """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """
    Class for storing a contact's name. It is a mandatory field.
    """
    pass


class Phone(Field):
    """
    Class for storing a phone number.
    Includes validation to ensure the number consists of exactly 10 digits.
    """
    def __init__(self, value):
        if not (isinstance(value, str) and value.isdigit() and len(value) == 10):
            raise ValueError("Phone number must be a string of 10 digits.")
        super().__init__(value)


class Birthday(Field):
    """
    Class for storing a birthday.
    Includes validation to ensure the date is in DD.MM.YYYY format and not in the future.
    """
    def __init__(self, value):
        try:
            parsed_date = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use valid date in format DD.MM.YYYY")
        
        if parsed_date > datetime.today().date():
            raise ValueError("Birthday cannot be in the future.")

        self.value = parsed_date


class Record:
    """
    Class for storing contact information, including name, phones, and birthday.
    """
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None


    def add_phone(self, phone_number):
        """Adds a phone number to the contact's record."""
        phone = Phone(phone_number)
        self.phones.append(phone)


    def find_phone(self, phone_number):
        """Finds a phone number in the contact's record."""
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None


    def edit_phone(self, old_phone_number, new_phone_number):
        """Edits an existing phone number in the contact's record."""
        phone_to_edit = self.find_phone(old_phone_number)

        if phone_to_edit:
            new_phone = Phone(new_phone_number)
            index = self.phones.index(phone_to_edit)
            self.phones[index] = new_phone
        else:
            raise ValueError(f"Old phone number '{old_phone_number}' not found.")


    def remove_phone(self, phone_number):
        """Removes a phone number from the contact's record."""
        phone_to_remove = self.find_phone(phone_number)
        if phone_to_remove:
            self.phones.remove(phone_to_remove)
        else:
            raise ValueError(f"Phone number '{phone_number}' not found.")

    def add_birthday(self, birthday_str):
        """Adds a birthday to the contact's record."""
        self.birthday = Birthday(birthday_str)
        logging.info(f"Birthday added for {self.name.value}")

    def __str__(self):
        phones = '; '.join(p.value for p in self.phones)
        birthday_str = self.birthday.value.strftime("%d.%m.%Y") if self.birthday else "Not set"
        return f"Contact name: {self.name.value}, phones: {phones}, birthday: {birthday_str}"


class AddressBook(UserDict):
    """
    Class for storing and managing records in an address book.
    """
    def add_record(self, record: Record):
        """Adds a new record to the address book."""
        self.data[record.name.value] = record
        logging.info(f"Record added for {record.name.value}")


    def find(self, name):
        """Finds a record by name."""
        return self.data.get(name)


    def delete(self, name):
        """Deletes a record by name."""
        if name in self.data:
            del self.data[name]
            logging.info(f"Record deleted for {name}")
        else:
            raise KeyError(f"Contact '{name}' not found.")


    def get_upcoming_birthdays(self) -> list:
        """
        Returns a list of contacts to be congratulated on their upcoming birthdays.
        Checks for birthdays in the next 7 days, including today. Adjusts for weekends (moves to next Monday).
        """
        today = datetime.today().date()
        upcoming_birthdays = []
        
        for record in self.data.values():
            if record.birthday:
                birthday_date = record.birthday.value
                
                # Check if birthday has already passed this year
                try:
                    birthday_this_year = birthday_date.replace(year=today.year)
                except ValueError: 
                    # Handle leap year birthdays (Feb 29) on non-leap years
                    birthday_this_year = birthday_date.replace(year=today.year, day=28)

                if birthday_this_year < today:
                    # If it passed, check for next year's birthday
                    try:
                        birthday_this_year = birthday_this_year.replace(year=today.year + 1)
                    except ValueError:
                         # Handle leap year birthdays (Feb 29) on non-leap years
                        birthday_this_year = birthday_this_year.replace(year=today.year + 1, day=28)
                
                # Calculate difference in days
                days_until_birthday = (birthday_this_year - today).days
                
                # Check if birthday is within the next 7 days (0 to 6)
                if 0 <= days_until_birthday < 7:
                    congr_date = birthday_this_year
                    
                    # Adjust for weekends
                    weekday = congr_date.weekday()
                    if weekday == 5:  # Saturday
                        congr_date += timedelta(days=2)
                    elif weekday == 6:  # Sunday
                        congr_date += timedelta(days=1)
                        
                    upcoming_birthdays.append({
                        "name": record.name.value,
                        "congratulation_date": congr_date.strftime("%d.%m.%Y")
                    })
                    
        return upcoming_birthdays


# --- Bot Logic ---

def input_error(func):
    """
    Decorator to handle common input errors for handler functions.
    Catches ValueError, KeyError, AttributeError and IndexError, returning a specific error message.
    """
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return f"Error: Not enough or wrong arguments for this command."
        except KeyError:
            return "Error: Contact not found."
        except IndexError:
            return f"Error: Contact not found."
        except AttributeError:
            return "Error: Contact not found."
    return inner


def parse_input(user_input):
    """
    Parses user input into a command and arguments.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


@input_error
def add_contact(args, book: AddressBook):
    """
    Adds a new contact or a new phone to an existing contact.
    """
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."

    record.add_phone(phone)
        
    return message

@input_error
def change_contact(args, book: AddressBook):
    """
    Changes an existing phone number for a contact.
    """
    name, old_phone, new_phone = args
    record = book.find(name)
    record.edit_phone(old_phone, new_phone)

    return f"Phone number updated for {name}."

@input_error
def show_phone(args, book: AddressBook):
    """
    Shows all phone numbers for a specific contact.
    """ 
    name = args[0]
    record = book.find(name)
    return f"{name}'s phones: {'; '.join(p.value for p in record.phones)}"

@input_error
def delete_contact(args, book: AddressBook):
    """
    Deletes a contact from the address book.
    """        
    name = args[0]
    book.delete(name)
    return f"Contact {name} deleted."

@input_error
def show_all(args, book: AddressBook):
    """
    Displays all contacts in the address book.
    """
    if not book.data:
        return "Address book is empty."
    return "\n".join(str(record) for record in book.data.values())

@input_error
def add_birthday(args, book: AddressBook):
    """
    Adds a birthday to a specific contact.
    """        
    name, birthday_str = args
    record = book.find(name)
    record.add_birthday(birthday_str)
    return f"Birthday added for {name}."

@input_error
def show_birthday(args, book: AddressBook):
    """
    Shows the birthday of a specific contact.
    """ 
    name = args[0]
    record = book.find(name)
        
    if record.birthday:
        return f"{name}'s birthday: {record.birthday.value.strftime('%d.%m.%Y')}"
    else:
        return f"{name}'s birthday is not set."

@input_error
def birthdays(args, book: AddressBook):
    """
    Shows upcoming birthdays for the next week.
    """
    upcoming = book.get_upcoming_birthdays()
    
    if not upcoming:
        return "No upcoming birthdays in the next week."
        
    lines = ["Upcoming birthdays:"]
    for entry in upcoming:
        lines.append(f"Congratulate {entry['name']} on {entry['congratulation_date']}")
        
    return "\n".join(lines)

def show_help():
    """
    Displays the help message with all available commands and their usage.
    """
    print("\nAvailable commands:")
    print("  hello                                 - Get a greeting from the bot.")
    print("  add [name] [phone]                    - Add a new contact or a new phone to an existing contact. A phone number must be 10 digits long and contain digits only.")
    print("  change [name] [old phone] [new phone] - Change a phone number for a contact. A phone number must be 10 digits long and contain digits only.")
    print("  phone [name]                          - Show all phone numbers for a contact.")
    print("  delete [name]                         - Delete a contact from the address book.")
    print("  all                                   - Show all contacts in the address book.")
    print("  add-birthday [name] [DD.MM.YYYY]      - Add a birthday for a contact.")
    print("  show-birthday [name]                  - Show the birthday for a contact.")
    print("  birthdays                             - Show upcoming birthdays for the next week.")
    print("  help                                  - Show this help message.")
    print("  close, exit                           - Close the program.\n")


def main():
    """
    Main function for the assistant bot.
    """
    book = AddressBook()
    print("Welcome to the assistant bot!")
    show_help()
    
    while True:
        try:
            user_input = input("Enter a command: ")
            if not user_input:
                continue
                
            command, args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break

            elif command == "hello":
                print("How can I help you?")

            elif command == "help":
                show_help()

            elif command == "add":
                print(add_contact(args, book))

            elif command == "change":
                print(change_contact(args, book))

            elif command == "phone":
                print(show_phone(args, book))

            elif command == "delete":
                print(delete_contact(args, book))

            elif command == "all":
                print(show_all(args, book))

            elif command == "add-birthday":
                print(add_birthday(args, book))

            elif command == "show-birthday":
                print(show_birthday(args, book))

            elif command == "birthdays":
                print(birthdays(args, book))

            else:
                print("Invalid command. Type 'help' to see available commands.")
        
        except EOFError:
            # Handle Ctrl+D (End of File)
            print("\nGood bye!")
            break
        except KeyboardInterrupt:
            # Handle Ctrl+C
            print("\nGood bye!")
            break
        except Exception as e:
            # Catch any other unexpected errors
            logging.error(f"An unexpected error occurred: {e}")
            print("An unexpected error occurred. Please try again.")


if __name__ == '__main__':
    main()