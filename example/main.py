import os
import logging

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.getLogger('request').setLevel(logging.WARNING)
    os.mkdir("logs")
    try:
        with open("/logs/test.txt", "w") as f:
            f.write("is writing test file")
        logging.info("write test file success")
        print("write test file success")
    except Exception as e:
        logging.error(e)
        print(e)
