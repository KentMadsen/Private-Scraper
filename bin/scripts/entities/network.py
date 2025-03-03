from bin.scripts.entities.link import Link
from bin.scripts.entities.domain import Domain

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

    def add_domain(self, tmp_link):
        element = Domain()

        if self.exist_domain(tmp_link):
            return None

        element.set_name(tmp_link.get_domain())

        self.registry.append(element)

        return element

    def exist_domain(self, tmp_link):
        if len(self.registry) == 0:
            return False

        for domain in self.registry:
            if domain.get_name() == tmp_link.get_domain():
                return True
        return False

    def add_uri(self, tmp_link):
        if self.exist_uri(tmp_link):
            return None

        element = Link()

        for domain in self.registry:
            if domain.get_name() == tmp_link.get_domain():
                element.set_domain(domain)
                element.set_content(tmp_link.get_url())

                domain.add_url(element)

        return element

    def exist_uri(self, tmp_link):
        for domain in self.registry:
            if domain.get_name() == tmp_link.get_domain():
                return domain.exist_url(tmp_link.get_url())

        return False