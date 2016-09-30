# -*- coding: utf-8 -*-

if db(db.Dedicacion.id > 0).count() == 0:
    db.Dedicacion.insert(
        nombre='Exclusiva'
    )
    db.commit()

if db(db.Division.id > 0).count() == 0:
    db.Division.insert(
        nombre='Ciencias Informaticas'
    )
    db.commit()

if db(db.Area_Proyecto.id > 0).count() == 0:
    db.Area_Proyecto.insert(
        nombre='Informatica Forense',
        descripcion=''
    )
    db.Area_Proyecto.insert(
        nombre='Sistema De Informacion',
        descripcion=''
    )
    db.commit()


if db(db.Sede.id > 0).count() == 0:
    db.Sede.insert(
        nombre='Sartenejas'
    )
    db.Sede.insert(
        nombre='Litoral'
    )
    db.commit()

if db(db.Pais.id > 0).count() == 0:
    db.Pais.insert(
        nombre='Venezuela'
    )
    db.Pais.insert(
        nombre='U.S.A.'
    )
    db.commit()

if db(db.Estado.id > 0).count() == 0:
    db.Estado.insert(
        nombre='Distrito Capital',
        Pais=1
    )
    db.Estado.insert(
        nombre='Aragua',
        Pais=1
    )
    db.commit()

if db(db.Etapa.id > 0).count() == 0:
    db.Etapa.insert(
        nombre='Preinscripcion',
        procedimientos='En las primeras cuatro semanas (semana 1 a semana 4) de cada trimestre académico se llevará a cabo el Proceso de Preinscripción de la Pasantía . Los estudiantes que desean optar a una pasantía deben preinscribirse al trimestre anterior al período de la pasantía a cursar. La preinscripción tendrá carácter obligatorio y el estudiante deberá consignar ante la CCTDS, o ante la CCCE según sea el caso, específicamente al personal de Atención al Estudiante, los siguientes recaudos:',
        descripcion='/#'
    )
    db.Etapa.insert(
        nombre='Colocacion',
        procedimientos='Después del proceso de Preinscripción, la sección de Relaciones con la Industria debe iniciar su proceso de búsqueda de pasantías mediante la comunicación con las empresas y la oferta de pasantes para el próximo período.',
        descripcion='/#'
    )
    db.Etapa.insert(
        nombre='Inscripcion',
        procedimientos='Durante la semana doce (12) del trimestre anterior a la pasantía y hasta la semana cero (0) del trimestre en el que se cursará la pasantía, se llevará a cabo el Proceso de Inscripción de la misma. Para ello, el estudiante debe descargar de la página web de la CCTDS (www.cctds.dex.usb.ve) los siguientes formularios (de carácter obligatorio)',
        descripcion='/#'
    )
    db.Etapa.insert(
        nombre='Ejecucion',
        procedimientos='Por contretar',
        descripcion='/#'
    )
    db.commit()

if db(db.Materia.id > 0).count() == 0:
    db.Materia.insert(
        codigo='EP3420',
        sede='1',
        tipo='Larga',
        descripcion='Lograr que el estudiante se integre a las actividades de la empresa o institución y actúe dentro de la misma como un recurso capaz de intervenir en el desarrollo completo de trabajos, tareas o proyectos a nivel profesional, utilizando para ello los conocimientos y la formación de que dispone.',
        duracion='20'
    )
    db.Materia.insert(
        codigo='EP1420',
        sede='1',
        tipo='Corta',
        descripcion='En las primeras cuatro semanas (semana 1 a semana 4) de cada trimestre académico se llevará a cabo el Proceso de Preinscripción de la Pasantía . Los estudiantes que desean optar a una pasantía deben preinscribirse al trimestre anterior al período de la pasantía a cursar. La preinscripción tendrá carácter obligatorio y el estudiante deberá consignar ante la CCTDS, o ante la CCCE según sea el caso, específicamente al personal de Atención al Estudiante, los siguientes recaudos:',
        duracion='6'
    )
    db.commit()

if db(db.Departamento.id > 0).count() == 0:
    db.Departamento.insert(
        nombre='Ciencias De La Informacion',
        id_division='1',
        email_dep='ci@usb.ve',
        sede='1',
    )
    db.commit()

if db(db.Periodo.id > 0).count() == 0:
    db.Periodo.insert(
        mes_inicio='Abril',
        mes_final='Septiembre'
    )
    db.Periodo.insert(
        mes_inicio='Abril',
        mes_final='Septiembre'
    )
    db.Periodo.insert(
        mes_inicio='Octubre',
        mes_final='Enero'
    )
    db.commit()

if db(db.Rol.id > 0).count() == 0:
    db.Rol.insert(
        nombre='Estudiante'
    )
    db.Rol.insert(
        nombre='Coordinador_CCT'
    )
    db.Rol.insert(
        nombre='Coordinador'
    )
    db.Rol.insert(
        nombre='Invitado'
    )
    db.Rol.insert(
        nombre='Profesor'
    )
    db.commit()

if db(db.Area_Laboral.id > 0).count() == 0:
    db.Area_Laboral.insert(
        nombre='Tecnologia',
        descripcion='tecnológica'
    )
    db.Area_Laboral.insert(
        nombre='Informatica',
        descripcion='Consultoria, desarrollo de software,etc'
    )
    db.Area_Laboral.insert(
        nombre='Legal',
        descripcion='Asesoria legal, resolucion de casos'
    )
    db.Area_Laboral.insert(
        nombre='Electricidad',
        descripcion='Instalaciones electricas'
    )
    db.Area_Laboral.insert(
        nombre='Arquitectura',
        descripcion='Diseño de planos'
    )
    db.commit()

if db(db.Universidad.id > 0).count() == 0:
    db.Universidad.insert(
        nombre='Universidad Simón Bolívar',
        id_pais=1
    )
    db.Universidad.insert(
        nombre='Universidad Católica Andrés Bello',
        id_pais=1
    )
    db.Universidad.insert(
        nombre='Universidad Metropolitana',
        id_pais=1
    )
    db.Universidad.insert(
        nombre='Universidad De Florida',
        id_pais=2
    )
    db.commit()

if db(db.Categoria.id > 0).count() == 0:
    db.Categoria.insert(
        nombre='Asociado'
    )
    db.Categoria.insert(
        nombre='Titular'
    )
    db.Categoria.insert(
        nombre='Agregado'
    )
    db.Categoria.insert(
        nombre='Asistente'
    )
    db.commit()

if db(db.Coordinacion.id > 0).count() == 0:
    db.Coordinacion.insert(
        nombre='Computacion',
        usbid='1000',
        sede=1
    )
    db.Coordinacion.insert(
        nombre='Mecanica',
        usbid='1001',
        sede=1
    )
    db.Coordinacion.insert(
        nombre='Coordinación de Cooperación Tecnica',
        usbid='1002',
        sede=1
    )
    db.commit()

if db(db.Carrera.id > 0).count() == 0:
    db.Carrera.insert(
        nombre='Ingenieria de la Computacion',
        codigo='0800',
        duracion='Larga',
        coordinacion=1
    )
    db.Carrera.insert(
        nombre='Ingenieria de Mecanica',
        codigo='0200',
        duracion='Larga',
        coordinacion=1
    )
    db.commit()

if db(db.Tipo_Documento.id > 0).count() == 0:
    db.Tipo_Documento.insert(
        nombre='Cedula'
    )
    db.Tipo_Documento.insert(
        nombre='Pasaporte'
    )
    db.Tipo_Documento.insert(
        nombre='RIF'
    )
    db.commit()

if db(db.Acceso_Etapa.id > 0).count() == 0:
    db.Acceso_Etapa.insert(
        rol='3',
        etapa='3'
    )
    db.Acceso_Etapa.insert(
        rol='2',
        etapa='2'
    )
    db.Acceso_Etapa.insert(
        rol='2',
        etapa='4'
    )
    db.Acceso_Etapa.insert(
        rol='2',
        etapa='3'
    )
    db.Acceso_Etapa.insert(
        rol='2',
        etapa='1'
    )
    db.commit()

if db(db.auth_group.id > 0).count() == 0:
    db.auth_group.insert(
        role='Estudiante',
        description='3'
    )
    db.auth_group.insert(
        role='Profesor',
        description='2'
    )
    db.auth_group.insert(
        role='Coordinador',
        description='4'
    )
    db.auth_group.insert(
        role='Empresa',
        description='3'
    )
    db.auth_group.insert(
        role='Tutor Industrial',
        description='3'
    )
    db.commit()

if db(db.auth_user.id > 0).count() == 0:
    db.auth_user.insert(
        id=1,
        first_name='Ecorp',
        last_name='',
        email='ecorp-admin@ecorp.com',
        username=None,
        password='pbkdf2(1000,20,sha512)$9e7fc40b64a2c681$edc7f2230715e6da7c5762a340af1357457867a6',
        registration_key='',
        reset_password_key='',
        registration_id='ecorp-admin@ecorp.com'
    )
    db.auth_user.insert(
        id=2,
        first_name='Francisco Javier',
        last_name='Sucre González',
        email='fsucre@integra.la',
        username=None,
        password='pbkdf2(1000,20,sha512)$a8021cc4975367f2$d9ea5c4e54a6663fe0e105979778b28e1f9d4ed8',
        registration_key='',
        reset_password_key='',
        registration_id=''
    )
    db.auth_user.insert(
        id=3,
        first_name='Enrique',
        last_name='Muguerza',
        email='emuguerza@gmail.com',
        username=None,
        password='pbkdf2(1000,20,sha512)$a8021cc4975367f2$d9ea5c4e54a6663fe0e105979778b28e1f9d4ed8',
        registration_key='',
        reset_password_key='',
        registration_id=''
    )
    db.auth_user.insert(
        id=4,
        first_name='Roberto Andres',
        last_name='Manzanilla',
        email='queso976@gmail.com',
        username=None,
        password='pbkdf2(1000,20,sha512)$a8021cc4975367f2$d9ea5c4e54a6663fe0e105979778b28e1f9d4ed8',
        registration_key='',
        reset_password_key='',
        registration_id=''
    )
    db.auth_user.insert(
        id=5,
        first_name='Hector Alejandro',
        last_name='Goncalves Pita',
        email='',
        username='10-10292',
        password='pbkdf2(1000,20,sha512)$a25f21cad42986e1$f4a52a8436c2f5f2bf6e24b8b35ffa3193244a35',
        registration_key='',
        reset_password_key='',
        registration_id=''
    )
    db.auth_user.insert(
        id=6,
        first_name='Daniel Arturo',
        last_name='Marin Tirado',
        email='',
        username='10-10419',
        password='pbkdf2(1000,20,sha512)$9b087027ff330ac0$6531b331348da4487a807605a7b44130af93beda',
        registration_key='',
        reset_password_key='',
        registration_id=''
    )
    db.auth_user.insert(
        id=7,
        first_name='Francisco Javier',
        last_name='Sucre Gonzalez',
        email='',
        username='10-10717',
        password='pbkdf2(1000,20,sha512)$b94c524c26eb4f03$b5ed28362b7422334de61ab389730cb8c3bf403c',
        registration_key='',
        reset_password_key='',
        registration_id=''
    )
    db.auth_user.insert(
        id=8,
        first_name='Roberto Antonio',
        last_name='Romero Barrientos',
        email='',
        username='10-10642',
        password='pbkdf2(1000,20,sha512)$915d2a6f4c2ff0f6$12040ff51286f9a3ffd970013fea95db0728ad9f',
        registration_key='',
        reset_password_key='',
        registration_id=''
    )
    db.auth_user.insert(
        id=9,
        first_name='Andres Rafael',
        last_name='Hernandez Monterola',
        email='',
        username='10-10353',
        password='pbkdf2(1000,20,sha512)$ad1699544ba1ac2f$dafd3e9e2a1ade4ec5aa3ead9cd2ad029b60d016',
        registration_key='',
        reset_password_key='',
        registration_id=''
    )
    db.commit()

if db(db.UsuarioExterno.id > 0).count() == 0:
    db.UsuarioExterno.insert(
        auth_User=1,
        nombre='Ecorp',
        correo='ecorp-admin@ecorp.com',
        clave='Ecorp.2016',
        pregunta_secreta='¿Cual es la solucion?',
        respuesta_secreta='¡Ecorp!',
        pais='1',
        estado='1',
        telefono='04128063009',
        direccion='Sartenejas'
    )
    db.UsuarioExterno.insert(
        auth_User=2,
        nombre='Francisco Javier',
        correo='fsucre@integra.la',
        clave='Ecorp.2016',
        pregunta_secreta='¿Mejor Equipo Del Futbol?',
        respuesta_secreta='Real Madrid',
        pais='1',
        estado='1',
        telefono='04128063009',
        direccion='Calle P1'
    )
    db.commit()

if db(db.UsuarioUSB.id > 0).count() == 0:
    db.UsuarioUSB.insert(
        id=3,
        auth_User=3,
        usbid='emuguerza',
        nombre='Enrique',
        apellido='Muguerza',
        correo='emuguerza@gmail.com',
        clave='123456789',
        tipo_documento='1',
        numero_documento='11234112',
        telefono='04122347576',
        direcUsuario='Caracas',
        sexo='M',
        rol='5',
        activo='True'
    )
    db.UsuarioUSB.insert(
        id=4,
        auth_User=4,
        usbid='10-10102',
        nombre='Roberto Andres',
        apellido='Manzanilla',
        correo='queso976@gmail.com',
        clave='123456789',
        tipo_documento='1',
        numero_documento='20101324',
        telefono='04129767576',
        direcUsuario='Prados Del Este',
        sexo='M',
        rol='1',
        activo='True'
    )
    db.UsuarioUSB.insert(
        id=5,
        auth_User=5,
        usbid='10-10292',
        nombre='Hector Alejandro',
        apellido='Goncalves Pita',
        correo='KKNKKMTGJYXLCURWCFAC',
        clave='21321312',
        tipo_documento='1',
        numero_documento='20101324',
        telefono='04243130932',
        direcUsuario='Prados Del Este',
        sexo='M',
        rol='5',
        activo='True'
    )
    db.UsuarioUSB.insert(
        id=6,
        auth_User=6,
        usbid='10-10419',
        nombre='Daniel Arturo',
        apellido='Marin Tirado',
        correo='NULL',
        clave='QHQNVEMXTOYMUGEEHEIZ',
        tipo_documento='1',
        numero_documento='21464359',
        telefono='0414-4742003',
        direcUsuario='merche',
        sexo='M',
        rol='2',
        activo='True'
    )
    db.UsuarioUSB.insert(
        id=7,
        auth_User=7,
        usbid='10-10717',
        nombre='Francisco Javier',
        apellido='Sucre Gonzalez',
        correo='10-10717@usb.ve',
        clave='MUVUEDMICWTEDTOQEEHF',
        tipo_documento='1',
        numero_documento='19564959',
        telefono='02127653852',
        direcUsuario='La Floresta',
        sexo='M',
        rol='1',
        activo='True'
    )
    db.UsuarioUSB.insert(
        id=8,
        auth_User=8,
        usbid='10-10642',
        nombre='Roberto Antonio',
        apellido='Romero Barrientos',
        correo='romero@gmail.com',
        clave='RXNTIYYFRUPCHHULMCOM',
        tipo_documento='1',
        numero_documento='20101324',
        telefono='04129767576',
        direcUsuario='Prados Del Este',
        sexo='M',
        rol='3',
        activo='True'
    )
    db.UsuarioUSB.insert(
        id=9,
        auth_User=9,
        usbid='10-10353',
        nombre='Andres Rafael',
        apellido='Hernandez Monterola',
        correo='queso976@gmail.com',
        clave='CJAISTOHHYHGUTSBTXGK',
        tipo_documento='1',
        numero_documento='20101324',
        telefono='04129767576',
        direcUsuario='Prados Del Este',
        sexo='M',
        rol='3',
        activo='True'
    )
    db.commit()

if db(db.Estudiante.id > 0).count() == 0:
    db.Estudiante.insert(
        id='4',
        usuario='4',
        carnet='10-10102',
        carrera='1',
        sede='1',
        activo='True'
    )
    db.Estudiante.insert(
        id='7',
        usuario='7',
        carnet='10-10717',
        carrera='1',
        sede='1',
        activo='True'
    )
    db.commit()

if db(db.Profesor.id > 0).count() == 0:
    db.Profesor.insert(
        id='3',
        usuario='3',
        categoria='1',
        dedicacion='1',
        departamento='1',
        sede='1',
        activo='True'
    )
    db.Profesor.insert(
        id='5',
        usuario='5',
        categoria='1',
        dedicacion='1',
        departamento='1',
        sede='1',
        activo='True'
    )
    db.commit()

if db(db.Empresa.id > 0).count() == 0:
    db.Empresa.insert(
        id='1',
        usuario='1',
        area_laboral='2',
        descripcion='Soluciones De Software',
        direccion_web='www.ecorp.com',
        contacto_RRHH='www.ecorp-rrhh@ecorp.com'
    )
    db.commit()

if db(db.Tutor_Industrial.id > 0).count() == 0:
    db.Tutor_Industrial.insert(
        id='2',
        usuario='2',
        apellido='Sucre González',
        Empresa='1',
        profesion='Consultor De Software',
        tipo_documento='1',
        numero_documento='19564959',
        cargo='Administrador De Base De Datos',
        departamento='Tecnologia De La Informacion',
        universidad='1',
        comfirmado_Por_Empresa='1'
    )
    db.commit()

if db(db.auth_membership.id > 0).count() == 0:
    db.auth_membership.insert(
        user_id='1',
        group_id='4'
    )
    db.auth_membership.insert(
        user_id='2',
        group_id='5'
    )
    db.auth_membership.insert(
        user_id='4',
        group_id='1'
    )
    db.auth_membership.insert(
        user_id='3',
        group_id='1'
    )
    db.auth_membership.insert(
        user_id='7',
        group_id='1'
    )
    db.commit()

if db(db.Accion_Usuario.id > 0).count() == 0:
    db.Accion_Usuario.insert(
        nombre='Acciones',
        destino='/SPE/acciones_usuario/listar',
        contexto='coordinacion',
        rol='2'
    )
    db.Accion_Usuario.insert(
        nombre='Mis Pasantias',
        destino='/SPE/mis_pasantias/listar',
        contexto='coordinacion',
        rol='1'
    )
    db.Accion_Usuario.insert(
        nombre='Pasantias',
        destino='/SPE/pasantias/listar',
        contexto='coordinacion',
        rol='2'
    )
    db.Accion_Usuario.insert(
        nombre='Pasantias',
        destino='/SPE/pasantias/listar',
        contexto=None,
        rol='3'
    )
    db.Accion_Usuario.insert(
        nombre='Editar Perfil',
        destino='/SPE/mi_perfil/configuracion',
        contexto='configuracion',
        rol='1'
    )
    db.Accion_Usuario.insert(
        nombre='Editar Curriculo',
        destino='/SPE/mi_perfil/editar_curriculo',
        contexto='configuracion',
        rol='1'
    )
    db.Accion_Usuario.insert(
        nombre='Usuarios',
        destino='/SPE/usuarios/listar',
        contexto='coordinacion',
        rol='2'
    )
    db.Accion_Usuario.insert(
        nombre='Estudiantes',
        destino='/SPE/estudiantes/listar',
        contexto='coordinacion',
        rol='2'
    )
    db.Accion_Usuario.insert(
        nombre='Sedes',
        destino='/SPE/sedes/listar',
        contexto='coordinacion',
        rol='2'
    )
    db.Accion_Usuario.insert(
        nombre='Carreras',
        destino='/SPE/carreras/listar',
        contexto='coordinacion',
        rol='2'
    )
    db.Accion_Usuario.insert(
        nombre='Coordinaciones',
        destino='/SPE/preinscripciones/listar',
        contexto='coordinacion',
        rol='2'
    )
    db.Accion_Usuario.insert(
        nombre='Colocaciones',
        destino='/SPE/colocaciones/listar',
        contexto='coordinacion',
        rol='2'
    )
    db.Accion_Usuario.insert(
        nombre='Inscripciones',
        destino='/SPE/inscripciones/listar',
        contexto='coordinacion',
        rol='2'
    )
    db.Accion_Usuario.insert(
        nombre='Mis Planes',
        destino='/SPE/mis_planes_tutor/listar',
        contexto='coordinacion',
        rol='2'
    )
    db.commit()

if db(db.Coordinador.id > 0).count() == 0:
    db.Coordinador.insert(
        usuario='6',
        carnet='10-10330',
        coordinacion = '3',
        correo_Alternativo='danielarturomt@gmail.com'
    )
    db.Coordinador.insert(
        usuario='8',
        carnet='10-10195',
        coordinacion = '1',
        correo_Alternativo='coord@copt.com'
    )
    db.Coordinador.insert(
        usuario='9',
        carnet='10-10292',
        coordinacion = '2',
        correo_Alternativo='asd@asd.com'
    )
    db.commit()

if db(db.Curriculo.id > 0).count() == 0:
    db.Curriculo.insert(
        estudiante='4',
        electivas='Diseño De Piezas',
        cursos = 'Matlab II',
        aficiones='Fifa 2016',
        idiomas='Español, Ingles',
        activo=True
    )
    db.Curriculo.insert(
        estudiante='7',
        electivas='Sistemas De Informacion II, Sistemas De Informacion III,Base De Datos II,Modelos Lineales II',
        cursos = 'Codeacademy',
        aficiones='Musica',
        idiomas='Español, Ingles,Portugues',
        activo=True
    )
    db.commit()