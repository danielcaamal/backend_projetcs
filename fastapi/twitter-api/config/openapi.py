from fastapi.openapi.utils import get_openapi

def custom_openapi(app):
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Twitter API - FastAPI",
        version="1.0.0",
        description="OpenAPI schema for Twitter",
        routes=app.routes,
        contact={
            'email':'danielcaamal97@gmail.com'
        }
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app