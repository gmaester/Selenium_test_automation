import logging
import time

class logs:
    def log(self, log_message):
        date = time.strftime('%d_%m_%Y, %H_%M_%S', time.localtime())
        logging.basicConfig(
            filename= fr'YOUR_PATH/log_{date}.txt',
            filemode= 'w',
            format= '%(asctime)s %(message)s',
            level= logging.INFO
        )
        logging.info(log_message)