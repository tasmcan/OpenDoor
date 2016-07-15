from Logger import Logger as log

try:
    import os
    import StringIO
    import ConfigParser
    from random import randint
    from linereader import copen

except ImportError:
    log.critical("""You need linereader!
                install it from http://pypi.python.org/pypi
                or run pip install linereader """)


class FileReader:
    """Filereader class"""

    def __init__(self):

        try:
            config = self.get_config()
        except ConfigParser.ParsingError as e:
            log.critical(e.message)

        # Files useragents.dat
        useragents_file_path = config.get('opendoor', 'useragents')
        useragents_file = os.getcwd() + '/' + useragents_file_path;
        if not os.path.isfile(useragents_file) and not os.access(useragents_file, os.R_OK):
            log.critical(useragents_file_path + """ file can not be read """)
        self.__useragents_file = copen(useragents_file)
        self.__useragents_file_lines = self.__useragents_file.count('\n')

        # Files directories
        directories_file_path = config.get('opendoor', 'directories')
        directories_file = os.getcwd() + '/' + directories_file_path;
        if not os.path.isfile(directories_file) and not os.access(directories_file, os.R_OK):
            log.critical(directories_file_path + """ file can not be read """)
            log.critical(directories_file_path + """ file can not be read """)
        with open(directories_file) as f_handler:
            self.__directories_file = f_handler.readlines()
            self.__directories_file_lines = self.__directories_file.__len__()

    def get_user_agent(self):

        user_agent = self.__useragents_file.getline(1)

        return user_agent

    def get_random_user_agent(self):

        random_user_agent = self.__useragents_file.getline(randint(1, self.__useragents_file_lines)).splitlines()

        return random_user_agent

    def get_directories(self):
        return self.__directories_file

    def get_config(self):
        config = ConfigParser.RawConfigParser()
        config_file = os.getcwd() + '/setup.cfg'

        if not os.path.isfile(config_file) and not os.access(config_file, os.R_OK):
            log.critical("""Configuration file setup.cfg can not be read """)

        try:
            config.read(config_file)
            return config
        except ConfigParser.ParsingError as e:
            log.critical(e.message)

    def get_config_raw(self, s_config):
        buf = StringIO.StringIO(s_config)
        config = ConfigParser.ConfigParser()
        config.readfp(buf)
        return config