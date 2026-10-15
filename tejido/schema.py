from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey, create_engine
from sqlalchemy.orm import DeclarativeBase, relationship

class Base(DeclarativeBase):
    pass

class Cliente(Base):
    __tablename__ = "cliente"

    id      = Column(Integer, primary_key=True, autoincrement=True)
    nombre  = Column(String(100))
    pedido_id_id = Column(Integer, ForeignKey("pedido.id"))

    pedidos = relationship('Pedido', back_populates='cliente')

class Pedido(Base):
    __tablename__ = "pedido"

    id      = Column(Integer, primary_key=True, autoincrement=True)
    descripcion  = Column(String(200))
    precio = Column(Float)
    cliente_id = Column(Integer, ForeignKey("cliente.id"))

    cliente = relationship('Cliente', back_populates= 'pedidos')

USUARIO = "tejido"
CONTRASENA = "tj123456"
HOST = "10.9.120.5"
PUERTO = 3306
BASE = "Tejido"    
url = f"mysql+pymysql://{USUARIO}:{CONTRASENA}@{HOST}:{PUERTO}/{BASE}"
engine = create_engine(url)
Base.metadata.create_all(engine)

print("DataBase creada")