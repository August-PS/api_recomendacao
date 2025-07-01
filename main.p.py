
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.impute import SimpleImputer

# Carregar dados
df = pd.read_csv("base_recomendacao.csv")
user_item_matrix = df.pivot_table(index='user_id', columns='product_id', values='rating')
imputer = SimpleImputer(strategy='mean')
user_item_matrix_filled = imputer.fit_transform(user_item_matrix)
user_similarity = cosine_similarity(user_item_matrix_filled)
user_similarity_df = pd.DataFrame(user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)

# Função de recomendação
def recommend_products(user_id, user_item_matrix, similarity_matrix, top_n=3):
    user_idx = user_item_matrix.index.get_loc(user_id)
    similar_users = similarity_matrix[user_idx]
    scores = np.dot(similar_users, user_item_matrix_filled)
    user_rated = user_item_matrix.loc[user_id].dropna().index
    recommendations = pd.Series(scores, index=user_item_matrix.columns).drop(user_rated, errors="ignore")
    top_recommendations = recommendations.sort_values(ascending=False).head(top_n)
    return top_recommendations.index.tolist()

# Criar a API
app = FastAPI()

class RecommenderRequest(BaseModel):
    user_id: int
    top_n: int = 3

@app.post("/recomendar")
def recomendar(request: RecommenderRequest):
    recs = recommend_products(request.user_id, user_item_matrix, user_similarity_df.values, request.top_n)
    return {"recomendados": recs}
