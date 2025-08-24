# Lenguaje a crear
## Objetivo
Ser un lenguaje de programación en español que permita expresar y automatizar tareas escolares (registrar notas, listar alumnos, generar reportes) de forma clara y accesible, con reglas simples y cercanas al ámbito educativo 

## Alcance
### Incluye:

-  Tipos: numero, nota (1..10), alumno (texto), bool (aprobado|desaprobado), lista<tipo_base>.

-  Sentencias: asignación, impresión, condicional (evaluar), iteración (mientras), funciones, procedimientos, operaciones de lista (agregar, quitar en, limpiar).

## Especificaciones léxicas
- Sensibilidad a mayúsculas/minúsculas: sí.

- Comentarios: ```// …``` (línea), ```/* … */``` (bloque).

- Léxicos básicos: números enteros no negativos; textos entre comillas "…".

- Operadores y signos: ```+ - * / == != < > <= >= ( ) [ ] , ``` y lógicos ```y```, ```o```, ```no```.

- Palabras clave principales: ```INICIO```, ```FIN.```, ```anotar```, ```mostrar```, ```evaluar```, ```si pasa:```, ```si no pasa:```, ```mientras```, ```hacer```, ```funcion```, ```retornar```, ```finFuncion```, ```procedimiento```, ```finProcedimiento```, ```agregar```, ```quitar```, ```en```, ```limpiar```, ```entre```, ```vacia```, ```aprobado```, ```desaprobado```.
 
## Especificaciones sintácticas
-  Programa: INICIO <sentencias> FIN.

-  Asignación:

  -  Declaración: ```anotar <tipo> <id> = <valor>```

  -  Modificación: ```anotar <id> = <valor>```

  -  Listas: ```anotar lista<tipo_base> L = vacia```; acceso ```L[i]```; escritura ```anotar L[i] = v```

- Impresión: mostrar <expresion_texto> (concatenación con +).

-  Condicional:
```
evaluar <condicion>
    si pasa: <sentencias>
    si no pasa: <sentencias>   // opcional
```
-  Iteración: ```mientras <condicion> hacer <sentencias>```.

-  Funciones: Se debe definir que tipo de dato devolvera la funcion al momento de crearla.

-  Expresiones: precedencia * / > + -; paréntesis para agrupar.

-  Indexación de listas: 1-based (primer elemento es índice 1).
 
## Especificaciones semánticas
-  **Tipos:** verificación estática; se declara al momento de crear la variable

-  **nota:** entero en [1..10]; asignar fuera de rango es error.

-  **Listas:** tipo base estricto; se declara al momento de crear la lista, se puede inicializar vacia
  
-  **mostrar:** acepta una expresión de texto que puede concatenar varias partes con + (variables, números, booleanos, accesos a lista, llamadas a función).

-  **Ámbitos:** variables de funciones/procedimientos son locales.
