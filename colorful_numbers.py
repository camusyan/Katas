from itertools import combinations

class ColorfulNumber:
    def __init__(self, number):
        self.number = number
        self.number_list = [int(x) for x in str(number)]

    @staticmethod
    def all_combinations_generator(iterable):
        for length in range(1, len(iterable) + 1):
            for comb in combinations(iterable, length):
                yield comb

    @staticmethod
    def all_consecutive_combinations_generator(iterable):
        for length in range(1, len(iterable) + 1):
            for start in range(len(iterable) + 1 - length):
                yield iterable[start:start+length]

    @staticmethod
    def combinations_product(iterable):
        total = 1
        for i in iterable:
            total *= i
        return total

    def is_colorful(self):
        # all_products = [self.combinations_product(x) for x in self.all_combinations_generator(self.number_list)]
        all_products = [self.combinations_product(x) for x in self.all_consecutive_combinations_generator(self.number_list)]
        return len(all_products) == len(set(all_products))
