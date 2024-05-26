from sqlalchemy.orm import sessionmaker
# se importa la clase(s) del
# archivo crear_entidades
from crear_entidades import localesdecomida, centrosdeportivos
# se importa el engine
from base_datos import engine

# Se crea una clase llamada Sessión,
# desde el generador de clases de SQLAlchemy
# sessionmaker.
Session = sessionmaker(bind=engine) # Se usa el engine
# Importante, se crea un objeto llamado session
# de tipo Session, que permite: permitir guardar, eliminar,
# actualizar y generar consultas a la base de datos.
session = Session()

# se crea un objetos de tipo locales-comida
local1 = localesdecomida(nombre="GING ASAI", ubicacion="La Joya")
local2 = localesdecomida(nombre="MIYAKO", ubicacion="Urdesa")
local3 = centrosdeportivos(pasillos="A1", estantes="balones")
local4 = centrosdeportivos(pasillos="A2", estantes="zapatos")
# se agrega los objetos de tipo Autor a la sesión
# a la espera de un commit
session.add(local1)
session.add(local2)
session.add(local3)
session.add(local4)

# se necesita confirmar los cambios que existan en la sessió
# se usar commit
session.commit()

