## GIC
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

## Programa

INICIO

anotar numero x = (2 + 3) * 4 - 5

FIN

## Derivación por la izquierda
Programa

⇒ INICIO **Sentencias** FIN

⇒ INICIO **Sentencia** Sentencias FIN

⇒ INICIO **Asignacion** Sentencias FIN

⇒ INICIO **anotar Tipo Identificador = Valor** Sentencias FIN

⇒ INICIO anotar **Tipo** Identificador = Valor FIN

⇒ INICIO anotar **numero** Identificador = Valor FIN

⇒ INICIO anotar numero **Identificador** = Valor FIN

⇒ INICIO anotar numero **x** = Valor FIN

⇒ INICIO anotar numero x = **Valor** FIN

⇒ INICIO anotar numero x = **Termino OpSuma Valor** FIN

⇒ INICIO anotar numero x = **Factor OpMul Termino** OpSuma Valor FIN

⇒ INICIO anotar numero x = **( Valor )** OpMul Termino OpSuma Valor FIN

⇒ INICIO anotar numero x = ( **Termino OpSuma Valor** ) OpMul Termino OpSuma Valor FIN

⇒ INICIO anotar numero x = ( **Factor OpSuma Valor** ) OpMul Termino OpSuma Valor FIN

⇒ INICIO anotar numero x = ( **Numero OpSuma Valor** ) OpMul Termino OpSuma Valor FIN

⇒ INICIO anotar numero x = ( **2 OpSuma Valor** ) OpMul Termino OpSuma Valor FIN

⇒ INICIO anotar numero x = ( 2 **+ Valor** ) OpMul Termino OpSuma Valor FIN

⇒ INICIO anotar numero x = ( 2 + **Termino** ) OpMul Termino OpSuma Valor FIN

⇒ INICIO anotar numero x = ( 2 + **Factor** ) OpMul Termino OpSuma Valor FIN

⇒ INICIO anotar numero x = ( 2 + **Numero** ) OpMul Termino OpSuma Valor FIN

⇒ INICIO anotar numero x = ( 2 + **3** ) OpMul Termino OpSuma Valor FIN

⇒ INICIO anotar numero x = ( 2 + 3 ) **OpMul** Termino OpSuma Valor FIN

⇒ INICIO anotar numero x = ( 2 + 3 ) * **Termino** OpSuma Valor FIN

⇒ INICIO anotar numero x = ( 2 + 3 ) * **Factor** OpSuma Valor FIN

⇒ INICIO anotar numero x = ( 2 + 3 ) * **Numero** OpSuma Valor FIN

⇒ INICIO anotar numero x = ( 2 + 3 ) * **4** OpSuma Valor FIN

⇒ INICIO anotar numero x = ( 2 + 3 ) * 4 **OpSuma** Valor FIN

⇒ INICIO anotar numero x = ( 2 + 3 ) * 4 - **Valor** FIN

⇒ INICIO anotar numero x = ( 2 + 3 ) * 4 - **Termino** FIN

⇒ INICIO anotar numero x = ( 2 + 3 ) * 4 - **Factor** FIN

⇒ INICIO anotar numero x = ( 2 + 3 ) * 4 - **Numero** FIN

⇒ INICIO anotar numero x = ( 2 + 3 ) * 4 - **5** FIN

## Derivación por la derecha
Programa

⇒ INICIO **Sentencias** FIN

⇒ INICIO **Sentencia** Sentencias FIN

⇒ INICIO **Asignacion** Sentencias FIN

⇒ INICIO **anotar Tipo Identificador = Valor** Sentencias FIN

⇒ INICIO anotar Tipo Identificador = **Valor** FIN

⇒ INICIO anotar Tipo Identificador = **Termino OpSuma Valor** FIN

⇒ INICIO anotar Tipo Identificador = Termino OpSuma **Valor** FIN

⇒ INICIO anotar Tipo Identificador = Termino OpSuma **Termino** FIN

⇒ INICIO anotar Tipo Identificador = Termino OpSuma **Factor** FIN

⇒ INICIO anotar Tipo Identificador = Termino OpSuma **Numero** FIN

⇒ INICIO anotar Tipo Identificador = Termino OpSuma **5** FIN

⇒ INICIO anotar Tipo Identificador = **Termino OpSuma 5** FIN

⇒ INICIO anotar **Factor OpMul Termino** OpSuma 5 FIN

⇒ INICIO anotar **( Valor )** OpMul Termino OpSuma 5 FIN

⇒ INICIO anotar ( **Termino OpSuma Valor** ) OpMul Termino OpSuma 5 FIN

⇒ INICIO anotar ( Termino OpSuma **Valor** ) OpMul Termino OpSuma 5 FIN

⇒ INICIO anotar ( Termino OpSuma **Termino** ) OpMul Termino OpSuma 5 FIN

⇒ INICIO anotar ( Termino OpSuma **Factor** ) OpMul Termino OpSuma 5 FIN

⇒ INICIO anotar ( Termino OpSuma **Numero** ) OpMul Termino OpSuma 5 FIN

⇒ INICIO anotar ( Termino OpSuma **3** ) OpMul Termino OpSuma 5 FIN

⇒ INICIO anotar ( **Factor OpSuma 3** ) OpMul Termino OpSuma 5 FIN

⇒ INICIO anotar ( **Numero OpSuma 3** ) OpMul Termino OpSuma 5 FIN

⇒ INICIO anotar ( **2 OpSuma 3** ) OpMul Termino OpSuma 5 FIN

⇒ INICIO anotar ( 2 + 3 ) **OpMul Termino OpSuma 5** FIN

⇒ INICIO anotar ( 2 + 3 ) * **Termino OpSuma 5** FIN

⇒ INICIO anotar ( 2 + 3 ) * **Factor OpSuma 5** FIN

⇒ INICIO anotar ( 2 + 3 ) * **Numero OpSuma 5** FIN

⇒ INICIO anotar ( 2 + 3 ) * **4 OpSuma 5** FIN

⇒ INICIO anotar ( 2 + 3 ) * 4 **OpSuma 5** FIN

⇒ INICIO anotar ( 2 + 3 ) * 4 - **5** FIN
