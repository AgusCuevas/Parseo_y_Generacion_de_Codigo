## GIC

ΣT = ```{ INICIO, FIN, anotar, numero, nota, alumno, bool, lista, vacia, mostrar, 
  evaluar, si, pasa, no, y, o, mientras, hacer, retornar, finFuncion, 
  procedimiento, finProcedimiento, funcion, aprobado, desaprobado, 
  agregar, quitar, en, limpiar, entre, a, =, , ,==, !=, <, >, <=, >=, +, -, *, /, 
  (, ), [, ], ", //, /*, */, :, cualquier_caracter_excepto_salto, cualquier_caracter }```

ΣN = ```{ <programa>, <sentencias>, <sentencia>, <asignacion>, <tipo>, <tipo_base>, 
  <impresion>, <expresion_texto>, <valor_texto>, <condicional>, <bloque_condicional>, 
  <condicion>, <iteracion>, <valor>, <termino>, <factor>, <op_suma>, <op_mul>, 
  <acceso_lista>, <operacion_lista>, <definicion_funcion>, <definicion_procedimiento>, 
  <llamada_funcion>, <llamada_procedimiento>, <parametros_opt>, <lista_parametros>, 
  <parametro>, <argumentos_opt>, <lista_argumentos>, <booleano>, 
  <operador_relacional>, <operador_logico>, <numero>, <texto>, <contenido_texto>, 
  <identificador>, <resto_identificador>, <letra>, <digito>, 
  <comentario_linea>, <comentario_linea_contenido>, 
  <comentario_bloque>, <comentario_bloque_contenido> }```

P =
```
<programa> -> INICIO <sentencias> FIN

<sentencias> -> <sentencia> <sentencias> | λ

<sentencia> -> <asignacion> | <impresion> | <condicional> | <iteracion> 
             | <definicion_funcion> | <definicion_procedimiento> 
             | <llamada_procedimiento> | <operacion_lista>

<asignacion> -> anotar <tipo> <identificador> = <valor>
              | anotar <identificador> = <valor>
              | anotar lista <tipo_base> <identificador> = vacia
              | anotar <identificador> [ <valor> ] = <valor>

<tipo> -> numero
          | nota
          | alumno
          | bool
          | lista <tipo_base>

<tipo_base> -> numero | nota | alumno | bool

<impresion> -> mostrar <expresion_texto>

<expresion_texto> -> <valor_texto> | <valor_texto> + <expresion_texto>

<valor_texto> -> <texto>
                | <identificador>
                | <booleano>
                | <numero>
                | <acceso_lista>
                | <llamada_funcion>

<condicional> -> evaluar <condicion> <bloque_condicional>

<bloque_condicional> -> si pasa: <sentencias> 
                      | si pasa: <sentencias> si no pasa: <sentencias>

<condicion> -> no <condicion>
             | <identificador> entre <valor> y <valor>
             | <valor> <operador_relacional> <valor>
             | <condicion> <operador_logico> <condicion>
             | <booleano>
             | <identificador>

<iteracion> -> mientras <condicion> hacer <sentencias>

<valor> ->  <termino> <op_suma> <valor> | <termino>

<termino> ->  <factor> <op_mul> <termino> | <factor>

<factor> -> <numero>
            | <texto>
            | <identificador>
            | <booleano>
            | <acceso_lista>
            | <llamada_funcion>
            | ( <valor> )

<op_suma> -> + | -

<op_mul> -> * | /

<acceso_lista> -> <identificador> [ <valor> ]

<operacion_lista> -> agregar <valor> a <identificador>
                   | quitar en <identificador> [ <valor> ]
                   | limpiar <identificador>

<definicion_funcion> -> funcion <tipo> <identificador> ( <parametros_opt> ) 
                        <sentencias> retornar <valor> finFuncion

<definicion_procedimiento> -> procedimiento <identificador> ( <parametros_opt> ) 
                              <sentencias> finProcedimiento

<llamada_funcion> -> <identificador> ( <argumentos_opt> )

<llamada_procedimiento> -> <identificador> ( <argumentos_opt> )

<parametros_opt> -> <lista_parametros> | λ

<lista_parametros> -> <parametro> | <parametro> , <lista_parametros>

<parametro> -> <tipo> <identificador>

<argumentos_opt> -> <lista_argumentos> | λ

<lista_argumentos> -> <valor> | <valor> , <lista_argumentos>

<booleano> -> aprobado | desaprobado

<operador_relacional> -> == | != | < | > | <= | >=

<operador_logico> -> y | o

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
