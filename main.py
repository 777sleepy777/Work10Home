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
    
 
class Record():
    def __init__(self, name, phone=None):
        self.name = Name(value=name)
        self.phones = []
        if phone:
            self.add_phone_number(phone)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p for p in self.phones)}"
   
    def add_phone(self, phone):
        self.phones.append(phone)

    def edit_phone(self, phone_old, phone_new):
        phone_old_ind = self.phones.index(phone_old)
        self.phones[phone_old_ind] = phone_new

    def remove_phone(self, phone):
        self.phones.remove(phone)

    def find_phone(self, phone):
        #for i in self.phones:
        #    if i == phone:
        #        return i
        return self.phones[self.phones.index(phone)]

        
class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record
    
    def find(self, name: Name):
        return self.data[name]
    
    def delete(self, name: Name):
        self.data.pop(name)
        

def main():
  
    book = AddressBook()

    
if __name__ == '__main__':
    main()