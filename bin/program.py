from bin.scripts.application import Application

main_entry_function_name = '__main__'


#
def main():
    application = Application()
    application.set_program_layer(application)

    application.initialise()
    application.execution()

    return application.done()


#
if __name__ == main_entry_function_name:
    main()