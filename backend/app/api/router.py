from fastapi import APIRouter

from app.api.routes import auth, districts, forecast, risk

router = APIRouter(prefix="/api")

router.include_router(risk.router)
router.include_router(districts.router)
router.include_router(forecast.router)
router.include_router(auth.router)
