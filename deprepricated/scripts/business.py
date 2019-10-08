# Domain Area
from deprepricated.scripts.database import Database
from deprepricated.scripts.entities.network import Network
from deprepricated.scripts.entities.buffer import Buffer
from deprepricated.scripts.entities.counter import Counter

zero = 0


class Business:
    global zero
    """ """

    def __init__(self):
        #
        self.databases = []

        self.program_layer = None
        self.business_layer = None

        self.network = Network()

        #
        self.buffer = Buffer()
        self.history = None

        self.current_position = Counter()

        self.explore = False

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

        return self.databases

    # Stage: execution
    def stages(self):
        self.program_layer.set_continue_process(False)

        #
        self.transference_process()

        #
        self.execute()

        #
        self.stage_garbage_collection()

        return None

    #
    def transference_process(self):
        #
        self.fetch_queue()

        #
        self.ready_queue()

        #
        self.buffer.status()

        return None

    #
    def fetch_queue(self):
        for database in self.databases:
            database.connect_pipeline()

            records = database.get_records('SELECT content FROM seeds_available order by content;')

            for record in records:
                current_url = str(record[zero])

                if not self.buffer.exist(current_url):
                    self.buffer.add_element(current_url)

            database.finalize()

        return self.buffer

    def exist_uri_in_buffer(self, VARIABLE_URI):
        if self.buffer.size_is_zero():
            return False

        return self.buffer.exist(VARIABLE_URI)

    #
    def ready_queue(self):
        self.buffer.sort()

        # process the element
        #   # Move to internal representation of the map
        for tmp_link in self.buffer.get_buffer():
            self.network.add_domain(tmp_link)
            self.network.add_uri(tmp_link)

        self.network.sort()
        self.network.status()

        return None

    def execute(self):
        continue_execution_process = True

        while continue_execution_process:
            # retrieve current value at the given position
            uri = self.get_current_url()

            # flag is done and ready to be removed from the buffer. Move to the next element
            self.current_value_is_done()
            self.current_position.increment()

            #
            if self.check_position():
                continue_execution_process = False
                self.current_position.reset()

        return

    def check_position(self):
        return self.current_position.get_value() >= self.buffer.size()

    # Stage: Garbage Collection
    def stage_garbage_collection(self):
        self.buffer.clean()
        return None

    def get_current_url(self):
        return self.buffer.get(self.current_position.get_value()).get_url()

    def get_current_domain(self):
        return self.buffer.get(self.current_position.get_value()).get_domain()

    def current_value_is_done(self):
        self.buffer.get(self.current_position.get_value()).set_flag_for_removal(True)

    # Accessor
        # self.flag_is_ready_output
    def get_flags_is_ready_output(self):
        return self.flag_is_ready_output

    def set_flags_is_ready_output(self, value):
        self.flag_is_ready_output = value

        return self.flag_is_ready_output

    #
    def set_program_layer(self, value):
        self.program_layer = value
        return self.get_program_layer()

    def get_program_layer(self):
        return self.program_layer

    def set_business_layer(self, value):
        self.business_layer = value
        return self.get_business_layer()

    def get_business_layer(self):
        return self.business_layer





