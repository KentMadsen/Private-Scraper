from bin.scripts.entities.temp_link import TemporaryLink
import operator

zero = 0


class Buffer:
    global zero
    """ """

    def __init__(self):
        self.data = []

    def get(self, idx):
        ret_val = self.data[idx]
        return ret_val

    def add_element(self, element):
        link = TemporaryLink()

        link.set_url(element)
        link.parse_host()
        link.register()

        self.data.append(link)

        return self.data

    def status(self):
        for e in self.data:
            print("buffer------------------------------------ \r\n" + e.print() + "\r\n")

        return None

    def add_elements_from_list(self, list_of_elements):
        for element in list_of_elements:
            self.add_element(element)

        return

    def sort(self):
        self.data.sort(key=operator.attrgetter('domain', 'url'))

        return self.data

    def size(self):
        return len(self.data)

    def size_is_zero(self):
        return self.size() == zero

    def exist(self, uri):
        for link in self.data:
            if link.get_url() == uri:
                return True
        return False

    def clean(self):
        return

    def get_buffer(self):
        return self.data

    def set_buffer(self, data):
        self.data = data
        return self.data

    def remove(self, idx):
        self.get(idx).set_flag_for_removal(True)
        return self.get(idx)