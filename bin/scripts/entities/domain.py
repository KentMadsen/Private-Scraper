import operator


class Domain:
    """ """

    def __init__(self):
        self.name = ""
        self.urls = []

    def add_url(self, link):
        self.urls.append(link)

    def get_name(self):
        return self.name

    def get_urls(self):
        return self.urls

    def exist_url(self, variable_value):
        if len(self.urls) == 0:
            return False

        for element in self.urls:
            if element.content == variable_value:
                return True

        return False

    def set_urls(self, variable_value):
        self.urls = variable_value
        return self.get_urls()

    def set_name(self, variable_value):
        self.name = variable_value
        return self.get_name()

    def sort_list(self):
        self.urls.sort(key=operator.attrgetter('content'))
        return

