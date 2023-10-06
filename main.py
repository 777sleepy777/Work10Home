from collections import UserDict
def input_error(func):
    def inner(*args):
        try:
            result = func(*args)
            return result
        except KeyError:
            return "KeyError. This name is not in phone-book"
        except ValueError:
            return "ValueError. Phone number must be from 10 digit"
        except TypeError:
            return "TypeError. Unknown command"
        except IndexError:
            return "IndexError. Give me name and phone please"
    return inner
#Базовий клас для полів запису. 
#Буде батьківським для всіх полів, у ньому реалізується логіка загальна для всіх полів
class Field: 
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    
#Клас для зберігання імені контакту. Обов'язкове поле.
class Name(Field):
    pass
    # реалізація класу

class Phone(Field):
    def __init__(self, value):
        self.value = value
        if len(self.value) != 10 or not self.value.isdigit():
            raise ValueError("Number is not valid")
    
    def __str__(self):
        return f"{self.value}"
   
 
class Record():
    def __init__(self, name, phone=None):
        self.name = Name(value=name)
        self.phones = []
        if phone:
            self.add_phone_number(value = phone)


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p for p in self.phones)}"
   
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def edit_phone(self, phone_old, phone_new):
        num = None
        for i in self.phones:
            if i.value == phone_old:
                num = phone_old
                i.value = phone_new

        if num is None:
        #    raise ValueError
        #if phone_old in self.phones:
        #   phone_old.value = phone_new 
        #else:
            raise ValueError



    def remove_phone(self, phone):
         for i in self.phones:
            if i.value == phone:
                self.phones.remove(i)

    def find_phone(self, phone):
        for i in self.phones:
            if i.value == phone:
                return i
   
        
class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record
    
    def find(self, name: Name):
         for i in self.data:
            if i == name:
                return self.data[i]

    
    def delete(self, name: Name):
        try:
            self.data.pop(name)
        except:
            KeyError

        

def main():
  
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")

    
if __name__ == '__main__':
    main()