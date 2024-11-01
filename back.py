import os

from resources import Entry


class EntryManager:
    def __init__(self, data_path: str):
        self.entries = []
        self.data_path = data_path

    def save(self):
        for entry in self.entries:
            entry.save(self.data_path)
        return

    def load(self):
        if not os.path.isdir(self.data_path):
            os.makedirs(self.data_path)
        else:
            for filename in os.listdir(self.data_path):
                if filename.endswith('json'):
                    entry = Entry.load(os.path.join(self.data_path, filename))
                    self.entries.append(entry)
        return self


    def add_entry(self, title: str):
        self.entries.append(Entry(title))