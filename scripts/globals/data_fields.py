# Static Variables

field_zero = 0


def access_static_field__number__zero():
    global field_zero
    return field_zero


field_reset = -1


def access_static_field__number__reset():
    global field_reset
    return field_reset


# Errors
field_special_major = 'major'


def access_static_field__text__error__major_error():
    global field_special_major
    return field_special_major


field_special_minor = 'minor'


def access_static_field__text__error__minor_error():
    global field_special_minor
    return field_special_minor


field_special_status = 'status'


def access_static__text__field_debug_status():
    global field_special_status
    return field_special_status


field_special_message = 'message'


def access_static__text__field_message():
    global field_special_message
    return field_special_message


field_special_debug = 'debug'


def access_static__text__field_debug():
    global field_special_debug
    return field_special_debug


field_special_trash = 'trash'


def access_static__text__field_trash():
    global field_special_trash
    return field_special_trash


field_special_unknown = 'unknown'


def access_static__text__field():
    global field_special_unknown
    return field_special_unknown


field_special_attachment = 'attachment'


def access_static__text__field():
    global field_special_attachment
    return field_special_attachment


field_special_source = 'source'
field_special_message_type = 'type of message'


# Short names
def asft_trash():
    return access_static__text__field_trash()


def asft_debug():
    return access_static__text__field_debug()


def asft_message():
    return access_static__text__field_message()


def asft_debug_status():
    return access_static__text__field_debug_status()


def asft_error_major():
    return access_static_field__text__error__major_error()


def asft_error_minor():
    return access_static_field__text__error__minor_error()


#
def asfi_reset():
    return access_static_field__number__reset()


def asfi_zero():
    return access_static_field__number__zero()


field_link = 'link'
field_link_container = 'links'

field_domain = 'domain'

field_register = 'registered'
field_last = 'last visited'
field_look_up = 'last seen'

field_special_flagged_for_deletion = 'flagged for deletion'

