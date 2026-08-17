from __future__ import annotations 
import asyncio # libreria estandar para programacion asincrona
from datetime import datetime, timezone
import httpx # cliente http asincrono
from bs4 import BeautifulSoup # libreria para analizar/extraer datos HTML

from app.models import ScrapedPage

REQUEST_TIMEOUT_SECONDS = 10
MAX_TEXT_CHARS = 5000

class ScrapeError(Exception):
    """"
    Tener excepciones propias en el caso de que algo
    falle en el scrape unicamente, reducir excepciones
    httpx a gestionar en el codigo
    """


async def fetch_and_parse(url: str) -> ScrapedPage:
    """" GET de la url, parsearla, retornar un objeto de ScrapedPage validado
    try/except 1. para errores httpx.RequestError
    2. para cuando el servidor responde pero con un codigo 400/50
    """

    try: 
        # usar AsyncClient (context manager) para abrir las conexiones 
        # asegurarnos de que se cierra aunque se
        # produzca una excepcion dentro del bloque

        # manejar aca timeout del cliente y redirecciones por si redirecciona de http a https
        async with httpx.AsyncClient(timeout=REQUEST_TIMEOUT_SECONDS, follow_redirects=True) as client: 
            response = await client.get(url) # peticion GET y ceder control (await)

    except httpx.RequestError as exc: # lanzar errores de tipo ScrapeError a cualquiera que sea de httpx, falla red, timeout, etc
        raise ScrapeError(f"Network error fetching {url}: {exc}") from exc

    if response.status_code >= 400: # verificar manualmente si hay codigo de error (el httpx no lanza excepciones de estos)
        raise ScrapeError(f"Fetch failed with status {response.status_code} for {url}")


    # BeatifulSoap ya es sincrono entonces no toca poner await, yava en el flujo principal
    # creo que se puede hacer el offloading a hilos o pero esto es pagina HTML basica asi que meh

    soup = BeautifulSoup(response.text, "html.parser") # procesar codigo HTML que viene de la respuesta

    # verificar si tiene la etiqueta de <title> y hacerle strip para sacar el titulo sin espacios in fin
    # soup.title verifica la etiqueta exista .string verifica que no este vacia
    title = soup.title.string.strip() if soup.title and soup.title.string else None

    # soup.get_text(separtor= " ") extraer todo el texto y sustituir etiquetas por espacio
    # .split dividir texto en lista de palabras y el " ".join funcionaria para unirlas otra vez pero 
    # con solo un espacio 
    text = " ".join(soup.get_text(separator=" ").split())

    return ScrapedPage( #devolver objeto scrapedPage con lo que parseamos ya
        url = url,
        title = title,
        text = text[:MAX_TEXT_CHARS], # despues del formateo nada mas 5000 carac
        fetched_at = datetime.now(timezone.utc),
        status_code = response.status_code,
    )

    
    