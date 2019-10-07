from scripts.database import Database
from scripts.domain.crawler import Crawler
from scripts.domain.entities.network import Network


class Business:
    """ """

    def __init__(self):
        #
        self.databases = []
        #
        self.crawler = Crawler()
        self.network = Network()

        #
        self.temporary_storage_for_uris = []

        self.current_pos = 0

        self.flag_is_ready_output = False

    # Stage: initialise
    def stage_setup(self):
        # config files

        # setup internals
        self.setup_database()

        return None

    def setup_database(self):
        current = Database()

        current.set_database("crawler_tests")
        current.set_hostname("localhost")

        current.set_username("root")
        current.set_password("Epc63gez")

        self.databases.append(current)

        return current

    # Stage: execution
    def stages(self):
        #
        self.transference_process()
        self.execute()

        self.stage_garbage_collection()

        return None

    #
    def transference_process(self):
        #
        self.fetch_queue()

        #
        self.sort_network()

        #
        self.ready_queue()

        return None

    #
    def fetch_queue(self):
        for database in self.databases:
            database.connect_pipeline()

            records = database.get_records('SELECT content FROM seeds order by content;')

            for record in records:
                current_url = str(record[0])

                if not self.exist_uri_in_buffer(current_url):
                    print('Added to temperary registry: ' + current_url)
                    self.temporary_storage_for_uris.append(current_url)

            database.finalize()

        return self.temporary_storage_for_uris

    def exist_uri_in_buffer(self, VARIABLE_URI):
        if len(self.temporary_storage_for_uris) == 0:
            return False

        for uri in self.temporary_storage_for_uris:
            if uri == VARIABLE_URI:
                return True

        return False

    def ready_queue(self):


        return None

    def sort_network(self):
        # Sort values by domain, name


        return None

    def execute(self):
        still_working = True

        while still_working:
            uri = self.get_current_value()
            print("crawling - " + str(self.get_position()) + " : " + uri)

            self.next()


            #
            if self.get_position() == len(self.temporary_storage_for_uris):
                still_working = False
                self.set_position(0)

        return

    # Stage: Garbage Collection
    def stage_garbage_collection(self):

        return None

    def output(self):
        if self.get_flags_is_ready_output():
            self.ready_messages()

            print(self.process_messages())

        return None

    def ready_messages(self):
        return self.get_flags_is_ready_output()

    def is_messages_not_ready(self):
        return not self.get_flags_is_ready_output()

    def process_messages(self):
        return_value = ''

        return return_value

    def current_messages_count(self):

        return

    def get_position(self):
        return self.current_pos

    def set_position(self, VARIABLE_VALUE):
        self.current_pos = VARIABLE_VALUE
        return self.current_pos

    def next(self):
        self.set_position( (self.get_position() + 1) )
        return self.get_position()

    def previous(self):
        self.set_position( (self.get_position() - 1) )
        return self.get_position()

    def get_current_value(self):
        return self.temporary_storage_for_uris[self.current_pos]

    # Accessor
        # self.flag_is_ready_output
    def get_flags_is_ready_output(self):
        return self.flag_is_ready_output

    def set_flags_is_ready_output(self, value):
        self.flag_is_ready_output = value

        return self.flag_is_ready_output



