# API de Recomendação de Produtos

Este projeto implementa um sistema de recomendação de produtos baseado em similaridade entre usuários, usando Python, FastAPI e machine learning.

## Como rodar

1.baixe todos os arquivos do projeto:
```bash
git clone https://github.com/August-PS/api_recomendacao.git
cd api_recomendacao
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Rode a API:
```bash
uvicorn app:app --reload
```

4. Acesse a documentação da API:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Exemplo de requisição

POST `/recomendar`

```json
{
  "user_id": 1,
  "top_n": 3
}
```
