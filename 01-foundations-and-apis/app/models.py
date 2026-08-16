"""Pydantic schemas for data validation"""

from datetime import datetime
from pydantic import BaseModel, HttpUrl

class IngestRequest(BaseModel):
    # Lo que manda el cliente. HttpUrl valida automaticamente que se mande una Url valida/real

    url: HttpUrl

class ScrapedPage(BaseModel):
    # Lo que se devuelve despues del scraping

    # URL original
    url: HttpUrl

    # Titulo de la pagina web, puede ser el que tenga la pagina o ninguno en el caso de que no tenga definido
    title: str | None = None

    # Texto que se extrae, originalmente vacio
    text: str = ""

    # Fecha y Hora a la que se hizo el scraping
    fetched_at: datetime

    # Codigo de respuesta del servidor
    status_code: int
    