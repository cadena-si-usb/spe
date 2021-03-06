# -*- coding: utf-8 -*-
from gluon import *


def Fase_Table(db, T):
    db.define_table('Fase',
                    Field('numero', 'integer',
                          requires=[IS_NOT_EMPTY
                                    (error_message='Es necesario un numero de identificacion')],
                          label='Numero'),
                    Field('plan_trabajo', 'reference Plan_Trabajo',
                          label='Pasantía (*)',
                          writable=False),
                    Field('objetivo_especifico', 'text',
                          requires=[IS_NOT_EMPTY
                                    (error_message='Es necesario un objetivo')],
                          label='Objetivo Específico'),
                    Field('descripcion', 'text',
                          requires=[IS_NOT_EMPTY
                                    (error_message='Es necesario una Descripcion')],
                          label='Descripción'),
                    format=lambda r: '%s - %s' % (r.numero, r.objetivo_especifico)
                    )
