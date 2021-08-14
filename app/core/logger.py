import logging

def setLogger(logName,logLevel):
    # create console handler and set level to debug
    handler  = logging.StreamHandler()

    # create formatter
    #formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s [%(funcName)s:%(lineno)d] - %(message)s')

    # add formatter to ch
    handler.setFormatter(formatter)

    logger = logging.getLogger(logName)
    logger.setLevel(logLevel)

    # add handler to logger
    logger.addHandler(handler)

    return logger