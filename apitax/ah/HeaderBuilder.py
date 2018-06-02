# Builder class for creating headers dynamically
class HeaderBuilder:
    def __init__(self):
        self.header = {}

    def build(self, header):
        self.header.update(header)

    def remove(self, header):
        return self.header.pop(header, None)

    def get(self):
        return self.header
