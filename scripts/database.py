import mysql.connector

from mysql.connector import Error


class Database:
    def __init__(self):

        self.connector = None

        self.hostname = None
        self.database = None

        self.username = None
        self.password = None

        self.updated = False

    #
    def connect_pipeline(self):
        ret_val = None

        try:
            self.connector = mysql.connector.connect(host=self.get_hostname(),
                                                     database=self.get_database(),

                                                     user=self.get_username(),
                                                     password=self.get_password(),

                                                     connection_timeout=320)

            ret_val = self.connector

        except Error:
            print(format(Error))

        return ret_val

    def disconnect_pipeline(self):
        ret_value = None

        if self.connector is None:
            raise ValueError('Connector not instantiated')

        if not self.connector.is_connected():
            raise ValueError('is offline')

        try:
            self.connector.close()

        except Error:
            print(str(Error))

        ret_value = self.connector

        return ret_value

    def finalize(self):
        if not self.is_pipeline_connected():
            raise ValueError('connection is offline')

        if self.updated:
            self.connector.commit()

        self.disconnect_pipeline()

    def is_pipeline_connected(self):
        return_value = self.connector.is_connected()
        return return_value

    # Accessor
    def set_hostname(self, VARIABLE_VALUE):
        self.hostname = VARIABLE_VALUE
        return self.hostname

    def set_database(self, VARIABLE_VALUE):
        self.database = VARIABLE_VALUE
        return self.database

    def set_username(self, VARIABLE_VALUE):
        self.username = VARIABLE_VALUE
        return self.username

    def set_password(self, VARIABLE_VALUE):
        self.password = VARIABLE_VALUE
        return self.password

    def get_updated(self):
        return self.updated

    def get_hostname(self):
        return self.hostname

    def get_database(self):
        return self.database

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_records(self, sql):
        records = None
        cursor = None

        try:
            cursor = self.connector.cursor()
            cursor.execute(sql)

            records = cursor.fetchall()

        except Error:
            print(str(Error))


        return records

    def print_status(self):
        print('username: ' + str(self.username))
        print('password: ' + str(self.password))
        print('database: ' + str(self.database))
        print('hostname: ' + str(self.hostname))

