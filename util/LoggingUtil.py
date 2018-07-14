import logging

def print_log(msg,**kw):
    logging.basicConfig(level=logging.DEBUG)
    logging.debug(msg,**kw)