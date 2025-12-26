from dataclasses import dataclass
import datetime
from enum import Enum


class EstadoTarea(Enum):
    PENDIENTE = 1
    EN_PROGRESO = 2
    COMPLETADA = 3




class ImportanciaTarea(Enum):
    BAJA= 1
    MEDIA= 2
    ALTA=3



@dataclass
class Tarea:
    titulo : str
    descripcion:str
    fecha_creacion: datetime.datetime
    fecha_entrega : datetime.datetime
    estado : EstadoTarea ### manejo de diccionario
    importancia :ImportanciaTarea ### diccionario 
