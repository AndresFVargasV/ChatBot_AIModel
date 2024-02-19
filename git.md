# Ejemplo de como escribir un archivo .md.

## Añadir cambios al área de preparación. Podemos añadir un archivo en particular o colocar un “.” Para añadir todos
 ```bash
 git add <archivo>
 ```

## Hacer commit a los cambios
```bash
git commit -m "Mensaje del commit"
```

## Agregar un repositorio remoto
```bash
git remote add origin <url_del_repositorio>
```

## Subir los cambios al repositorio remoto si esta ya enlazado con la rama y con el repositorio remoto.
```bash
    git push
  ```

## Si no esta enlazado, podemos hacerlo de la siguiente forma.
```bash
git push origin nombre_rama
```

## Ver el historial de commits.
```bash
git log
```

## Ver el árbol de commits con otras ramas
```bash
git log --all --decorate --oneline --graph
```

## Crear una nueva rama
```bash
git branch <nombre_de_la_rama>
```

## Cambiar a otra rama
```bash
git checkout <nombre_de_la_rama>
```

## Fusionar una rama con la rama actual
```bash
git merge <nombre_de_la_rama>
```
