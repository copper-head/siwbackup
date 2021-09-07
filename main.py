# -- module for loading SIW configuration -- #
#
#
# -- Last edited by: Duncan Truitt 9-7-21 -- #

# ----- TO DO ----- #
# 1. Add code to check to make sure that config file formating is correct
# 2.

import yaml
import time
import datetime


class Config:

    # param:
    #
    #   path: Full file path to yaml config file

    def __init__(self, path):
        self.config_path = path

        # Raise Error if path input != String
        if type(path) != str:
            raise TypeError('{} : ---- Config Path input must be a string!'.format(path))


        # Load yaml config file and dump raw contents into a var as well as create two attributes that hold the source and destination paths
        try:
            self.config_file = open(path, 'r')
        except FileNotFoundError:
            print('Cofiguration file not found.')
            print()
            input('Press enter to exit: ')
            exit()

        self.config_file_raw = self.config_file.read()
        self.config_file.close()
        self.yaml_dict = yaml.load(self.config_file_raw, Loader=yaml.FullLoader)
        self.source_path = self.yaml_dict['source']
        self.destination_path = self.yaml_dict['destination']


        # Blank dict that will hold lists of backupjobs for each day of the week
        self.backup_jobs = {
            'monday': [],
            'tuesday': [],
            'wednesday': [],
            'thursday': [],
            'friday': [],
            'saturday': [],
            'sunday': []
        }


        # Loads backup jobs into a dictionary with day_of_week keys that each hold a list of backup_jobs with time and backup_type values
        for job in self.yaml_dict['backup_jobs']:
            job_elements = job.split('-')
            self.backup_jobs[job_elements[0]].append({'time': job_elements[1], 'backup_type': job_elements[2]})


my_loader = Config('example_config.yaml')

print(my_loader.backup_jobs)
