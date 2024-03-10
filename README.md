# M.I.D.A.S
Sistema que auxiliará os produtores e investidores do setor de agronegócios na identificação de tendências de preços com antecedência, a fim de gerar vantagens significativas, minimizar riscos e maximizar lucros.

# Backend

## Como iniciar o backend

- Vá para a pasta `backend/`

- Execute o seguinte comando: 

```console
  python3 manage.py runserver ou python manage.py runserver
```

## Para criar migrations de alteração na estrutura do banco

- Crie uma classe dentro de `backend/app_midas/models`

- Apague o arquivo `db.sqlite3`

- Execute os seguintes comandos:

 ```console
  python3 manage.py makemigrations
```
```console
  python3 manage.py migrate 
```