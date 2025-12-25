class SmartList(list):
    def __getitem__(self, index):
        if isinstance(index, int) and index < 0:
            index = abs(index) - 1
        return super().__getitem__(index)
sl = SmartList([10, 20, 30])
print(sl[1])
print(sl[-1])
print(sl[-2])
print(sl[-3])
print(sl[2])