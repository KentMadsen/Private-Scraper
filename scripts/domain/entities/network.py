import scripts.generics.functions


class Network:
    """ """

    def __init__(self):
        self.registry = []

    def add_domain(self, domain_name):
        element = {
            'domain name':domain_name,
            'urls': [],
            'registered': scripts.generics.functions.timestamp_now()
        }

        element['domain name'] = domain_name

        self.registry.append(element)

        return element

    def add_uri(self, url_name, domain_name):
        element = {
            'uri': url_name,
            'registered' : scripts.generics.functions.timestamp_now(),
        }

        for domain_element in self.registry:
            if domain_element['domain name'] == domain_name:
                domain_element['urls'].append(element)

        return None

    def exist_uri(self, url_name, domain_name):
        return None

    def exist_domain(self, domain_name):
        return None