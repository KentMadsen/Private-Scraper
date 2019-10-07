import scripts.data_fields
import scripts.generic


def print_message(message, exception, var_type):


    now = scripts.generic.timestamp_now()

    #
    if is_str_elements_equal(var_type, field_special_major) and scripts.globals.is_major_errors_allowed():
        print(str(now), var_type, message, str(exception), end=' | ')
        return True

    #
    if is_str_elements_equal(var_type, field_special_minor) and scripts.globals.is_minor_errors_allowed():
        print(str(now), var_type, message, str(exception), end=' | ')
        return True

    #
    if is_str_elements_equal(var_type, field_special_message) and scripts.globals.is_messages_allowed():
        print(str(now), var_type, message, end=' | ')
        return True

    #
    if is_str_elements_equal(var_type, field_special_debug) and scripts.globals.is_debug_allowed():
        print(str(now), var_type, message, end=' | ')
        return True

    #
    if is_str_elements_equal(var_type, field_special_trash) and scripts.globals.is_trash_allowed():
        print(str(now), var_type, message, end=' | ')
        return True

    #
    if is_str_elements_equal(var_type, field_special_status) and scripts.globals.is_status_allowed():
        print(str(now), var_type, message, end=' | ')
        return True

    return False
