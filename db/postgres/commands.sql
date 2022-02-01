-- INNER JOIN  pasajeros que han tomado un viaje
SELECT * FROM pasajeros
JOIN viajes ON pasajeros.id=viajes.id_pasajero;

-- LEFT JOIN  pasajeros que NO han tomado un viaje
SELECT * FROM pasajeros
LEFT JOIN viajes ON pasajeros.id=viajes.id_pasajero
WHERE viajes.id_pasajero IS NULL;

-- LIKE AND ALIKE
SELECT nombre FROM pasajeros
WHERE nombre ILIKE '%O';

-- RETURNING
UPDATE public.pasajeros
	SET nombre=NULL
	WHERE id=1
	RETURNING *;

-- COALESCE
SELECT id, COALESCE(nombre, 'NO APLICA') as nombre, direccion, fecha_nacimiento
FROM public.pasajeros WHERE id = 1;

-- NULLIF  GREATEST  LEAST
SELECT NULLIF (0,0);
SELECT GREATEST (1,5,6,7,5,9);
SELECT LEAST (1,5,6,7,5,9);

-- BLOQUES ANONIMOS
SELECT *, 
CASE WHEN fecha_nacimiento > '2012-01-01' THEN 'niño'
ELSE 'mayor' END FROM public.pasajeros;

-- VISTAS  // GUARDA COMANDOS DE EJECUCION
SELECT *  FROM rango_view;

-- VISTAS MATERIALIZADAS // guarda comandos en memoria con datos hasta que se actualice
SELECT * FROM despues_2021_mview;
-- REFRESH MATERIALIZED VIEW despues_noche_mview;

-- PL / SQL
CREATE FUNCTION mypl() 
	RETURNS void
AS $$
DECLARE
 rec record;
 contador integer := 0;
BEGIN
 FOR rec IN SELECT * FROM Pasajeros LOOP
 	RAISE NOTICE  'Un pasajero se llama %', rec.nombre;
	contador := contador + 1;
 END LOOP;
 	RAISE NOTICE  'Conteo es %', contador;
END
$$
LANGUAGE PLPGSQL;

SELECT mypl();