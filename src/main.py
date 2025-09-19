from fastapi import FastAPI

from .routes import student_routes, health_routes, route_routes, wall_routes

app = FastAPI(title="Route Logger API", summary="Route Logger backend")

def registerApi():
    app.include_router(student_routes.router)
    app.include_router(health_routes.router)
    app.include_router(route_routes.router)
    app.include_router(wall_routes.router)

registerApi()