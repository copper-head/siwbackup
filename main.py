# -- module for loading SIW configuration -- #
#
#
# -- Last edited by: Duncan Truitt 9-4-21 -- #


import yaml


class Config:

    # param:
    #
    #   path: Full file path to yaml config file

    def __init__(self, path):
        self.config_path = path

        # Raise Error if path input != String
        if type(path) != str:
            raise TypeError('{} : ---- Config Path input must be a string!'.format(path))

        # Load yaml config file and dump raw contents into a var
        self.config_file = open(path, 'r')
        self.config_file_raw = self.config_file.read()
        self.config_file.close()

        self.yaml_dict = yaml.load(self.config_file_raw, Loader=yaml.FullLoader)

        #TO DO: ADD PORTION TO CHECK ALL ESSENTIAL PORTIONS OF THE YAML FILE EXIST





my_loader = Config('example_config.yaml')

print(my_loader.yaml_dict)