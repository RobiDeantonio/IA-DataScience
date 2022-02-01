SELECT titulo AS encabezado,fecha_publicacion AS publicado,estatus FROM posts;

# LEFT JOIN
#ELECT * FROM usuarios LEFT JOIN posts ON usuarios.id=posts.usuario_id;
SELECT * FROM usuarios LEFT JOIN posts ON usuarios.id=posts.usuario_id WHERE posts.usuario_id IS NULL;

# RIGHT JOIN
SELECT * FROM usuarios LEFT JOIN posts ON usuarios.id=posts.usuario_id;
SELECT * FROM usuarios RIGHT JOIN posts ON usuarios.id=posts.usuario_id WHERE posts.usuario_id IS NULL;

# INNER JOIN // INTERSECTION
SELECT * FROM usuarios INNER JOIN posts ON usuarios.id=posts.usuario_id;

# OUTER JOIN // UNION 

SELECT * FROM usuarios LEFT JOIN posts ON usuarios.id=posts.usuario_id
UNION
SELECT * FROM usuarios RIGHT JOIN posts ON usuarios.id=posts.usuario_id;



# OUTER JOIN // SIMETRIC DIFFERENCE	
SELECT * FROM usuarios LEFT JOIN posts ON usuarios.id=posts.usuario_id WHERE posts.usuario_id IS NULL
UNION
SELECT * FROM usuarios RIGHT JOIN posts ON usuarios.id=posts.usuario_id WHERE posts.usuario_id IS NULL;


#WHERE
SELECT * FROM posts WHERE estatus != 'activo';
SELECT * FROM posts WHERE titulo LIKE '%escandalo%';
SELECT * FROM posts WHERE fecha_publicacion BETWEEN '2021-01-01' AND '2025-12-31';
SELECT * FROM posts WHERE YEAR(fecha_publicacion) BETWEEN '2023' AND '2024';
SELECT * FROM posts WHERE usuario_id IS NOT NULL AND estatus='activo' AND id<50 AND categoria_id=2 AND YEAR(fecha_publicacion)='2025';

# GROUP BY
SELECT estatus, COUNT(*) AS post_aquantity FROM posts GROUP BY estatus;


















