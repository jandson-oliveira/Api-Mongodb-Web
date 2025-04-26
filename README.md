# 📚 Projeto API Flask + MongoDB + Frontend

Este projeto é um ambiente completo com:

- Backend em Flask
- MongoDB para persistência de dados
- Frontend HTML simples
- Toda a infraestrutura orquestrada com **Docker Compose**

---

# 🚀 Como subir o projeto
surgiu a necessidade de garantir que o banco de dados MongoDB fosse populado automaticamente
com dados iniciais (como a criação de usuários) toda vez que o ambiente fosse criado do zero.


1. Clone o repositório:
```bash
git clone git@github.com:jandson-oliveira/Api-Mongodb-Web.git
cd /Api-Mongodb-Web
```

2. Suba os containers:

```bash
docker compose up -d
```

3. Deu problema nos containers:

```bash
docker compose down
```

4. Acesse:

- API Flask: `http://localhost:5000`
- Frontend: `http://localhost:8080/login.html`

---

# 📦 Observação importante sobre o MongoDB

Durante o desenvolvimento, foi necessário garantir que o MongoDB criasse **usuários e senhas** automaticamente já na subida do container.

Para isso, criamos um script chamado `mongo-init.js`, que é executado automaticamente na inicialização do MongoDB.  
Essa etapa é **obrigatória** para que a API Flask consiga autenticar corretamente com o banco.

Encontrar uma solução confiável para isso na internet foi **desafiador**, então este projeto já entrega essa funcionalidade pronta, evitando configurações manuais posteriores.

Sem o `mongo-init.js`, o container subiria sem usuários, o que impediria a comunicação segura entre a API e o banco.

---

# 🛠️ Tecnologias Utilizadas

- Python 3
- Flask
- MongoDB
- Docker
- Docker Compose

---

# 🌟 Sobre futuras melhorias

Este projeto foi estruturado para rodar tudo em uma única VM, mas como ainda estou trabalhado nele, o próximo passo se resume a 2 etapas.

Etapa 1:

O frontend poderá ser separado e servido por um Nginx dedicado, em outra VM ou container, otimizando ainda mais a arquitetura.

Etapa 2:

/login para autenticar e receber o token JWT

Guardar o token no localStorage

Usar o token para acessar /upload, /files etc.

