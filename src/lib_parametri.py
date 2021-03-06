#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Libreria dei parametri generali e di classi di parametri suddivisi per area.
"""


import time
from datetime import datetime

DEBUG = True

LISTA_AZIONI_POSSIBILI = ()
LISTA_STAGIONI = (1, 2)

START_TIME = time.time()
START_DATETIME = datetime.today()
DATE_FMT = '%Y-%m-%d %H:%M:%S'
DAY_FMT = '%Y-%m-%d'

LOG_FMT = '%(asctime)s - %(filename)-8s - %(funcName)-10s - %(levelname)-10s: %(message)s'
LOGFILE_FMT = ".log"
LOGFILE_MODE = {
    "write": "w",
    "append": "a"
}


# per ottenere il tempo intercorso dall'inizio dell'esecuzione
def get_elapsed_time(final_time):
    """
    Funzione per calcolo del tempo trascorso dall'inizio dell'esecuzione del
    programma

    :param final_time: tempo su cui effettuare il calcolo
    :type final_time: time.time
    :return: tempo trascorso dall'inizio dell'esecuzione
    :rtype: str
    """
    return str(final_time - START_TIME)


# ============================================================================ #
#### Parametri suddivisi per categorie
class BaseParameter(object):

    def __init__(self):
        pass


class ParametriWS(BaseParameter):

    def __init__(self):
        super(ParametriWS, self).__init__()
        self.ws_dict = {}


class ParametriDS(BaseParameter):

    def __init__(self):
        super(ParametriDS, self).__init__()

        self.lista_completa_DS = ()
        self.lista_ECI = ()
        self.lista_USA = ()
        self.lista_USA_completa = ()
        self.lista_europa = ()


class ParametriLogger(BaseParameter):

    def __init__(self):
        super(ParametriLogger, self).__init__()

        self.LOGFILE_PATH = '../log/'
        self.LOGFILE_NAME = str((datetime.today().date().strftime(DAY_FMT))) + \
                            LOGFILE_FMT
        self.STREAM_PATH = ''
        self.INFO = 'INFO'
        self.DEBUG = 'DEBUG'
        self.WARNING = 'WARNING'
        self.MODE = LOGFILE_MODE["append"]
        self.fmt = LOG_FMT
        self.fmt_date = DATE_FMT

