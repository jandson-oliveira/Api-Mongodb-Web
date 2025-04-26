# Usar uma imagem Nginx oficial
FROM nginx:alpine

# Copiar os arquivos estáticos (HTML, JS, CSS, etc.) para o diretório de dados do Nginx
COPY ./frontend /usr/share/nginx/html

# Expor a porta 80, onde o Nginx estará servindo os arquivos
EXPOSE 80

# Comando para iniciar o Nginx
CMD ["nginx", "-g", "daemon off;"]
