from fastapi import FastAPI
from app.models import IngestRequest, ScrapedPage
from app.scraper import fetch_and_parse

app = FastAPI()


@app.post("/scrape", response_model = ScrapedPage)
async def scrape_url(request: IngestRequest) -> ScrapedPage:
    """
    Crear endpoint para hacer el scrape a una pagina url, y retornar el resultado validado
    Como pasamos IngestRequest ya se revisa que sea una url valida
    Si es invalida ya aca FastApi retorna 422 
    """

    # el scraper se encarga de manejar los errores como los timeouts y >200 codigos
    # si existe uno de esas excepciones/errores de ScrapeError, FastApi tambien devuelve un error
    return await fetch_and_parse(str(request.url))