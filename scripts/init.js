db = db.getSiblingDB("some_db_name");

// Evita erro se o usuário já existir
try {
    db.createUser({
        user: "some_username",
        pwd: "some_password",
        roles: [ { role: "readWrite", db: "some_db_name" } ]
    });
    print("Usuário criado com sucesso.");
} catch (e) {
    print("Usuário já existe ou erro ao criar:", e.message);
}

// Verifica e cria coleção
const collections = db.getCollectionNames();
if (!collections.includes("store")) {
    db.createCollection("store");
    db.store.createIndex({ name: 1 });
    print("Coleção 'store' criada.");
} else {
    print("Coleção 'store' já existe.");
}
