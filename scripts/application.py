from scripts import global_variables

from scripts.business import Business
from scripts import static_data


class Application:

    def __init__(self):
        self.business_layer = Business()

        self.output = static_data.access_default_output_data()

    def initialise(self):
        self.business_layer.stage_setup()

        return None

    def execution(self):
        while global_variables.access_state_current_state_of_operation():
            self.business_layer.stages()

        return None

    def done(self):
        print(self.access_output())

    # Accessor
    def access_output(self):
        return self.output

    def edit_output(self, VARIABLE_VALUE):
        self.output = VARIABLE_VALUE


