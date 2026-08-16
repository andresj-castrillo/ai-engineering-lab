from datetime import datetime, timezone
import pytest
from pydantic import ValidationError
from app.models import IngestRequest, ScrapedPage

# Crear test para cada caso

# test para url valida
def test_ingest_request_accepts_valid_url():
    # dar una url valida
    request = IngestRequest(url = "https://example.com")

    # respuesta esperada
    assert str(request.url) == "https://example.com/"


# test para url invalida
def test_ingest_request_rejects_invalid_url():
    # dar url invalida, pydantic deberia devolver el ValidationError
    with pytest.raises(ValidationError):
        IngestRequest(url = "url-invalida")

