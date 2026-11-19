from src.main import app


def test_index():
    respuesta = app.test_client().get("/")
    assert respuesta.status_code == 200


def test_health():
    respuesta = app.test_client().get("/health")
    assert respuesta.get_json() == {"status": "ok"}


def test_ready():
    respuesta = app.test_client().get("/ready")
    assert respuesta.get_json() == {"status": "ready"}

