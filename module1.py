import pandas as pd


class Book:
    def __init__(self):
        try:
            self.data = pd.read_csv('library.csv')  
        except FileNotFoundError:
            
            self.data = pd.DataFrame(columns=["name", "author", "year", "genre", "count"])
      
    def add_new_book(self, name, author, year, genre, count):
        new_book = pd.DataFrame({
            "name": [name],
            "author": [author],
            "year": [year],
            "genre": [genre],
            "count": [count]
        })
        self.data = pd.concat([self.data, new_book], ignore_index=True)  
        self.data.to_csv('library.csv', index=False)  
        print("Книга успішно додана.")

    def delete_by_name(self, name):
        
        self.data = self.data[self.data["name"] != name] 
        self.data.to_csv('library.csv', index=False)  
        print(f"Книга з назвою '{name}' успішно видалена.")

    def get_data(self):
        
        return self.data  

    def get_total_count(self):
        
        return self.data['count'].sum()  
    
    def find_most_popular(self):
        
        if not self.data.empty:
            most_popular = self.data.loc[self.data['count'].idxmax()]
            return most_popular
        return "Бібліотека порожня."

    def find_by_year(self, year):
        
        books = self.data[self.data['year'] == year]
        if not books.empty:
            return books
        return f"Немає книг, написаних у {year} році."

    def change_book_atrib(self, name, column, new_value):
        if name in self.data['name'].values:
            self.data.loc[self.data['name'] == name, column] = new_value
            self.data.to_csv('library.csv', index=False)
            print(f"Атрибут '{column}' книги '{name}' успішно змінено.")
        else:
            print("Книга з такою назвою не знайдена.")


def main():
    lib = Book()
    while True:
        print("\nМеню:")
        print("1. Показати всі книги")
        print("2. Додати нову книгу")
        print("3. Видалити книгу за назвою")
        print("4. Отримати загальну кількість книг")
        print("5. Знайти найпопулярнішу книгу")
        print("6. Знайти книги за роком")
        print("7. Змінити атрибут книги")
        print("8. Вийти")

        choice = input("Оберіть опцію: ")

        if choice == '1':
            print("\nБібліотека:")
            print(lib.get_data())

        elif choice == '2':
            
            name = input("Введіть назву книги: ")
            author = input("Введіть автора: ")
            year = int(input("Введіть рік: "))
            genre = input("Введіть жанр: ")
            count = int(input("Введіть кількість: "))
            lib.add_new_book(name, author, year, genre, count)

        elif choice == '3':
            
            name = input("Введіть назву книги для видалення: ")
            lib.delete_by_name(name)

        elif choice == '4':
            
            print(f"\nЗагальна кількість книг: {lib.get_total_count()}")

        elif choice == '5':
            
            print("\nНайпопулярніша книга:")
            print(lib.find_most_popular())

        elif choice == '6':
            
            year = int(input("Введіть рік: "))
            print("\nКниги, написані в цьому році:")
            print(lib.find_by_year(year))

        elif choice == '7':
            
            name = input("Введіть назву книги для зміни: ")
            column = input("Введіть атрибут (name, author, year, genre, count): ")
            new_value = input("Введіть нове значення: ")
            if column in ["year", "count"]:
                new_value = int(new_value)  
            lib.change_book_atrib(name, column, new_value)

        elif choice == '8':
            print("Програма завершена.")
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
