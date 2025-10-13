## GIC

ΣT = ```{ INICIO, FIN, anotar, numero, nota, alumno, bool, lista, vacia, mostrar, 
  evaluar, si, pasa, no, y, o, mientras, hacer, retornar, finFuncion, 
  procedimiento, finProcedimiento, funcion, aprobado, desaprobado, 
  agregar, quitar, en, limpiar, ==, !=, <, >, <=, >=, +, -, *, /, 
  (, ), [, ], ", ,, :, entre, y, a, 
  cualquier_caracter_excepto_salto, cualquier_caracter }```

ΣN = ```{ <programa>, <bloque>, <sentencia>, <asignacion>, <tipo>, <tipo_base>, 
  <impresion>, <texto_concatenado>, <mas_texto>, <elemento_texto>, 
  <condicional>, <bloque_condicional>, <opcional_sino>, <condicion>, 
  <condicion_o>, <mas_o>, <condicion_y>, <mas_y>, <condicion_no>, 
  <comparacion>, <cola_comparacion>, <repeticion>, <expresion>, 
  <suma_opcional>, <termino>, <producto_opcional>, <factor>, 
  <uso_variable>, <op_suma>, <op_mul>, <operacion_lista>, 
  <definicion_funcion>, <definicion_procedimiento>, <llamada_funcion>, 
  <llamada_procedimiento>, <parametros>, <lista_parametros>, 
  <parametros_extra>, <parametro>, <argumentos>, <lista_argumentos>, 
  <argumentos_extra>, <booleano>, <operador_relacional>, 
  <numero>, <texto>, <contenido_texto>, <identificador>, 
  <resto_identificador>, <letra>, <digito>, <comentario_linea>, 
  <comentario_linea_contenido>, <comentario_bloque>, 
  <comentario_bloque_contenido> }```

P =
```
<programa> -> INICIO <bloque> FIN

<bloque> -> <sentencia> <bloque> | λ

<sentencia> -> <asignacion>
             | <impresion>
             | <condicional>
             | <repeticion>
             | <definicion_funcion>
             | <definicion_procedimiento>
             | <llamada_procedimiento>
             | <operacion_lista>

# -----------------------------
# Asignaciones y tipos
# -----------------------------
<asignacion> -> anotar <tipo> <identificador> = <expresion>
              | anotar <identificador> = <expresion>
              | anotar lista<tipo_base> <identificador> = vacia
              | anotar <identificador> [ <expresion> ] = <expresion>

<tipo> -> numero | nota | alumno | bool | lista<tipo_base>
<tipo_base> -> numero | nota | alumno | bool

# -----------------------------
# Impresión (concatenación de texto)
# -----------------------------
<impresion> -> mostrar <texto_concatenado>

<texto_concatenado> -> <elemento_texto> <mas_texto>
<mas_texto> -> + <elemento_texto> <mas_texto> | λ

<elemento_texto> -> <texto>
                  | <numero>
                  | <booleano>
                  | <identificador> <uso_variable>
                  | ( <expresion> )

# -----------------------------
# Condicional con precedencia (no > y > o) y 'entre'
# -----------------------------
<condicional> -> evaluar <condicion> <bloque_condicional>

<bloque_condicional> -> si pasa: <bloque> <opcional_sino>
<opcional_sino> -> si no pasa: <bloque> | λ

<condicion> -> <condicion_o>

<condicion_o> -> <condicion_y> <mas_o>
<mas_o> -> o <condicion_y> <mas_o> | λ

<condicion_y> -> <condicion_no> <mas_y>
<mas_y> -> y <condicion_no> <mas_y> | λ

<condicion_no> -> no <condicion_no> | <comparacion>

<comparacion> -> <expresion> <cola_comparacion>
<cola_comparacion> -> <operador_relacional> <expresion>
                    | entre <expresion> y <expresion>
                    | λ

# -----------------------------
# Repetición (bucle mientras)
# -----------------------------
<repeticion> -> mientras <condicion> hacer <bloque>

# -----------------------------
# Expresiones aritméticas (sin recursión izquierda)
# -----------------------------
<expresion> -> <termino> <suma_opcional>
<suma_opcional> -> <op_suma> <termino> <suma_opcional> | λ

<termino> -> <factor> <producto_opcional>
<producto_opcional> -> <op_mul> <factor> <producto_opcional> | λ

<factor> -> <numero>
          | <texto>
          | <booleano>
          | ( <expresion> )
          | <identificador> <uso_variable>

<uso_variable> -> ( <argumentos> )
                | [ <expresion> ]
                | λ

<op_suma> -> + | -
<op_mul> -> * | /

# -----------------------------
# Listas
# -----------------------------
<operacion_lista> -> agregar <expresion> a <identificador>
                   | quitar en <identificador> [ <expresion> ]
                   | limpiar <identificador>

# -----------------------------
# Funciones y procedimientos
# -----------------------------
<definicion_funcion> -> funcion <tipo> <identificador> ( <parametros> )
                       <bloque>
                       retornar <expresion>
                       finFuncion

<definicion_procedimiento> -> procedimiento <identificador> ( <parametros> )
                             <bloque>
                             finProcedimiento

<llamada_funcion> -> <identificador> ( <argumentos> )
<llamada_procedimiento> -> <identificador> ( <argumentos> )

<parametros> -> <lista_parametros> | λ
<lista_parametros> -> <parametro> <parametros_extra>
<parametros_extra> -> , <parametro> <parametros_extra> | λ
<parametro> -> <tipo> <identificador>

<argumentos> -> <lista_argumentos> | λ
<lista_argumentos> -> <expresion> <argumentos_extra>
<argumentos_extra> -> , <expresion> <argumentos_extra> | λ

# -----------------------------
# Léxico y operadores
# -----------------------------
<booleano> -> aprobado | desaprobado
<operador_relacional> -> == | != | < | > | <= | >=

<numero> -> <digito> | <digito> <numero>
<texto> -> " <contenido_texto> "
<contenido_texto> -> <letra> <contenido_texto> | <digito> <contenido_texto> | λ

<identificador> -> <letra> <resto_identificador>
<resto_identificador> -> <letra> <resto_identificador>
                       | <digito> <resto_identificador>
                       | _ <resto_identificador>
                       | λ

<letra> -> a | b | ... | z | A | B | ... | Z
<digito> -> 0 | 1 | ... | 9

<comentario_linea> -> // <comentario_linea_contenido>
<comentario_linea_contenido> -> cualquier_caracter_excepto_salto <comentario_linea_contenido> | λ

<comentario_bloque> -> /* <comentario_bloque_contenido> */
<comentario_bloque_contenido> -> cualquier_caracter <comentario_bloque_contenido> | λ
```

S= ```<programa>```

------------------------------------------------
ACTUALIZAR
------------------------------------------------

## Programa ejemplo

INICIO

anotar nota x = (2 + 3) * 2

FIN

## Análisis Sintáctico Descendente (ASD) - Derivación por la izquierda

Programa

⇒ INICIO **[Sentencias]** FIN

⇒ INICIO **[Sentencia]** Sentencias FIN

⇒ INICIO **[Asignacion]** Sentencias FIN

⇒ INICIO **[anotar Tipo Identificador = Valor]** Sentencias FIN

⇒ INICIO anotar **[Tipo]** Identificador = Valor Sentencias FIN

⇒ INICIO anotar **[nota]** Identificador = Valor Sentencias FIN

⇒ INICIO anotar nota **[Identificador]** = Valor Sentencias FIN

⇒ INICIO anotar nota **[x]** = Valor Sentencias FIN

⇒ INICIO anotar nota x = **[Valor]** Sentencias FIN

⇒ INICIO anotar nota x = **[Termino]** Sentencias FIN

⇒ INICIO anotar nota x = **[Factor OpMul Termino]** Sentencias FIN

⇒ INICIO anotar nota x = **[( Valor )]** OpMul Termino Sentencias FIN

⇒ INICIO anotar nota x = ( **[Valor]** ) OpMul Termino Sentencias FIN

⇒ INICIO anotar nota x = ( **[Termino OpSuma Valor]** ) OpMul Termino Sentencias FIN

⇒ INICIO anotar nota x = ( **[Termino] OpSuma Valor** ) OpMul Termino Sentencias FIN

⇒ INICIO anotar nota x = ( **[Factor] OpSuma Valor** ) OpMul Termino Sentencias FIN

⇒ INICIO anotar nota x = ( **[Numero] OpSuma Valor** ) OpMul Termino Sentencias FIN

⇒ INICIO anotar nota x = ( **[2] OpSuma Valor** ) OpMul Termino Sentencias FIN

⇒ INICIO anotar nota x = ( 2 **[OpSuma]** Valor ) OpMul Termino Sentencias FIN

⇒ INICIO anotar nota x = ( 2 **[+]** Valor ) OpMul Termino Sentencias FIN

⇒ INICIO anotar nota x = ( 2 + **[Valor]** ) OpMul Termino Sentencias FIN

⇒ INICIO anotar nota x = ( 2 + **[Termino]** ) OpMul Termino Sentencias FIN

⇒ INICIO anotar nota x = ( 2 + **[Factor]** ) OpMul Termino Sentencias FIN

⇒ INICIO anotar nota x = ( 2 + **[Numero]** ) OpMul Termino Sentencias FIN

⇒ INICIO anotar nota x = ( 2 + **[3]** ) OpMul Termino Sentencias FIN

⇒ INICIO anotar nota x = ( 2 + 3 ) **[OpMul]** Termino Sentencias FIN

⇒ INICIO anotar nota x = ( 2 + 3 ) **[*]** Termino Sentencias FIN

⇒ INICIO anotar nota x = ( 2 + 3 ) * **[Termino]** Sentencias FIN

⇒ INICIO anotar nota x = ( 2 + 3 ) * **[Factor]** Sentencias FIN

⇒ INICIO anotar nota x = ( 2 + 3 ) * **[Numero]** Sentencias FIN

⇒ INICIO anotar nota x = ( 2 + 3 ) * **[2]** Sentencias FIN

⇒ INICIO anotar nota x = ( 2 + 3 ) * 2 **[Sentencias]** FIN

⇒ INICIO anotar nota x = ( 2 + 3 ) * 2 **[λ]** FIN

## Análisis Sintáctico Ascendente (ASA) - Derivación por la derecha

Programa

⇒ INICIO **[Sentencias]** FIN

⇒ INICIO Sentencia **[Sentencias]** FIN

⇒ INICIO Sentencia **[λ]** FIN

⇒ INICIO **[Sentencia]** FIN

⇒ INICIO **[Asignacion]** FIN

⇒ INICIO **[anotar Tipo Identificador = Valor]** FIN

⇒ INICIO anotar Tipo Identificador = **[Valor]** FIN

⇒ INICIO anotar Tipo Identificador = **[Termino]** FIN

⇒ INICIO anotar Tipo Identificador = **[Factor OpMul Termino]** FIN

⇒ INICIO anotar Tipo Identificador = Factor OpMul **[Termino]** FIN

⇒ INICIO anotar Tipo Identificador = Factor OpMul **[Factor]** FIN

⇒ INICIO anotar Tipo Identificador = Factor OpMul **[Numero]** FIN

⇒ INICIO anotar Tipo Identificador = Factor OpMul **[2]** FIN

⇒ INICIO anotar Tipo Identificador = Factor **[OpMul]** 2 FIN

⇒ INICIO anotar Tipo Identificador = Factor **[*]** 2 FIN

⇒ INICIO anotar Tipo Identificador = **[Factor]** * 2 FIN

⇒ INICIO anotar Tipo Identificador = **[( Valor )]** * 2 FIN

⇒ INICIO anotar Tipo Identificador = ( **[Valor]** ) * 2 FIN

⇒ INICIO anotar Tipo Identificador = ( **[Termino OpSuma Valor]** ) * 2 FIN

⇒ INICIO anotar Tipo Identificador = ( Termino OpSuma **[Valor]** ) * 2 FIN

⇒ INICIO anotar Tipo Identificador = ( Termino OpSuma **[Termino]** ) * 2 FIN

⇒ INICIO anotar Tipo Identificador = ( Termino OpSuma **[Factor]** ) * 2 FIN

⇒ INICIO anotar Tipo Identificador = ( Termino OpSuma **[Numero]** ) * 2 FIN

⇒ INICIO anotar Tipo Identificador = ( Termino OpSuma **[3]** ) * 2 FIN

⇒ INICIO anotar Tipo Identificador = ( Termino **[OpSuma]** 3 ) * 2 FIN

⇒ INICIO anotar Tipo Identificador = ( Termino **[+]** 3 ) * 2 FIN

⇒ INICIO anotar Tipo Identificador = ( **[Termino]** + 3 ) * 2 FIN

⇒ INICIO anotar Tipo Identificador = ( **[Factor]** + 3 ) * 2 FIN

⇒ INICIO anotar Tipo Identificador = ( **[Numero]** + 3 ) * 2 FIN

⇒ INICIO anotar Tipo Identificador = ( **[2]** + 3 ) * 2 FIN

⇒ INICIO anotar Tipo **[Identificador]** = ( 2 + 3 ) * 2 FIN

⇒ INICIO anotar Tipo **[x]** = ( 2 + 3 ) * 2 FIN

⇒ INICIO anotar **[Tipo]** x = ( 2 + 3 ) * 2 FIN

⇒ INICIO anotar **[nota]** x = ( 2 + 3 ) * 2 FIN

⇒ INICIO anotar nota x = ( 2 + 3 ) * 2 FIN

### Orden Inverso a la derivación por derecha

INICIO anotar nota x = ( 2 + 3 ) * 2 FIN

⇒ INICIO anotar **[nota]** x = ( 2 + 3 ) * 2 FIN

⇒ INICIO anotar **[Tipo]** x = ( 2 + 3 ) * 2 FIN

⇒ INICIO anotar Tipo **[x]** = ( 2 + 3 ) * 2 FIN

⇒ INICIO anotar Tipo **[Identificador]** = ( 2 + 3 ) * 2 FIN

⇒ INICIO anotar Tipo Identificador = ( **[2]** + 3 ) * 2 FIN

⇒ INICIO anotar Tipo Identificador = ( **[Numero]** + 3 ) * 2 FIN

⇒ INICIO anotar Tipo Identificador = ( **[Factor]** + 3 ) * 2 FIN

⇒ INICIO anotar Tipo Identificador = ( **[Termino]** + 3 ) * 2 FIN

⇒ INICIO anotar Tipo Identificador = ( Termino **[+]** 3 ) * 2 FIN

⇒ INICIO anotar Tipo Identificador = ( Termino **[OpSuma]** 3 ) * 2 FIN

⇒ INICIO anotar Tipo Identificador = ( Termino OpSuma **[3]** ) * 2 FIN

⇒ INICIO anotar Tipo Identificador = ( Termino OpSuma **[Numero]** ) * 2 FIN

⇒ INICIO anotar Tipo Identificador = ( Termino OpSuma **[Factor]** ) * 2 FIN

⇒ INICIO anotar Tipo Identificador = ( Termino OpSuma **[Termino]** ) * 2 FIN

⇒ INICIO anotar Tipo Identificador = ( **[Termino OpSuma Valor]** ) * 2 FIN

⇒ INICIO anotar Tipo Identificador = ( **[Valor]** ) * 2 FIN

⇒ INICIO anotar Tipo Identificador = **[( Valor )]** * 2 FIN

⇒ INICIO anotar Tipo Identificador = **[Factor]** * 2 FIN

⇒ INICIO anotar Tipo Identificador = Factor **[*]** 2 FIN

⇒ INICIO anotar Tipo Identificador = Factor **[OpMul]** 2 FIN

⇒ INICIO anotar Tipo Identificador = Factor OpMul **[2]** FIN

⇒ INICIO anotar Tipo Identificador = Factor OpMul **[Numero]** FIN

⇒ INICIO anotar Tipo Identificador = Factor OpMul **[Factor]** FIN

⇒ INICIO anotar Tipo Identificador = Factor OpMul **[Termino]** FIN

⇒ INICIO anotar Tipo Identificador = **[Factor OpMul Termino]** FIN

⇒ INICIO anotar Tipo Identificador = **[Termino]** FIN

⇒ INICIO anotar Tipo Identificador = **[Valor]** FIN

⇒ INICIO anotar **[anotar Tipo Identificador = Valor]** FIN

⇒ INICIO **[Asignacion]** FIN

⇒ INICIO **[Sentencia]** FIN

⇒ INICIO Sentencia **[λ]** FIN

⇒ INICIO Sentencia **[Sentencias]** FIN

⇒ INICIO **[Sentencias]** FIN

Programa
