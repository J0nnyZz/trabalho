from src.app import create_app


def test_home_route() -> None:
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.get_json() == {"message": "CI/CD project running"}


def test_health_route() -> None:
    app = create_app()
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_sum_route() -> None:
    app = create_app()
    client = app.test_client()

    response = client.get("/sum/7/5")

    assert response.status_code == 200
    assert response.get_json() == {"result": 12}
