import logging
import os
import datetime


time = datetime.datetime.now().strftime("%d_%m_%y_%H_%M_%S")
file_name = str(time)+".log"
path = os.path.join(os.getcwd(),"logs")
os.makedirs(path, exist_ok=True)
Log_file_path = os.path.join(path,file_name)

logging.basicConfig(
    filename=Log_file_path,
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logging.info("logging started")
