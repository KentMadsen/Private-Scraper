from scripts.globals import data_fields


class Link:
    """ """
    def __init__(self):
        self.data = {
            data_fields.field_link: None,

            data_fields.field_register: None,
            data_fields.field_last: None
        }

    #
    def to_array(self):
        ret_arr = []

        for entries in self.data.items():
            ret_arr.append(entries)

        return ret_arr

    #
    def access_link(self):
        return self.data[data_fields.field_link]

    def access_registered(self):
        return self.data[data_fields.field_register]

    def access_last_visited(self):
        return self.data[data_fields.field_last]

    #
    def update_link(self, VARIABLE_VALUE):

        if not type(VARIABLE_VALUE is str):
            raise ValueError('is not a acceptable input value')

        self.data[data_fields.field_link] = VARIABLE_VALUE

        return self.data[data_fields.field_link]

    #
    def update_registered(self, VARIABLE_VALUE):

        if not type(VARIABLE_VALUE is int):
            raise ValueError('is not a acceptable input value')

        self.data[data_fields.field_register] = VARIABLE_VALUE

        return self.data[data_fields.field_link]

    #
    def update_last_visited(self, VARIABLE_VALUE):

        if not type(VARIABLE_VALUE is int):
            raise ValueError('is not a acceptable input value')

        self.data[data_fields.field_last] = VARIABLE_VALUE

        return self.data[data_fields.field_last]


#
class Network:
    """ """

    def __init__(self):
        print('')

        self.data = {

        }


class Buffer:
    """ """

    def __init__(self):
        print('')

        self.data = {

        }


# data_fields.field_reset()
# data_fields.asfi_reset()
# data_fields.access_static__text__field()

class Message:
    def __init__(self):
        print('')

        self.data = {
            data_fields.field_special_source: None,
            data_fields.field_register: None,
            data_fields.access_static__text__field(): None,
            data_fields.field_special_message_type: None
        }

    # Accessors
    def access_source(self):
        return self.data[data_fields.field_special_source]

    def access_registered(self):
        return self.data[data_fields.field_register]

    def access_last_lookup(self):
        return self.data[data_fields.field_last]

    def access_message_type(self):
        return self.data[data_fields.field_special_message_type]

    def update_source(self, VARIABLE_VALUE):
        self.data[data_fields.field_special_source] = VARIABLE_VALUE
        return self.data[data_fields.field_special_source]

    def update_registered(self, VARIABLE_VALUE):
        self.data[data_fields.field_register] = VARIABLE_VALUE
        return self.data[data_fields.field_register]

    def update_last_lookup(self, VARIABLE_VALUE):
        self.data[data_fields.field_last] = VARIABLE_VALUE
        return self.data[data_fields.field_last]

    def update_message_type(self, VARIABLE_VALUE):
        self.data[data_fields.field_special_message_type] = VARIABLE_VALUE
        return self.data[data_fields.field_special_message_type]

    def to_array(self):
        ret_arr = []

        for entries in self.data.items():
            ret_arr.append(entries)

        return ret_arr

# factory functions


def create_link_element(VARIABLE_USE_PREDEFINED_DATA):
    #
    element = Link()

    return element


#
    #element = {
        #data_fields.field_domain: None,
       # data_fields.field_link_container: [None],

      #  data_fields.field_register: data_fields.asfi_reset(),
     #   data_fields.field_last: data_fields.asfi_reset()
    #}

   # if VARIABLE_USE_PREDEFINED_DATA:
  #      now = generic.timestamp_now()

 #       element[data_fields.field_register] = now
#        element[data_fields.field_last] = now

def create_network_element(VARIABLE_USE_PREDEFINED_DATA):
    #
    element = Network()


    return element


# {
       # data_fields.field_domain:None,
      #  data_fields.field_link:None,

     #   data_fields.field_look_up:data_fields.asfi_reset(),
    #    data_fields.field_special_flagged_for_deletion: False
   # }

    #
  #  if VARIABLE_USE_PREDEFINED_DATA:
 #       now = generic.timestamp_now()

#        element[data_fields.field_look_up] = now


def create_buffer_element(VARIABLE_USE_PREDEFINED_DATA):
    #

    element = Buffer()

    return element


def create_message_element():
    #

    #element = {
    #    data_fields.field_special_source: data_fields.field_reset(),
   #     data_fields.field_register(): data_fields.asfi_reset(),
  #      data_fields.access_static__text__field(): None,
 #       data_fields.field_special_message_type: data_fields.access_static__text__field()
#    }

    #
    #if VARIABLE_USE_PREDEFINED_DATA:
     #   now = generic.timestamp_now()

      #  element[data_fields.field_register] = now

    element = Message()

    return element
