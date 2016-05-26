db.define_table('Empresa',
    Field('usuario', 'reference UsuarioExterno',
          requires=[IS_NOT_EMPTY(error_message='Es necesario un email.'),IS_EMAIL
                               (error_message='Introduzca un email valido.') ],
          label='Email(*)'),
    Field('nombre','string',
          requires=[IS_NOT_EMPTY(error_message='Es necesario un nombre.') ],
          label = 'Nombre (*)',
          comment='nombre@mail.com',
          ),
    Field('area_laboral','reference Area_Laboral',
          label = 'Area Laboral'),
    Field('descripcion',
          label='Descripcion'),
    Field('direccion_web',##verificador de urls
          label = 'Pagina Web'),
    Field('contacto_RRHH',
          label='Contactos De Recursos Humanos',requires=[IS_NOT_EMPTY(error_message='Es necesario un email.'),IS_EMAIL
                               (error_message='Introduzca un email valido.')])

)

db.Empresa.area_laboral.requires=IS_IN_DB(db,db.Area_Laboral.id,'%(nombre)s')