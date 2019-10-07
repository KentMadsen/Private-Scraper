class Crawler:
    def __init__(self):
        self.title = None
        self.url = None


    def set_url(self, VARIABLE_VALUE):
        self.url = VARIABLE_VALUE

    def get_url(self):
        return self.url

    def initialise(self):

        self.open()
        return

    def open(self):
        return None

    def close(self):
        return None
