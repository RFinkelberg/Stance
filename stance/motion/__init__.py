import logging

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                                       '%H:%M:%S'))
logger.addHandler(handler)
logger.setLevel(logging.INFO)
