from fastapi import FastAPI

app = FastAPI(
    title="Fibr Quiz Task Backend"
)

@app.get("/")
def api():
    return {"message": "Quiz Backend"}