from fastapi import FastAPI
import logging
my_app = FastAPI()

logging.basicConfig(filename='access.log',
                    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    level=10)

@my_app.get("/")
def read_index():
    logging.info("hello,word")
    return {"Hello":"World"}