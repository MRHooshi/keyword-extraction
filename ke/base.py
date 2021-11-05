
class BaseExtractor:
    def get_keywords(self, number):
        pass

    def extract(self, number = 5):
        return self.get_keywords(number=number)
