zero = 0


class Network:
    global zero
    """ """

    def __init__(self):
        self.registry = []

    def status(self):
        print('Network Status')

        if self.size() == zero:
            print('network: registry is empty')
        else:
            for entry in self.registry:
                print(entry)

        return

    def size(self):
        return len(self.registry)

    def add_domain(self, domain_name):

        return None

    def exist_domain(self, domain_name):
        return None

    def add_uri(self, url_name):

        return None

    def exist_uri(self, uri_name):
        return None