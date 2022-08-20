class FlatIterator:
    def __init__(self, input_list):
        self.counter = 0
        self.input_list = input_list
        self.unpacked_list = list()
        self.unpack()

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        if self.counter - 1 >= len(self.unpacked_list):
            raise StopIteration
        return self.unpacked_list[self.counter - 1]

    def unpack(self):
        def merge(current_list):
            for element in current_list:
                if isinstance(element, list):
                    merge(element)

                else:
                    self.unpacked_list.append(element)

        merge(self.input_list)




