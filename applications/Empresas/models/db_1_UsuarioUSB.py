db.define_table('UsuarioUSB',
    Field('auth_User','reference auth_user'),
    Field('usbid', 'string',
          requires=[IS_NOT_EMPTY(error_message='Es necesario un usbid.')],
          label='USB ID (*)'),
    Field('nombre','string',
          requires=[IS_NOT_EMPTY(error_message='Es necesario un nombre.') ],
          label = 'Nombre (*)'),
    Field('apellido','string',
          requires=[IS_NOT_EMPTY(error_message='Es necesario un apellido.') ],
          label = 'Apellido (*)'),
    Field('correo',
          requires=IS_EMPTY_OR(IS_EMAIL(error_message='Introduzca un email valido.')),
          comment='nombre@mail.com',
          label = 'Email(*)'), 
    Field('clave', 'password',
          requires=[IS_NOT_EMPTY(error_message='Es necesaria una clave.'),
                    IS_STRONG(min=10, special=1, upper=1)],
          label = 'Contraseña (*)'),
    Field('tipo_documento','reference Tipo_Documento',
          label='Tipo de Documento (*)'),
    Field('numero_documento', 
          requires=[IS_MATCH('^[0-9][0-9]*$',
                        error_message='Introduzca una cedula.')],
          label='Numero Documentacion (*)' ),
    Field('telefono',
          requires=IS_MATCH('^\d{4}?[\s.-]?\d{7}$',                             
          error_message='Numero no valido,ingrese numero telefonico'),
          comment='0212-111111',
          label = 'Telefono(*)'),        
    Field('direcUsuario','text',
          label = 'Direccion'),
    Field('sexo',
          requires=IS_IN_SET(['M','F']),
          label = 'Sexo (*)'),
    Field('rol','reference Rol',
          label='Rol (*)'),
    Field('activo','boolean')
)
