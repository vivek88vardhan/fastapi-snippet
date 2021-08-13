#!/usr/bin/env python3

__author__ = "Girish Mallula"
__version__ = "0.1.0"
__license__ = "chandramgc@gmail.com"

from src.utils.logger import setLogger
from datetime import datetime
import argparse
import traceback

def main(args):
    try:
        logger = setLogger('FASTAPI',args.log)
        jobStartTime_dt = datetime.now()
        logger.info("Job method started : " + jobStartTime_dt.strftime("%m/%d/%Y %I:%M:%S.%f %p"))
        logger.info("Job method ended : " + jobStartTime_dt.strftime("%m/%d/%Y %I:%M:%S.%f %p"))
    except:
        traceback.print_exc()

if __name__ == '__main__':
    print('Starting main application...')

    import sys, os
    sys.path.append(os.getcwd())

    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    # Optional argument which requires a parameter (eg. -l test)
    parser.add_argument("-l", "--log", action="store", dest="log", default="INFO")

    args = parser.parse_args()
    main(args)


        