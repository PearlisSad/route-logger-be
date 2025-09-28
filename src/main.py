from fastapi import FastAPI

from .routes import health_routes, route_routes, wall_routes

app = FastAPI(title="Route Logger API", summary="Route Logger backend")


def registerApi():
    for route_module in [health_routes, route_routes, wall_routes]:
        app.include_router(route_module.router)


registerApi()
