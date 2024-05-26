from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
# se importa el engine
from base_datos import engine

# se crea la clase llamada Base que permite definir las clases bajo las
# características de SQLAlchemy
Base = declarative_base()

# Se crea la una entidad llamada localesdecomida, que hereda
# de Base
class localesdecomida(Base):
    __tablename__ = 'localesdecomida' # El nombre de la entidad en sqlite
    # Se definen los atributos
    id = Column(Integer, primary_key=True) # este atributo es entero y
                                        # se lo considera como llave
                                        # primaria
    nombre = Column(String) # atributo de tipo String
    ubicacion = Column(String)

    def __str__(self):
        return "%s %s %s %s" % (self.nombre, self.ubicacion)
class centrosdeportivos(Base):
    __tablename__ = 'centrosdeportivos' # El nombre de la entidad en sqlite
    # Se definen los atributos
    id = Column(Integer, primary_key=True) # este atributo es entero y
                                        # se lo considera como llave
                                        # primaria
    pasillos = Column(String) # atributo de tipo String
    estantes = Column(String)

    def __str__(self):
        return "%s %s %s %s" % (self.pasillos, self.estantes)

# Sentencia que permite crear o migrar las clases en Python al
# gestor de base de datos, expresado en el engine.
Base.metadata.create_all(engine)
