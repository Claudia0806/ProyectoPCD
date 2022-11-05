from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import pandas as pd
from fastapi import Security, Depends, FastAPI, HTTPException
from fastapi.security.api_key import APIKeyQuery, APIKey

from starlette.status import HTTP_403_FORBIDDEN
# from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Book Recommender API",
              description="Esta API tiene un endpoint que se usa para obtener recomendaciones de libros"
                          "con base en un libro ingresado por el usuario.",
              version="0.0.1")

API_KEY = "1234567asdfgh"
API_KEY_NAME = "access_token"

api_key_query = APIKeyQuery(name=API_KEY_NAME, auto_error=False)


def get_api_key(api_key_query: str = Security(api_key_query)):

    if api_key_query == API_KEY:
        return api_key_query
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )


class User(BaseModel):
    user_id: str


@app.on_event("startup")
def load_matrix():
    global matrix
    matrix = pd.read_parquet("./predictions_matrix.parquet.gzip")
    return matrix


@app.get("/api/v1/recommend")
def recommend_book(user: User, api_key: APIKey = Depends(get_api_key)):
    registros = matrix[matrix["User-ID"] == user.user_id]
    registros = registros.sort_values("est", ascending=False).head()
    books_rec = registros["Book-Title"].tolist()
    return {"Recommended books": books_rec}


@app.get("/")
def home():
    return{"Desc": "Health Check"}


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)
