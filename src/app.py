from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/health")
    def health() -> tuple[dict[str, str], int]:
        return {"status": "ok"}, 200

    @app.get("/")
    def home() -> tuple[dict[str, str], int]:
        return {"message": "CI/CD project running"}, 200

    @app.get("/sum/<int:a>/<int:b>")
    def sum_values(a: int, b: int) -> tuple[dict[str, int], int]:
        return {"result": a + b}, 200

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
