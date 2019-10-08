class Link:
    """ """

    def __init__(self):
        self.content = None
        self.domain = None

    def get_domain(self):
        return self.domain

    def set_domain(self, variable_value):
        self.domain = variable_value
        return self.get_domain()

    def get_content(self):
        return self.content

    def set_content(self, variable_value):
        self.content = variable_value
        return self.get_content()