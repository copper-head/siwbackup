import os
import shutil
import tarfile
import logging

# define logging function


class Backup:

    def __init__(self, source, destination, logfile, loglevel):
        self.source = source
        self.destination = destination
        self.loglevel = loglevel


    def full_file_backup(self, logfile):
        logformat = '%(asctime)-15s %(message)s'
        log = logging.basicConfig(format=logformat, filename=logfile)
        for item in os.listdir(self.source):
            srcitempath = str(self.source + item)
            destitempath = str(self.destination + item)
            try:
                shutil.copy(src=srcitempath, dst=destitempath, follow_symlinks=True)
            except OSError:
                log.error("siwbackup was unable to copy file: {}".format(item))

