# Añadir cambios al área de preparación. Podemos añadir un archivo en particular o colocar un “.” Para añadir todos
git add <archivo>

# Hacer commit a los cambios
git commit -m "Mensaje del commit"

# Agregar un repositorio remoto
git remote add origin <url_del_repositorio>

# Subir los cambios al repositorio remoto si esta ya enlazado con la rama y con el repositorio remoto.
git push

# Si no esta enlazado, podemos hacerlo de la siguiente forma.
git push origin nombre_rama

# Ver el historial de commits
git log

# Ver el árbol de commits con otras ramas
git log --all --decorate --oneline --graph

# Crear una nueva rama
git branch <nombre_de_la_rama>

# Cambiar a otra rama
git checkout <nombre_de_la_rama>

# Fusionar una rama con la rama actual
git merge <nombre_de_la_rama>
