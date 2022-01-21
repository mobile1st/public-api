from dotenv import dotenv_values


class ENV:
    def __init__(self, param=None):
        if param:
            self.get_value(param)

    def get_value(self, param):
        return dotenv_values()[param]

    def get_db_uri(self):
        host = self.get_value("PROD_DB_HOST")
        user = self.get_value("PROD_DB_USER_NAME")
        db_pass = self.get_value("PROD_DB_PASSWORD")
        db_name = self.get_value("PROD_DB_NAME")
        db_port = self.get_value("DB_PORT")
        return f'mysql+pymysql://{user}:{db_pass}@{host}:{db_port}/{db_name}'
