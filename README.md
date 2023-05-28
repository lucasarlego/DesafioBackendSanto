# Santo Digital
### Desafio de Back-End

## Linguagem e Frameworks utilizada para realização do desafio:
* Python;
* FastAPI.

### Conclusão:

Foi a minha primeira vez construindo uma API. Pesquisei muito e achei muita informação, o que é legal. Porém tive muitas dificuldades...
De primeiro momento, foi bastante complicado conectar ao banco de dados MySQL, fiz varias tentativas com o SQLAlchemy e com o mysql.connector
e todas sem sucesso... Acredito que a conexão tenha sido feita, mas alguma coisa me impedia de pegar as informações existentes no banco então parei
mesmo no primeiro GET.

Depois de um tempo olhando pro céu, decidi fazer com que ela não tivesse acesso a um banco mas sim a uma lista diretamente pelo Python
e deu certo, consegui fazer o CRUD!

### Guia de diretórios:
* schemas -> classe products.

### Guia geral:
* Para testar a API:
```uvicorn app:app --reload```

# Obrigado!
