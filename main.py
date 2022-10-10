# -*- coding: utf-8 -*-
import logging
import os
import shutil

from filecmp import cmp

logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler()
logger.setLevel(level=logging.INFO)
logger.addHandler(stream_handler)
file_handler = logging.FileHandler("./log.log")
formatter = logging.Formatter("%(asctime)s : %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

REMOVE_PATH = "C:\\Users\\gunho\\Desktop\\temp_176GB_v.22.9.15"
ORIGIN_PATH = "D:\\__home"
TRASH = "C:\\Users\\gunho\\Desktop\\Trash"
NEED_CHECK = "C:\\Users\\gunho\\Desktop\\Check"

check_num = 1


def find_file(ORIGIN_PATH, remove_file_path):
    for root, dirs, files in os.walk(ORIGIN_PATH):
        for fname in files:
            full_fname = os.path.join(root, fname)
            if cmp(full_fname, remove_file_path):
                logger.info("  [+] Match: " + str(full_fname))
                try:
                    shutil.move(remove_file_path, TRASH)
                except Exception as e:
                    logging.exception(e)

                return True
    return False


for root, dirs, files in os.walk(REMOVE_PATH):
    for fname in files:
        full_fname = os.path.join(root, fname)
        logger.info("[*][" + str(check_num) + "] Now: " + str(full_fname))
        if find_file(ORIGIN_PATH, remove_file_path=full_fname):
            print("=============== OK... Find! ===============")
        else:
            logger.info("  [-] Not Found!")
            # try:
            #     shutil.move(full_fname, NEED_CHECK)
            # except Exception as e:
            #     logging.exception(e)
        check_num += 1
