import logging

def configurar_logger():
    # Configurar el formato del mensaje
    formato = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

    # Configurar el nivel de registro (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    logging.basicConfig(level=logging.DEBUG, format=formato,
                        handlers=[
                            logging.FileHandler("registro.log"),  # Guardar en archivo
                            logging.StreamHandler()  # Mostrar en consola
                        ])


# Llamar a la función para configurar el logger
configurar_logger()

# Crear un logger
logger = logging.getLogger(__name__)
