from bin.scripts.business import Business


class Application:
    """ """

    def __init__(self):
        self.program_layer = None

        self.business_layer = Business()
        self.business_layer.set_business_layer(self.business_layer)

        self.continue_process = True

    def initialise(self):
        self.business_layer.stage_setup()

        return None

    def execution(self):
        while self.continue_process:
            self.business_layer.stages()

        return None

    def done(self):
        print('Completed')

    # Accessor
    def set_program_layer(self, variable_value):
        self.program_layer = variable_value
        return self.get_program_layer()

    def get_program_layer(self):
        return self.program_layer

    def append_structure_to_children(self):
        self.business_layer.set_program_layer(self.get_program_layer())
        return

    def get_continue_process(self):
        return self.continue_process

    def set_continue_process(self, variable):
        self.continue_process = variable
        return self.continue_process


