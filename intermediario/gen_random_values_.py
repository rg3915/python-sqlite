# -*- coding: utf-8 -*-
import random
import rstr
import datetime


def gen_age():
    # gera numeros inteiros entre 15 e 99
    return random.randint(15, 99)


def gen_cpf():
    # gera uma string com 11 caracteres numericos
    return rstr.rstr('1234567890', 11)


def gen_phone():
    # gera um telefone no formato (xx) xxxx-xxxx
    return '({0}) {1}-{2}'.format(
        rstr.rstr('1234567890', 2),
        rstr.rstr('1234567890', 4),
        rstr.rstr('1234567890', 4))


def gen_timestamp():
    # gera um datetime no formato yyyy-mm-dd hh:mm:ss.000000
    year = random.randint(1980, 2015)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    hour = random.randint(1, 23)
    minute = random.randint(1, 59)
    second = random.randint(1, 59)
    microsecond = random.randint(1, 999999)
    date = datetime.datetime(
        year, month, day, hour, minute, second, microsecond).isoformat(" ")
    return date


def gen_city():
    list_city = [
        [u'São Paulo', 'SP'],
        [u'Belém', 'PA'],
        [u'Rio de Janeiro', 'RJ'],
        [u'Goiânia', 'GO'],
        [u'Salvador', 'BA'],
        [u'Guarulhos', 'SP'],
        [u'Brasília', 'DF'],
        [u'Campinas', 'SP'],
        [u'Fortaleza', 'CE'],
        [u'São Luís', 'MA'],
        [u'Belo Horizonte', 'MG'],
        [u'São Gonçalo', 'RJ'],
        [u'Manaus', 'AM'],
        [u'Maceió', 'AL'],
        [u'Curitiba', 'PR'],
        [u'Duque de Caxias', 'RJ'],
        [u'Recife', 'PE'],
        [u'Natal', 'RN'],
        [u'Porto Alegre', 'RS'],
        [u'Campo Grande', 'MS']]
    return random.choice(list_city)
