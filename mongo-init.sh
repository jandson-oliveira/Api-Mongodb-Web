// Script específico para Bitnami - configurações adicionais
db = db.getSiblingDB('database-TuxOps');

// Criar roles personalizados se necessário
db.createRole({
  role: "customRole",
  privileges: [
    { resource: { db: "database-TuxOps", collection: "" }, actions: ["find", "insert", "update"] }
  ],
  roles: []
});

// Atribuir roles ao usuário (já criado pelas variáveis de ambiente)
db.grantRolesToUser("api_user", [
  { role: "readWrite", db: "database-TuxOps" },
  { role: "dbAdmin", db: "database-TuxOps" },
  { role: "customRole", db: "database-TuxOps" }
]);

// Criar coleções iniciais
db.createCollection("usuario");