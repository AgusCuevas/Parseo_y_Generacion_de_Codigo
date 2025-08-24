# Parseo_y_Generacion_de_Codigo

# Lenguaje Educativo

## Descripción del lenguaje

Es un lenguaje de programación educativa, con palabras clave que se relacionan a situaciones del entorno académico. Está diseñado para ser simple, legible y didáctico, permitiendo representar conceptos comunes como alumnos, notas, aprobaciones, etc

## Tipos de datos

- **numero** → valor numérico entero.

- **nota** → valor entre 1 y 10 (calificaciones).

- **alumno** → texto (cadenas como "Lucía").

- **bool** → aprobado / desaprobado.

- **lista<tipo_base>** → lista tipada cuyos elementos son **numero**, **nota**, **alumno** o **bool**.

  - No existen literales de lista; se crean vacías con **vacia** y se completan con operaciones.

  - El primer indice de la lista es 1.

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

### Impresión

**mostrar** acepta una expresión de texto que puede concatenar varias partes con + (variables, números, booleanos, accesos a lista, llamadas a función).
Ej.: ```mostrar "Alumno: " + nombre + " | Nota: " + nota```

### Condicional

```evaluar <condicion>``` ejecuta un bloque ```si pasa:``` y, opcionalmente, un bloque ```si no pasa:```.

Negación: ```no <condicion>```

Rango: ```<identificador>``` entre ```<a>``` y ```<b>``` (equivale a ```a <= x y x <= b```)

### Iteración (únicamente mientras)

```mientras <condicion> hacer``` repite mientras la condición sea verdadera.

## Operaciones de lista
- ```agregar <valor> a <lista>``` (Se agrega al final de lista)

- ```quitar en <lista>[<indice>]``` (Elimina por índice)

- ```limpiar <lista>``` (Deja la lista vacía)

## Funciones y procedimientos

- **Funciones:** devuelven un valor con **retornar**. Se aceptan parametros
```
funcion <tipo> <nombre>(parámetros)
    sentencias
    retornar <valor>
finFuncion
```

- **Procedimientos:** no devuelven valor; se invocan como sentencia. Se aceptan parametros
```
procedimiento <nombre>(parámetros)
    sentencias
finProcedimiento
```
## Comentarios

- De línea: ```// comentario```

- De bloque: ```/* comentario */```

## Operadores

- **Aritméticos:** +, -, *, / con precedencia: * / > + - (asociatividad izquierda).
Se admiten paréntesis para agrupar: ( … ).

- **Relacionales:** ==, !=, <, >, <=, >= (se permiten en ambos lados valores/expresiones).

- **Lógicos:** y, o, y prefijo no.

## Reglas semánticas

- nota debe estar en [1..10].

- Tipos de listas estrictos (solo tipo_base permitido).
- 
- Variables de función/procedimiento son locales.

- Todo valor se convierte a texto al imprimir/concatenar en mostrar.

## Ejemplo
```
INICIO

// Listas: alumnos y sus notas. Se inicializan vacias
anotar lista<alumno> alumnos = vacia
anotar lista<nota>   notas   = vacia

// Carga de listas con 'agregar'
agregar "Lucía"  a alumnos
agregar 8        a notas

agregar "Martín" a alumnos
agregar 5        a notas

agregar "Sofía"  a alumnos
agregar 10       a notas

//["Lucía", "Martín", "Sofía"]
//[8, 5, 10]

// Cantidad de registros 
anotar numero cantidad = 3

// Corrección por índice (0-based): Martín pasa a 6
anotar notas[1] = 6
//["Lucía", "Martín", "Sofía"]
//[8, 6, 10]

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

// Recorrido con 'mientras' para imprimir boletines
mostrar "Boletines:"
anotar numero i = 0
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
## Salida
```
Boletines:
Alumno: Lucía | Nota: 8 | Estado: aprobado
Alumno: Martín | Nota: 6 | Estado: aprobado
Alumno: Sofía | Nota: 10 | Estado: aprobado
Promedio del curso: 8
Quitando última entrada...
Limpiando listas...
```


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
# Clase 1
## Introduccion
```mermaid
graph LR
    %% =============== NODO CENTRAL ===============
    A((Traductor)):::nivel0

    %% =============== LADO IZQUIERDO ===============
    subgraph IZQUIERDA
    direction RL
        %% Definición
        B["Definición"]:::ramaDef --- A
        B1["Convierte un programa de un<br/>lenguaje (fuente) a otro (objeto)"]:::ramaDef --- B

        %% Historia
        H[Historia]:::ramaHist --- A
        %% Hoja 1 — 1951 · Grace Hopper · A-0 (UNIVAC)
        H1["1951: Grace Hopper — A-0, UNIVAC"]:::ramaHist --- H
        H1a["Desarrolla el primer compilador: <b>A-0</b>"]:::ramaHist --- H1
        H1b["Primera rutina “compilada” ejecutada con éxito"]:::ramaHist --- H1a


        %% Hoja 2 — 1954 · John Backus · FORTRAN (IBM 704)
        H2["1954: John Backus — FORTRAN (IBM 704)"]:::ramaHist --- H
        H2a["Comienza el desarrollo del compilador de <b>FORTRAN</b>"]:::ramaHist --- H2

        %% Diferencias
        F[Diferencias]:::ramaDif --- A
        F1["Intérprete → ejecuta el<br/>código fuente"]:::ramaDif --- F
        F2["Compilador → produce objeto/binario<br/>y luego se ejecuta"]:::ramaDif --- F

        %% Herramientas (dos columnas compactas)
        G["Herramientas de la cadena de compilación"]:::ramaHerr --- A

        %% Columna A (Construcción)
        G1["Editores / IDE (ASCII)"]:::ramaHerr --- G
        G1a["Utilizados para leer y escribir los programas, que el compilador traducirá a código máquina"]:::ramaHerr --- G1
        
        G2["Preprocesadores<br/>(macros, includes, comentarios)"]:::ramaHerr --- G
        G2a["Funcionan de forma independiente cuando compilador lo llama. Modifican el programa fuente antes de compilar"]:::ramaHerr --- G2

        G3["Enlazadores<br/>(objetos + libs → ejecutable)"]:::ramaHerr --- G
        G3a["Unen los diferentes módulos con sus respectivos códigos objeto para producir un archivo ejecutable"]:::ramaHerr --- G3
        
        G4["Cargadores<br/>(direcciones reales / reubicable)"]:::ramaHerr --- G
        G4a["Asignan las direcciones y el espacio de memoria necesario para la ejecución del programa"]:::ramaHerr --- G4
        
        G5["Depuradores<br/>(paso a paso; inspección de vars)"]:::ramaHerr --- G
        G5a["Permiten encontrar errores y solucionarlos en un programa, una vez que ha sido compilado"]:::ramaHerr --- G5
        
        G6["Desensambladores<br/>(máquina → ensamblador)"]:::ramaHerr --- G
        G6a["Traducen el lenguaje máquina a lenguaje ensamblador"]:::ramaHerr --- G6
        
        G7["Decompiladores<br/>(máquina → alto nivel)"]:::ramaHerr --- G
        G7a["Traducen de código máquina a un lenguaje de alto nivel"]:::ramaHerr --- G7

        G8["Transpilador"]:::ramaHerr --- G
        G8a["Leen código fuente escrito en un lenguaje de programación y producen el código equivalente en otro lenguaje"]:::ramaHerr --- G8
        
    end

    %% =============== LADO DERECHO ===============
    subgraph DERECHA
    direction LR
        %% Tipos de traductores
        A --- C[Tipos de Traductores]:::ramaTipos

        %% Ensamblador
        C --- E1[Ensamblador]:::ramaTipos
        E1 --- E1a["Traduce de ensamblador a código máquina"]:::ramaTipos
        E1 --- E1b["Correspondencia 1:1 (instr ↔ instr)"]:::ramaTipos
        E1 --- E1c["Ventajas: muy veloz, exacto"]:::ramaTipos
        E1 --- E1d["Desventajas: difícil de leer/escribir,<br/>dependiente de la máquina"]:::ramaTipos
        E1 --- E1e["Ejemplo: LD HL,#0100 → 65h 00h 01h"]:::ramaTipos

        %% Intérprete
        C --- E2[Intérprete]:::ramaTipos
        E2 --- E2a["Lee, traduce y ejecuta<br/>sentencia por sentencia"]:::ramaTipos
        E2 --- E2b["Permite agregar sentencias en ejecución"]:::ramaTipos
        E2 --- E2c["Ejemplos: Basic, Python, Smalltalk,<br/>Ruby, JavaScript"]:::ramaTipos
        E2 --- E2d["No genera binario final"]:::ramaTipos

        %% Compilador
        C --- E3[Compilador]:::ramaTipos
        E3 --- E3a["Analiza todo el programa y<br/>genera código de bajo nivel (objeto)"]:::ramaTipos
        E3 --- E3b["Luego se ejecuta el programa objeto"]:::ramaTipos
        E3 --- E3c["Más rápido que interpretado"]:::ramaTipos
        E3 --- E3d["Lenguajes: C, C++, Pascal,<br/>Fortran, COBOL, Go"]:::ramaTipos
    end

    %% ================= ESTILOS =================
    classDef nivel0 fill:#FFD700,stroke:#333,stroke-width:2px;

    classDef ramaDef  fill:#fff2b2,stroke:#FFB300,stroke-width:2px;
    classDef ramaHist fill:#f0d6ff,stroke:#800080,stroke-width:2px;
    classDef ramaDif  fill:#ffd6d6,stroke:#FF0000,stroke-width:2px;

    classDef ramaHerr fill:#e5ffd6,stroke:#28A745,stroke-width:2px;
    classDef ramaTipos fill:#d0e6ff,stroke:#007BFF,stroke-width:2px;

    %% Al final de cada subgraph:
    style IZQUIERDA fill:transparent,stroke:none
    style DERECHA fill:transparent,stroke:none
```
