# Global Variables
Global_Operation_Continue_Process = True
#
Global_Show_Messages_in_general = True

#
Global_Show_Messages_MajorErrors = True
Global_Show_Messages_MinorErrors = True

Global_Show_Messages_Status = True
Global_Show_Messages_Trash = True

Global_Show_Messages_Debug = True

Global_Maximum_Message = 500

global_domain_lock = True


#
def access_maximum_message():
    global Global_Maximum_Message
    return Global_Maximum_Message


def switch_maximum_message(VARIABLE_VALUE):
    global Global_Maximum_Message
    Global_Maximum_Message = VARIABLE_VALUE
    return Global_Maximum_Message


# Accessor
def access_show_major_errors():
    global Global_Show_Messages_MajorErrors
    return Global_Show_Messages_MajorErrors


def switch_show_major_errors(VARIABLE_VALUE):
    global Global_Show_Messages_MajorErrors
    Global_Show_Messages_MajorErrors = VARIABLE_VALUE
    return Global_Show_Messages_MajorErrors


    #
def access_show_minor_errors():
    global Global_Show_Messages_MinorErrors
    return Global_Show_Messages_MinorErrors


def switch_show_minor_errors(VARIABLE_VALUE):
    global Global_Show_Messages_MinorErrors
    Global_Show_Messages_MinorErrors = VARIABLE_VALUE
    return Global_Show_Messages_MinorErrors


#
def access_messages_allowed():
    global Global_Show_Messages_in_general
    return Global_Show_Messages_in_general


def switch_message_allowed(VARIABLE_VALUE):
    global Global_Show_Messages_in_general
    Global_Show_Messages_in_general = VARIABLE_VALUE
    return Global_Show_Messages_in_general


#
def access_state_trash_allowed():
    global Global_Show_Messages_Trash
    return Global_Show_Messages_Trash


def switch_state_trash_allowed(VARIABLE_VALUE):
    global Global_Show_Messages_Trash
    Global_Show_Messages_Trash = VARIABLE_VALUE
    return Global_Show_Messages_Trash


#
def access_state_status_allowed():
    global Global_Show_Messages_Status
    return Global_Show_Messages_Status


def switch_state_status_allowed(VARIABLE_VALUE):
    global Global_Show_Messages_Status
    Global_Show_Messages_Status = VARIABLE_VALUE
    return Global_Show_Messages_Status


#
def access_state_debug_allowed():
    global Global_Show_Messages_Debug
    return Global_Show_Messages_Debug


def switch_state_debug_allowed(VARIABLE_VALUE):
    global Global_Show_Messages_Debug
    Global_Show_Messages_Debug = VARIABLE_VALUE
    return Global_Show_Messages_Debug


#
def switch_state_of_operation(VARIABLE_VALUE):
    global Global_Operation_Continue_Process
    Global_Operation_Continue_Process = VARIABLE_VALUE
    return Global_Operation_Continue_Process


def access_state_current_state_of_operation():
    global Global_Operation_Continue_Process
    return Global_Operation_Continue_Process

