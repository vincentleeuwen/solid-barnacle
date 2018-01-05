class Allergies(object):

    def __init__(self, score):
        items = {
            1: 'eggs',
            2: 'peanuts',
            4: 'shellfish',
            8: 'strawberries',
            16: 'tomatoes',
            32: 'chocolate',
            64: 'pollen',
            128: 'cats',
        }
        self.allergies = []
        for i in [1024, 512, 256] + sorted(items, reverse=True):
            if i <= score:
                score -= i
                try:
                    self.allergies.append(items[i])
                except KeyError:
                    pass  # ignore higher items

    def is_allergic_to(self, item):
        return item in self.allergies

    @property
    def lst(self):
        return self.allergies
