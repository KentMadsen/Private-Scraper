global_messages = [

]


def access_global_message():
    global global_messages
    return global_messages


def set_global_messages(VARIABLE_VALUE):
    global global_messages
    global_messages = VARIABLE_VALUE

    return global_messages

