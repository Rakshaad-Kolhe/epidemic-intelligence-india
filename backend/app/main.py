from fastapi import FastAPI

from app.api.router import router as api_router

app = FastAPI(
    title="Epidemic Intelligence India",
    version="0.1.0"
)
app.include_router(api_router)


@app.get("/")
def root() -> dict[str, str]:
    return {"status": "running"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
