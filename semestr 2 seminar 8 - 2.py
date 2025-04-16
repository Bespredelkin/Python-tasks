class HashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def hash_function(self, key):
        """Хеш-функция для преобразования ключа в индекс таблицы"""
        return hash(key) % self.size

    def put(self, key, value):
        """Добавление записи в таблицу"""
        current = self.hash_function(key)
        if self.keys[current] is None:
            self.keys[current] = key
            self.values[current] = value
            return
        else:
            for i in range(1, self.size):
                next = (current + i) % self.size
                if self.keys[next] is None:
                    self.keys[next] = key
                    self.values[next] = value
                    return
        raise Exception("Хеш-таблица заполнена")

    def get(self, key):
        """Поиск записи в таблице"""
        current = self.hash_function(key)
        if self.keys[current] == key:
            return self.values[current]
        else:
            for i in range(1, self.size):
                next = (current + i) % self.size
                if self.keys[next] == key:
                    return self.values[next]
                elif self.keys[next] is None:
                    return None
        return None

    def delete(self, key):
        """Удаление записи из таблицы"""
        current = self.hash_function(key)
        if self.keys[current] == key:
            self.keys[current] = None
            self.values[current] = None
            return
        else:
            for i in range(1, self.size):
                next = (current + i) % self.size
                if self.keys[next] == key:
                    self.keys[next] = None
                    self.values[next] = None
                    for j in range(1, self.size):
                        vremen_current = (next + j) % self.size
                        if self.keys[vremen_current] is None:
                            return
                        else:
                            hash_value = self.hash_function(self.keys[vremen_current])
                            if hash_value <= current:
                                self.keys[current] = self.keys[vremen_current]
                                self.values[current] = self.values[vremen_current]
                                self.keys[vremen_current] = None
                                self.values[vremen_current] = None
                                current = vremen_current
                    return
                elif self.keys[next] is None:
                    return

    def update(self, key, value):
        """Замена значения по ключу"""
        next = self.hash_function(key)
        if self.keys[next] == key:
            self.values[next] = value
            return
        else:
            for i in range(1, self.size):
                next = (next + i) % self.size
                if self.keys[next] == key:
                    self.values[next] = value
                    return
                elif self.keys[next] is None:
                    self.put(key, value)
                    return

    def print_table(self):
        """Печать всей таблицы"""
        print("Hash table:")
        for i in range(self.size):
            if self.keys[i] is not None:
                print(f"Key: {self.keys[i]}, Value: {self.values[i]}")

Size = int(input("Введите размер таблицы: "))
table = HashTable(Size)

while 0 == 0:
    print()
    print(f"Для выхода введите: {0}")
    print(f"Для добавления записи в таблицу введите: {1}")
    print(f"Для замены значения по ключу введите: {2}")
    print(f"Для удаления записи из таблицы введите: {3}")
    print(f"Для поиска записи в таблице введите: {4}")
    print(f"Для печати таблицы введите: {5}")
    c = int(input("Введите номер от 0 до 5 для выполнения одной из команд: "))
    if c == 0:
        '''Выход'''
        quit()
    if c == 1:
        """Добавление записи в таблицу"""
        Familia = input("Введите фамилию")
        Telephon = input("Введите телефон")
        table.put(Familia, Telephon)
        table.print_table()
    elif c == 2:
        """Замена значения по ключу"""
        kluch = input("Введите ключ, значение которого вы хотите изменить")
        izmenenievalue = input("Введите значение для замены")
        table.update(kluch, izmenenievalue)
        table.print_table()
    elif c == 3:
        """Удаление записи из таблицы"""
        teludol = input("Введите ключ для удаления")
        table.delete(teludol)

    elif c == 4:
        """Поиск записи в таблице"""
        Famkluch = input("Введите ключ для получения значения")
        tel = table.get(Famkluch)
        print(tel)
    elif c == 5:
        """Печать таблицы"""
        table.print_table()
    else:
        a = input("Вы не ввели номер от 0 до 5, нажмите на любую клавишу и попробуйте еще раз: ")
