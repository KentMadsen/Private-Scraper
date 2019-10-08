from bin.scripts.business import Business


class Application:
    """ """

    def __init__(self):
        self.business_layer = Business()
        self.continue_process = True

    def initialise(self):
        self.business_layer.stage_setup()

        return None

    def execution(self):
        while self.continue_process:
            self.business_layer.stages()

        return None

    def done(self):
        print(self.access_output())

    # Accessor
    def access_output(self):
        return self.output

    def edit_output(self, VARIABLE_VALUE):
        self.output = VARIABLE_VALUE

    def set_program_layer(self, variable_value):
        self.business_layer.set_program_layer(variable_value)
        return

    def get_continue_process(self):
        return self.continue_process

    def set_continue_process(self, variable):
        self.continue_process = variable
        return self.continue_process


