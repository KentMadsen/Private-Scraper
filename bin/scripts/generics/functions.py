
import calendar

import time

from bin.scripts.globals import data_fields


#
def timestamp_now():
    return calendar.timegm(time.gmtime())


def is_numbers_equal(x, y):
    return x == y


def is_data_fields_elements_equal(a, b):
    if str.upper(a) == str.upper(b):
        return True

    return False


def inverse(value):
    if type(value is bool):
        return not value

    return False


def empty_index(idx):
    return idx == data_fields.asfi_zero()


def detect_index_error(idx):
    return idx == data_fields.asfi_reset()
