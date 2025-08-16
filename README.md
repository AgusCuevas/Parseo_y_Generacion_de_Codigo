# Parseo_y_Generacion_de_Codigo

# Lenguaje Educativo

## Descripción del lenguaje

Propósito. Lenguaje de programación educativo con palabras clave del entorno escolar. Busca enseñar secuencia, decisión e iteración con una sintaxis clara y semántica cercana: alumnos, notas, estados de aprobación, listas de datos del curso, etc.

## Tipos de datos

- **numero** → valor numérico entero.

- **nota** → valor entre 1 y 10 (calificaciones).

- **alumno** → texto (cadenas como "Lucía").

- **bool** → aprobado / desaprobado.

- **lista<tipo_base>** → lista tipada cuyos elementos son **numero**, **nota**, **alumno** o **bool**.

  - No existen literales de lista; se crean vacías con vacia y se completan con operaciones.

  - Índices 0-based (el primer elemento es el índice 0).

## Estructura de programa

Un programa comienza con **INICIO** y termina con **FIN.**. Todas las sentencias válidas van entre esas dos palabras clave.

### Sentencias principales
### Asignación

- Declaración + asignación: ```anotar <tipo> <variable> = <valor>```

- Modificación: ```anotar <variable> = <nuevo_valor>```

- Listas:

  - Crear: ```anotar lista<tipo_base> <lista> = vacia```

  - Acceso: ```<lista>[<indice>]```

  - Asignación por índice: ```anotar <lista>[<indice>] = <valor>```

No se permite declarar sin valor inicial. No se puede re-declarar un identificador en el mismo ámbito.

### Impresión

**mostrar** acepta una expresión de texto que puede concatenar varias partes con + (variables, números, booleanos, accesos a lista, llamadas a función).
Ej.: ```mostrar "Alumno: " + nombre + " | Nota: " + nota```

### Condicional

```evaluar <condicion>``` ejecuta un bloque ```si pasa:``` y, opcionalmente, un bloque ```si no pasa:```.
Atajos legibles:

Negación: ```no <condicion>```

Rango: ```<identificador>``` entre ```<a>``` y ```<b>``` (equivale a ```a <= x y x <= b```, incluye los extremos)

### Iteración (únicamente mientras)

Mientras <condicion> hacer repite mientras la condición sea verdadera.

## Operaciones de lista
- ```agregar <valor> a <lista>``` (append al final)

- ```quitar en <lista>[<indice>]``` (elimina por índice)

- ```limpiar <lista>``` (deja la lista vacía)

Sugerencia de biblioteca: ```longitud(<lista>)``` → **numero** (si luego querés incorporarla como primitiva).

## Funciones y procedimientos

- **Funciones:** devuelven un valor con **retornar**, se usan en expresiones.
```
funcion <tipo> <nombre>(parámetros)
    sentencias
    retornar <valor>
finFuncion
```

- **Procedimientos:** no devuelven valor; se invocan como sentencia.
```
procedimiento <nombre>(parámetros)
    sentencias
finProcedimiento
```
## Comentarios

- De línea: ```// comentario```

- De bloque: ```/* comentario */```
Se pueden ubicar donde se permita espacio en blanco; son ignorados por el parser.

## Operadores y precedencia

- **Aritméticos:** +, -, *, / con precedencia: * / > + - (asociatividad izquierda).
Se admiten paréntesis para agrupar: ( … ).

- **Relacionales:** ==, !=, <, >, <=, >= (se permiten en ambos lados valores/expresiones).

- **Lógicos:** y, o, y prefijo no.

## Reglas semánticas clave

- nota debe estar en [1..10].

- Tipos de listas estrictos (solo tipo_base permitido).

- Índices válidos: enteros no negativos y dentro de rango.

- Variables de función/procedimiento son locales; sombrean a globales.

- Todo valor se convierte a texto al imprimir/concatenar en mostrar.

## BNF
```
<programa> ::= INICIO <sentencias> FIN.

<sentencias> ::= <sentencia> <sentencias> | λ

<sentencia> ::= <asignacion> | <impresion> | <condicional> | <iteracion>
              | <definicion_funcion>
              | <definicion_procedimiento>
              | <llamada_procedimiento>
              | <operacion_lista>

<asignacion> ::= anotar <tipo> <identificador> = <valor>
               | anotar <identificador> = <valor>
               | anotar lista<tipo_base> <identificador> = vacia
               | anotar <identificador> [ <valor> ] = <valor>

<tipo> ::= numero | nota | alumno | bool | lista<tipo_base>

<tipo_base> ::= numero | nota | alumno | bool

<impresion> ::= mostrar <expresion_texto>

<expresion_texto> ::= <valor_texto> | <valor_texto> + <expresion_texto>

<valor_texto> ::= <texto> | <identificador> | <booleano> | <numero>
                | <acceso_lista> | <llamada_funcion>

<condicional> ::= evaluar <condicion> <bloque_condicional>

<bloque_condicional> ::= si pasa: <sentencias>
                       | si pasa: <sentencias> si no pasa: <sentencias>

<condicion> ::= no <condicion>
              | <identificador> entre <valor> y <valor>
              | <valor> <operador_relacional> <valor>
              | <condicion> <operador_logico> <condicion>
              | <booleano> | <identificador>

<iteracion> ::= mientras <condicion> hacer <sentencias>

<valor>   ::= <valor> <op_suma> <termino> | <termino>
<termino> ::= <termino> <op_mul> <factor> | <factor>
<factor>  ::= <numero> | <texto> | <identificador> | <booleano>
            | <acceso_lista> | <llamada_funcion> | "(" <valor> ")"

<op_suma> ::= + | -
<op_mul>  ::= * | /

<acceso_lista> ::= <identificador> [ <valor> ]

<operacion_lista> ::= agregar <valor> a <identificador>
                    | quitar en <identificador> [ <valor> ]
                    | limpiar <identificador>

<definicion_funcion> ::= funcion <tipo> <identificador> ( <parametros_opt> )
                         <sentencias>
                         retornar <valor>
                         finFuncion

<definicion_procedimiento> ::= procedimiento <identificador> ( <parametros_opt> )
                               <sentencias>
                               finProcedimiento

<llamada_funcion> ::= <identificador> ( <argumentos_opt> )
<llamada_procedimiento> ::= <identificador> ( <argumentos_opt> )

<parametros_opt> ::= λ | <lista_parametros>
<lista_parametros> ::= <parametro> | <parametro> , <lista_parametros>
<parametro> ::= <tipo> <identificador>

<argumentos_opt> ::= λ | <lista_argumentos>
<lista_argumentos> ::= <valor> | <valor> , <lista_argumentos>

<booleano> ::= aprobado | desaprobado

<operador_relacional> ::= == | != | < | > | <= | >=
<operador_logico> ::= y | o

<numero> ::= <digito> { <digito> }
<texto> ::= '"' { <letra> | <digito> } '"'
<identificador> ::= <letra> { <letra> | <digito> | _ }

<letra> ::= a | b | ... | z | A | B | ... | Z
<digito> ::= 0 | 1 | ... | 9

<comentario_linea>  ::= "//" {cualquier_caracter_excepto_salto}
<comentario_bloque> ::= "/*" {cualquier_caracter} "*/"
```

## Ejemplo
```
INICIO

// Listas tipadas (sin literales): alumnos y sus notas
anotar lista<alumno> alumnos = vacia
anotar lista<nota>   notas   = vacia

// Carga con 'agregar'
agregar "Lucía"  a alumnos
agregar 8        a notas

agregar "Martín" a alumnos
agregar 5        a notas

agregar "Sofía"  a alumnos
agregar 10       a notas

// Cantidad de registros administrada por el programa
anotar numero cantidad = 3

// Corrección por índice (0-based): Martín pasa a 6
anotar notas[1] = 6

// Procedimiento: imprime un boletín simple
procedimiento mostrarBoletin(alumno nombre, nota n, bool estado)
    mostrar "Alumno: " + nombre + " | Nota: " + n + " | Estado: " + estado
finProcedimiento

// Función: estado según nota (bool)
funcion bool estadoSegunNota(nota n)
    evaluar n >= 6
        si pasa:
            retornar aprobado
        si no pasa:
            retornar desaprobado
finFuncion

// Función: promedio de n elementos de una lista de notas
funcion nota promedio(lista<nota> xs, numero n)
    anotar numero i = 0
    anotar nota   s = 0
    mientras i < n hacer
        anotar s = s + xs[i]
        anotar i = i + 1
    retornar s / n
finFuncion

// Validación con 'entre' y demostración de 'no'
mostrar "Validando notas ingresadas:"
anotar numero i = 0
mientras i < cantidad hacer
    evaluar notas[i] entre 1 y 10
        si pasa:
            mostrar "Nota " + i + " válida: " + notas[i]
    anotar i = i + 1

evaluar no (estadoSegunNota(notas[0]) == desaprobado)
    si pasa:
        mostrar "El primer alumno no está desaprobado"

// Recorrido con 'mientras' para imprimir boletines
mostrar "Boletines:"
anotar i = 0
mientras i < cantidad hacer
    anotar alumno nombre = alumnos[i]
    anotar nota n = notas[i]
    anotar bool est = estadoSegunNota(n)
    mostrarBoletin(nombre, n, est)
    anotar i = i + 1

// Promedio del curso
anotar nota prom = promedio(notas, cantidad)
mostrar "Promedio del curso: " + prom

// Operaciones de lista: quitar y limpiar
mostrar "Quitando última entrada..."
quitar en alumnos[2]
quitar en notas[2]
anotar cantidad = 2

mostrar "Limpiando listas..."
limpiar alumnos
limpiar notas

FIN.
```
