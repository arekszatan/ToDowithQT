import logging as log
from datetime import datetime

logName = datetime.today().strftime('%Y_%m_%d_logging.log')
log.basicConfig(level=log.INFO, filename=logName, filemode='w',
                format='%(asctime)s::%(levelname)s >>> %(message)s',
                datefmt='%d-%b-%y %H:%M:%S')

if __name__ == "__main__":
    log.info(f'Start application ToDo')
    from GUI.mainGUI import start_application
    start_application()
