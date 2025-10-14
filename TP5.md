**Cadena:** INICIO anotar nota x = ( 2 + 3 ) * 2 FIN .

---------------------------------------------

**GIC** - Para cadena 
```
<programa> → INICIO <bloque> FIN .
<bloque> → <sentencia> <bloque> | λ
<sentencia> → <asignacion>
<asignacion> → anotar <tipo> <identificador> = <expresion>
<tipo> → nota
<identificador> → x
<expresion> → <termino> <suma_opcional>
<suma_opcional> → + <termino> <suma_opcional> | λ
<termino> → <factor> <producto_opcional>
<producto_opcional> → * <factor> <producto_opcional> | λ
<factor> → ( <expresion> ) | <numero> 
<numero> → 2 | 3
```

---------------------------------------------

**PRIM** 

```
PRIM(<programa>) = { INICIO }
PRIM(<bloque>) = { anotar, λ }
PRIM(<sentencia>) = { anotar }
PRIM(<asignacion>) = { anotar }
PRIM(<tipo>) = { nota }
PRIM(<identificador>) = { x }
PRIM(<expresion>) = { (, 2, 3 }
PRIM(<suma_opcional>) = { +, λ }
PRIM(<termino>) = { (, 2, 3 }
PRIM(<producto_opcional>) = { *, λ }
PRIM(<factor>) = { (, 2, 3 }
PRIM(<numero>) = { 2, 3 }
```

**SEG** 

```
SEG(<programa>) = { $ }
SEG(<bloque>) = { FIN }
SEG(<sentencia>) = { anotar, FIN }
SEG(<asignacion>) = { anotar, FIN }
SEG(<tipo>) = { x }
SEG(<identificador>) = { = }
SEG(<expresion>) = { ), anotar, FIN }
SEG(<suma_opcional>) = { ), anotar, FIN }
SEG(<termino>) = { +, ), anotar, FIN }
SEG(<producto_opcional>) = { +, ), anotar, FIN }
SEG(<factor>) = { *, +, ), anotar, FIN }
SEG(<numero>) = { *, +, ), anotar, FIN }
```

**PRED** 

```
PRED(<programa> → INICIO <bloque> FIN .) = { INICIO }
PRED(<bloque> → <sentencia> <bloque>) = { anotar }
PRED(<bloque> → λ) = { FIN }
PRED(<sentencia> → <asignacion>) = { anotar }
PRED(<asignacion> → anotar <tipo> <identificador> = <expresion>) = { anotar }
PRED(<tipo> → nota) = { nota }
PRED(<identificador> → x) = { x }
PRED(<expresion> → <termino> <suma_opcional>) = { (, 2, 3 }
PRED(<suma_opcional> → + <termino> <suma_opcional>) = { + }
PRED(<suma_opcional> → λ) = { ), anotar, FIN }
PRED(<termino> → <factor> <producto_opcional>) = { (, 2, 3 }
PRED(<producto_opcional> → * <factor> <producto_opcional>) = { * }
PRED(<producto_opcional> → λ) = { +, ), anotar, FIN }
PRED(<factor> → ( <expresion> )) = { ( }
PRED(<factor> → <numero>) = { 2, 3 }
PRED(<numero> → 2) = { 2 }
PRED(<numero> → 3) = { 3 }
```

---------------------------------------------

|                           |                             INICIO      |                                                     anotar       |          nota       |                   x       |     = |                                        (       |                                        2       |                                             +       |                                        3       |                       )       |                                                    *       |                     FIN       |     . |     $ |
| -----------------------   | ---------------------------------:      | ---------------------------------------------------------:       | ------------:       | ------------------:       | ----: | ---------------------------------------:       | ---------------------------------------:       | --------------------------------------------:       | ---------------------------------------:       | ----------------------:       | ---------------------------------------------------:       | ----------------------:       | ----: | ----: |
| ```<programa>```          | ```<programa> → INICIO <bloque> FIN.``` |                                                      error       |         error       |               error       | error |                                    error       |                                    error       |                                         error       |                                    error       |                   error       |                                                error       |                   error       | error | error |
| ```<bloque>```            |                              error      |                            ```<bloque> → <sentencia> <bloque>``` |         error       |               error       | error |                                    error       |                                    error       |                                         error       |                                    error       |                   error       |                                                error       |            ```<bloque> → λ``` | error | error |
| ```<sentencia>```         |                              error      |                                 ```<sentencia> → <asignacion>``` |         error       |               error       | error |                                    error       |                                    error       |                                         error       |                                    error       |                   error       |                                                error       |                   error       | error | error |
| ```<asignacion>```        |                              error      | ```<asignacion> → anotar <tipo> <identificador> = <expresion>``` |         error       |               error       | error |                                    error       |                                    error       |                                         error       |                                    error       |                   error       |                                                error       |                   error       | error | error |
| ```<tipo>```              |                              error      |                                                      error       | ```<tipo> → nota``` |               error       | error |                                    error       |                                    error       |                                         error       |                                    error       |                   error       |                                                error       |                   error       | error | error |
| ```<identificador>```     |                              error      |                                                      error       |         error       | ```<identificador> → x``` | error |                                    error       |                                    error       |                                         error       |                                    error       |                   error       |                                                error       |                   error       | error | error |
| ```<expresion>```         |                              error      |                                                      error       |         error       |               error       | error |  ```<expresion> → <termino> <suma_opcional>``` |  ```<expresion> → <termino> <suma_opcional>``` |                                         error       |  ```<expresion> → <termino> <suma_opcional>```  |                   error       |                                                error       |                   error       | error | error |
| ```<suma_opcional>```     |                              error      |                                                      error       |         error       |               error       | error |                                    error       |                                    error       | ```<suma_opcional> → + <termino> <suma_opcional>``` |                                    error       |     ```<suma_opcional> → λ``` |                                                error       |     ```<suma_opcional> → λ``` | error | error |
| ```<termino>```           |                              error      |                                                      error       |         error       |               error       | error | ```<termino> → <factor> <producto_opcional>``` | ```<termino> → <factor> <producto_opcional>``` |                                         error       | ```<termino> → <factor> <producto_opcional>``` |                   error       |                                                error       |                   error       | error | error |
| ```<producto_opcional>``` |                              error      |                                                      error       |         error       |               error       | error |                                    error       |                                    error       |                       ```<producto_opcional> → λ``` |                                    error       | ```<producto_opcional> → λ``` | ```<producto_opcional> → * <factor> <producto_opcional>``` | ```<producto_opcional> → λ``` | error | error |
| ```<factor>```            |                              error      |                                                      error       |         error       |               error       | error |               ```<factor> → ( <expresion> )``` |                      ```<factor> → <numero>``` |                                         error       |                      ```<factor> → <numero>``` |                   error       |                                                error       |                   error       | error | error |
| ```<numero>```            |                              error      |                                                      error       |         error       |               error       | error |                                    error       |                             ```<numero> → 2``` |                                         error       |                             ```<numero> → 3``` |                   error       |                                                error       |                   error       | error | error |

---------------------------------------------

| Paso | Pila                                                                                                     | Entrada                                           | Regla o Acción                                                   |
| ---- | -------------------------------------------------------------------------------------------------------- | --------------------------------------------      | ----------------------------------------------------------       |
| 1    | ```$ <programa>```                                                                                       | ```INICIO anotar nota x = ( 2 + 3 ) * 2 FIN. $``` | ```<programa> → INICIO <bloque> FIN.```                          |
| 2    | ```$ INICIO <bloque> FIN.```                                                                             | ```INICIO anotar nota x = ( 2 + 3 ) * 2 FIN. $``` | ```Emparejar(INICIO)```                                          |
| 3    | ```$ <bloque> FIN.```                                                                                    | ```anotar nota x = ( 2 + 3 ) * 2 FIN. $```        | ```<bloque> → <sentencia> <bloque> ```                           |
| 4    | ```$ <sentencia> <bloque> FIN.```                                                                        | ```anotar nota x = ( 2 + 3 ) * 2 FIN. $```        | ```<sentencia> → <asignacion>```                                 |
| 5    | ```$ <asignacion> <bloque> FIN.```                                                                       | ```anotar nota x = ( 2 + 3 ) * 2 FIN. $```        | ```<asignacion> → anotar <tipo> <identificador> = <expresion>``` |
| 6    | ```$ anotar <tipo> <identificador> = <expresion> <bloque> FIN.```                                        | ```anotar nota x = ( 2 + 3 ) * 2 FIN. $```        | ```Emparejar(anotar)```                                          |
| 7    | ```$ <tipo> <identificador> = <expresion> <bloque> FIN.```                                               | ```nota x = ( 2 + 3 ) * 2 FIN. $```               | ```<tipo> → nota```                                              |
| 8    | ```$ nota <identificador> = <expresion> <bloque> FIN.```                                                 | ```nota x = ( 2 + 3 ) * 2 FIN. $```               | ```Emparejar(nota)```                                            |
| 9    | ```$ <identificador> = <expresion> <bloque> FIN.```                                                      | ```x = ( 2 + 3 ) * 2 FIN. $```                    | ```<identificador> → x```                                        |
| 10   | ```$ x = <expresion> <bloque> FIN.```                                                                    | ```x = ( 2 + 3 ) * 2 FIN. $```                    | ```Emparejar(x)```                                               |
| 11   | ```$ = <expresion> <bloque> FIN.```                                                                      | ```= ( 2 + 3 ) * 2 FIN. $```                      | ```Emparejar(=)```                                               |
| 12   | ```$ <expresion> <bloque> FIN.```                                                                        | ```( 2 + 3 ) * 2 FIN. $```                        | ```<expresion> → <termino> <suma_opcional>```                    |
| 13   | ```$ <termino> <suma_opcional> <bloque> FIN.```                                                          | ```( 2 + 3 ) * 2 FIN. $```                        | ```<termino> → <factor> <producto_opcional>```                   |
| 14   | ```$ <factor> <producto_opcional> <suma_opcional> <bloque> FIN.```                                       | ```( 2 + 3 ) * 2 FIN. $```                        | ```<factor> → ( <expresion> )```                                 |
| 15   | ```$ ( <expresion> ) <producto_opcional> <suma_opcional> <bloque> FIN.```                                | ```( 2 + 3 ) * 2 FIN. $```                        | ```Emparejar(()```                                               |
| 16   | ```$ <expresion> ) <producto_opcional> <suma_opcional> <bloque> FIN.```                                  | ```2 + 3 ) * 2 FIN. $```                          | ```<expresion> → <termino> <suma_opcional>```                    |
| 17   | ```$ <termino> <suma_opcional> ) <producto_opcional> <suma_opcional> <bloque> FIN.```                    | ```2 + 3 ) * 2 FIN. $```                          | ```<termino> → <factor> <producto_opcional>```                   |
| 18   | ```$ <factor> <producto_opcional> <suma_opcional> ) <producto_opcional> <suma_opcional> <bloque> FIN.``` | ```2 + 3 ) * 2 FIN. $```                          | ```<factor> → <numero>```                                        |
| 19   | ```$ <numero> <producto_opcional> <suma_opcional> ) <producto_opcional> <suma_opcional> <bloque> FIN.``` | ```2 + 3 ) * 2 FIN. $```                          | ```<numero> → 2```                                               |
| 20   | ```$ 2 <producto_opcional> <suma_opcional> ) <producto_opcional> <suma_opcional> <bloque> FIN.```        | ```2 + 3 ) * 2 FIN. $```                          | ```Emparejar(2)```                                               |
| 21   | ```$ <producto_opcional> <suma_opcional> ) <producto_opcional> <suma_opcional> <bloque> FIN.```          | ```+ 3 ) * 2 FIN. $```                            | ```<producto_opcional> → λ```                                    |
| 22   | ```$ <suma_opcional> ) <producto_opcional> <suma_opcional> <bloque> FIN.```                              | ```+ 3 ) * 2 FIN. $```                            | ```<suma_opcional> → + <termino> <suma_opcional>```              |
| 23   | ```$ + <termino> <suma_opcional> ) <producto_opcional> <suma_opcional> <bloque> FIN.```                  | ```+ 3 ) * 2 FIN. $```                            | ```Emparejar(+)```                                               |
| 24   | ```$ <termino> <suma_opcional> ) <producto_opcional> <suma_opcional> <bloque> FIN.```                    | ```3 ) * 2 FIN. $```                              | ```<termino> → <factor> <producto_opcional>```                   |
| 25   | ```$ <factor> <producto_opcional> <suma_opcional> ) <producto_opcional> <suma_opcional> <bloque> FIN.``` | ```3 ) * 2 FIN. $```                              | ```<factor> → <numero>```                                        |
| 26   | ```$ <numero> <producto_opcional> <suma_opcional> ) <producto_opcional> <suma_opcional> <bloque> FIN.``` | ```3 ) * 2 FIN. $```                              | ```<numero> → 3```                                                |
| 27   | ```$ 3 <producto_opcional> <suma_opcional> ) <producto_opcional> <suma_opcional> <bloque> FIN.```        | ```3 ) * 2 FIN. $```                              | ```Emparejar(3)```                                               |
| 28   | ```$ <producto_opcional> <suma_opcional> ) <producto_opcional> <suma_opcional> <bloque> FIN.```          | ```) * 2 FIN. $```                                | ```<producto_opcional> → λ```                                    |
| 29   | ```$ <suma_opcional> ) <producto_opcional> <suma_opcional> <bloque> FIN.```                              | ```) * 2 FIN. $```                                | ```<suma_opcional> → λ```                                        |
| 30   | ```$ ) <producto_opcional> <suma_opcional> <bloque> FIN.```                                              | ```) * 2 FIN. $```                                | ```Emparejar())```                                               |
| 31   | ```$ <producto_opcional> <suma_opcional> <bloque> FIN.```                                                | ```* 2 FIN. $```                                  | ```<producto_opcional> → * <factor> <producto_opcional>```       |
| 32   | ```$ * <factor> <producto_opcional> <suma_opcional> <bloque> FIN.```                                     | ```* 2 FIN. $```                                  | ```Emparejar(*)```                                               |
| 33   | ```$ <factor> <producto_opcional> <suma_opcional> <bloque> FIN.```                                       | ```2 FIN. $```                                    | ```<factor> → <numero>```                                        |
| 34   | ```$ <numero> <producto_opcional> <suma_opcional> <bloque> FIN.```                                       | ```2 FIN. $```                                    | ```<numero> → 2```                                               |
| 35   | ```$ 2 <producto_opcional> <suma_opcional> <bloque> FIN.```                                              | ```2 FIN. $```                                    | ```Emparejar(2)```                                               |
| 36   | ```$ <producto_opcional> <suma_opcional> <bloque> FIN.```                                                | ```FIN. $```                                      | ```<producto_opcional> → λ```                                    |
| 37   | ```$ <suma_opcional> <bloque> FIN.```                                                                    | ```FIN. $```                                      | ```<suma_opcional> → λ```                                        |
| 38   | ```$ <bloque> FIN.```                                                                                    | ```FIN. $```                                      | ```<bloque> → λ```                                               |
| 39   | ```$ FIN.```                                                                                             | ```FIN. $```                                      | ```Emparejar(FIN)```                                             |
| 40   | ```$ .```                                                                                                | ```. $```                                         | ```Emparejar(.)```                                               |
| 41   | ```$```                                                                                                  | ```$```                                           | **accept**                                                 |
