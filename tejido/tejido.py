from sqlalchemy import create_engine, text

USUARIO = "tejido"
CONTRASENA = "tj123456"
HOST = "10.9.120.5"
PUERTO = 3306
BASE = "Tejido"

url = f"mysql+pymysql://{USUARIO}:{CONTRASENA}@{HOST}:{PUERTO}/{BASE}"
engine = create_engine(url)

with engine.connect() as conn:
    resultado = conn.execute(text("SELECT 1"))
    print("Conexión exitosa:", resultado.scalar())