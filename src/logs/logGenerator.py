import logging


logger = logging.Logger

def setLogger():
    global logger
    logger = logging.getLogger()
    hdlr = logging.FileHandler('C:/Users/Dell/PycharmProjects/Selenium/src/Output/Logs.txt', mode='w')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.WARNING)
    return logger


def logInfo(text):
    logger.error(text, "major problem", exc_info=0)
    return

# if __name__ != '__main__':
#     setLogger()