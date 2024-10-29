import json
import os



def print_with_indent(value, indent=0):
    indentation = "\t" * indent
    print(indentation + str(value))


class Entry:
    def __init__(self, title, entries=None, parent=None):
        if entries is None:
            self.entries = []
        self.title = title
        self.parent = parent

    def __str__(self):
        return self.title

    def add_entry(self, entry):
        self.entries.append(entry)
        entry.parent = self

    @classmethod
    def from_json(cls, value: dict):
        new_value = cls(value['title'])
        for sub_entry in value.get('entries', []):
            new_value.add_entry(cls.from_json(sub_entry))
        return new_value

    def check_directory(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Директория {path} была создана.")
        else:
            print(f"Директория {path} уже существует.")

    def save(self, path):
        self.check_directory(path)
        file_path = os.path.join(path, f'{self.title}.json')
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(self.json(), file, ensure_ascii=False, indent=4)
        return

    @classmethod
    def load(cls, filename):
        with open(filename, 'r') as file:
            res = file.read()
            data = json.loads(res)
            dub = cls.from_json(data)
        return dub

    def json(self):
        res = {
            'title': self.title,
            'entries': [entry.json() for entry in self.entries]
        }
        return res

    def print_entries(self, indent=0):
        print_with_indent(self.title, indent)
        for entry in self.entries:
            entry.print_entries(indent + 1)


# def entry_from_json(value: dict) -> Entry:
#     new_entry = Entry(value['title'])
#     for value in value.get('entries', []):
#         new_entry.add_entry(entry_from_json(value))
#     return new_entry

if __name__ == '__main__':

    new_entry = Entry.from_json(grocery_list)
    new_entry.print_entries()
    print(new_entry.json())

    new_entry.save('E:')
    # groceries = Entry('Продукты')
    # category = Entry('Мясное')
    # category_1 = Entry('Молочное')
    #
    # category.add_entry(Entry('Курица'))
    # category.add_entry(Entry('Говядина'))
    # category.add_entry(Entry('Колбаса'))
    # category_1.add_entry(Entry('Творог'))
    # category_1.add_entry(Entry('Мороженное'))
    #
    # groceries.add_entry(category)
    # groceries.add_entry(category_1)
    #
    # # groceries.print_entries()
    #
    # res = category.json()
    # print(json.dumps(res, ensure_ascii=False, indent=4))

    # print_with_indent('test')
    # print_with_indent('test', indent=1)
    # print_with_indent('test', indent=2)
    # print_with_indent('test', indent=3)


