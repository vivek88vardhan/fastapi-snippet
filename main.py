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

        # Beginning main application
        jobStartTime_dt = datetime.now()        
        logger.info("Job method started : " + jobStartTime_dt.strftime("%m/%d/%Y %I:%M:%S.%f %p"))

        # Current application

        # Ending main application
        jobEndTime_dt = datetime.now()
        logger.info("Job method ended   : " + jobEndTime_dt.strftime("%m/%d/%Y %I:%M:%S.%f %p"))
        logger.info("Job duration       : " + str(int((jobEndTime_dt - jobStartTime_dt).total_seconds())) + " sec" )
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

    # Syntex for requires a parameter
    # parser.add_argument("--module", action="store", dest="module", default="sharepoint")

    args = parser.parse_args()
    main(args)


        