import calendar
import time

from urllib.parse import urlparse


class TemporaryLink:
    """ """

    def __init__(self):
        self.url = None
        self.domain = None

        self.flag_for_removal = False

        # Internally
        self.registered = 0

    def set_url(self, VARIABLE_VALUE):
        self.url = VARIABLE_VALUE
        return self.get_url()

    def get_url(self):
        return self.url

    def get_registered(self):
        return self.registered

    def get_domain(self):
        return self.domain

    def set_flag_for_removal(self, VARIABLE_VALUE):
        self.flag_for_removal = VARIABLE_VALUE
        return self.get_flag_for_removal()

    def get_flag_for_removal(self):
        return self.flag_for_removal

    def set_registered(self, VARIABLE_VALUE):
        self.registered = VARIABLE_VALUE
        return self.get_registered()

    def set_domain(self, VARIABLE_VALUE):
        self.domain = VARIABLE_VALUE

    def register(self):
        self.set_registered( calendar.timegm( time.gmtime() ) )

    def parse_host(self):
        try:
            uritokens = urlparse(self.get_url())
            self.set_domain(uritokens.netloc)

            return self.get_domain()
        except Exception:
            print(str(Exception))

        return None

    def print(self):
        ret_value = None

        ret_value = 'url: ' + str(self.get_url()) + '\r\n'
        ret_value = ret_value + 'domain: ' + str(self.get_domain()) + '\r\n'
        ret_value = ret_value + 'registered: ' + str(self.get_registered()) + '\r\n'
        ret_value = ret_value + 'flagged for removal: ' + str(self.get_flag_for_removal())

        return ret_value

