## Requisitos
- Ter o docker instalado
- Ter o docker-compose instalado

## Instalação
Entre na pasta do projeto e digite:
```cmd
docker-compose up --build
```
Quando os 2 containers (web e db) ja estiverem rodando, você deve entrar no container web:
```
docker container exec -it tcc-backend-web-1 /bin/sh
```

Você saberá que entrou no container quando aparecer um `#` no seu terminal

Quando entrar, digite os seguintes comandos:
```cmd
cd ..
cd alembic
alembic upgrade head
```

Se tudo correr bem, é só vc digitar o seguinte endereço no seu navegador:
```cmd
http://localhost:8000/docs
```

Deverá aparecer uma tela semelhante a essa
![image](https://user-images.githubusercontent.com/23513359/190537919-65362d4c-8cf0-47fb-8b16-02188d34cacf.png)

Pronto, a aplicação já está funcionando.
