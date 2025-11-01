# Análisis Sintáctico Descendente con Retroceso 

## Cadena
```
INICIO

anotar nota x = (2 + 3) * 2

FIN.
```

| **Pila**                                                                                               | **Entrada**                                 | **Transición δ**                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------- | --------------------------------------------------------------------------- |
| `λ`                                                                                                    | `INICIO anotar nota x = ( 2 + 3 ) * 2 FIN.` | `δ(q0, λ, λ) = (q1, #)`                                                     |
| `#`                                                                                                    | `INICIO anotar nota x = ( 2 + 3 ) * 2 FIN.` | `δ(q1, λ, λ) = (q2, <programa>)`                                            |
| `<programa>#`                                                                                          | `INICIO anotar nota x = ( 2 + 3 ) * 2 FIN.` | `δ(q2, λ, <programa>) = (q2, INICIO<bloque>FIN.)`                           |
| `INICIO<bloque>FIN.#`                                                                                  | `INICIO anotar nota x = ( 2 + 3 ) * 2 FIN.` | `δ(q2, INICIO, INICIO) = (q2, λ)`                                           |
| `<bloque>FIN.#`                                                                                        | ` anotar nota x = ( 2 + 3 ) * 2 FIN.`       | `δ(q2, ' ', λ) = (q2, λ)`                                                   |
| `<bloque>FIN.#`                                                                                        | `anotar nota x = ( 2 + 3 ) * 2 FIN.`        | `δ(q2, λ, <bloque>) = (q2, <sentencia><bloque>)`                            |
| `<sentencia><bloque>FIN.#`                                                                             | `anotar nota x = ( 2 + 3 ) * 2 FIN.`        | `δ(q2, λ, <sentencia>) = (q2, <asignacion>)`                                |
| `<asignacion><bloque>FIN.#`                                                                            | `anotar nota x = ( 2 + 3 ) * 2 FIN.`        | `δ(q2, λ, <asignacion>) = (q2, anotar<tipo><identificador>=<expresion>)`    |
| `anotar<tipo><identificador>=<expresion><bloque>FIN.#`                                                 | `anotar nota x = ( 2 + 3 ) * 2 FIN.`        | `δ(q2, anotar, anotar) = (q2, λ)`                                           |
| `<tipo><identificador>=<expresion><bloque>FIN.#`                                                       | ` nota x = ( 2 + 3 ) * 2 FIN.`              | `δ(q2, ' ', λ) = (q2, λ)`                                                   |
| `<tipo><identificador>=<expresion><bloque>FIN.#`                                                       | `nota x = ( 2 + 3 ) * 2 FIN.`               | `δ(q2, λ, <tipo>) = (q2, nota)`                                             |
| `nota<identificador>=<expresion><bloque>FIN.#`                                                         | `nota x = ( 2 + 3 ) * 2 FIN.`               | `δ(q2, nota, nota) = (q2, λ)`                                               |
| `<identificador>=<expresion><bloque>FIN.#`                                                             | ` x = ( 2 + 3 ) * 2 FIN.`                   | `δ(q2, ' ', λ) = (q2, λ)`                                                   |
| `<identificador>=<expresion><bloque>FIN.#`                                                             | `x = ( 2 + 3 ) * 2 FIN.`                    | `δ(q2, λ, <identificador>) = (q2, <letra><resto_identificador>)`            |
| `<letra><resto_identificador>=<expresion><bloque>FIN.#`                                                | `x = ( 2 + 3 ) * 2 FIN.`                    | `δ(q2, x, <letra>) = (q2, λ)`                                               |
| `<resto_identificador>=<expresion><bloque>FIN.#`                                                       | ` = ( 2 + 3 ) * 2 FIN.`                     | `δ(q2, ' ', λ) = (q2, λ)`                                                   |
| `<resto_identificador>=<expresion><bloque>FIN.#`                                                       | `= ( 2 + 3 ) * 2 FIN.`                      | `δ(q2, λ, <resto_identificador>) = (q2, λ)`                                 |
| `=<expresion><bloque>FIN.#`                                                                            | `= ( 2 + 3 ) * 2 FIN.`                      | `δ(q2, =, =) = (q2, λ)`                                                     |
| `<expresion><bloque>FIN.#`                                                                             | ` ( 2 + 3 ) * 2 FIN.`                       | `δ(q2, ' ', λ) = (q2, λ)`                                                   |
| `<expresion><bloque>FIN.#`                                                                             | `( 2 + 3 ) * 2 FIN.`                        | `δ(q2, λ, <expresion>) = (q2, <termino><suma_opcional>)`                    |
| `<termino><suma_opcional><bloque>FIN.#`                                                                | `( 2 + 3 ) * 2 FIN.`                        | `δ(q2, λ, <termino>) = (q2, <factor><producto_opcional>)`                   |
| `<factor><producto_opcional><suma_opcional><bloque>FIN.#`                                              | `( 2 + 3 ) * 2 FIN.`                        | `δ(q2, λ, <factor>) = (q2, (<expresion>))`                                  |
| `(<expresion>)<producto_opcional><suma_opcional><bloque>FIN.#`                                         | `( 2 + 3 ) * 2 FIN.`                        | `δ(q2, '(', '(') = (q2, λ)`                                                 |
| `<expresion>)<producto_opcional><suma_opcional><bloque>FIN.#`                                          | ` 2 + 3 ) * 2 FIN.`                         | `δ(q2, ' ', λ) = (q2, λ)`                                                   |
| `<expresion>)<producto_opcional><suma_opcional><bloque>FIN.#`                                          | `2 + 3 ) * 2 FIN.`                          | `δ(q2, λ, <expresion>) = (q2, <termino><suma_opcional>)`                    |
| `<termino><suma_opcional>)<producto_opcional><suma_opcional><bloque>FIN.#`                             | `2 + 3 ) * 2 FIN.`                          | `δ(q2, λ, <termino>) = (q2, <factor><producto_opcional>)`                   |
| `<factor><producto_opcional><suma_opcional>)<producto_opcional><suma_opcional><bloque>FIN.#`           | `2 + 3 ) * 2 FIN.`                          | `δ(q2, λ, <factor>) = (q2, <numero>)`                                       |
| `<numero><producto_opcional><suma_opcional>)<producto_opcional><suma_opcional><bloque>FIN.#`           | `2 + 3 ) * 2 FIN.`                          | `δ(q2, λ, <numero>) = (q2, <digito><num_rest>)`                             |
| `<digito><num_rest><producto_opcional><suma_opcional>)<producto_opcional><suma_opcional><bloque>FIN.#` | `2 + 3 ) * 2 FIN.`                          | `δ(q2, 2, <digito>) = (q2, λ)`                                              |
| `<num_rest><producto_opcional><suma_opcional>)<producto_opcional><suma_opcional><bloque>FIN.#`         | ` + 3 ) * 2 FIN.`                           | `δ(q2, ' ', λ) = (q2, λ)`                                                   |
| `<num_rest><producto_opcional><suma_opcional>)<producto_opcional><suma_opcional><bloque>FIN.#`         | `+ 3 ) * 2 FIN.`                            | `δ(q2, λ, <num_rest>) = (q2, λ)`                                            |
| `<producto_opcional><suma_opcional>)<producto_opcional><suma_opcional><bloque>FIN.#`                   | `+ 3 ) * 2 FIN.`                            | `δ(q2, λ, <producto_opcional>) = (q2, λ)`                                   |
| `<suma_opcional>)<producto_opcional><suma_opcional><bloque>FIN.#`                                      | `+ 3 ) * 2 FIN.`                            | `δ(q2, λ, <suma_opcional>) = (q2, <op_suma><termino><suma_opcional>)`       |
| `<op_suma><termino><suma_opcional>)<producto_opcional><suma_opcional><bloque>FIN.#`                    | `+ 3 ) * 2 FIN.`                            | `δ(q2, +, +) = (q2, λ)`                                                     |
| `<termino><suma_opcional>)<producto_opcional><suma_opcional><bloque>FIN.#`                             | ` 3 ) * 2 FIN.`                             | `δ(q2, ' ', λ) = (q2, λ)`                                                   |
| `<termino><suma_opcional>)<producto_opcional><suma_opcional><bloque>FIN.#`                             | `3 ) * 2 FIN.`                              | `δ(q2, λ, <termino>) = (q2, <factor><producto_opcional>)`                   |
| `<factor><producto_opcional><suma_opcional>)<producto_opcional><suma_opcional><bloque>FIN.#`           | `3 ) * 2 FIN.`                              | `δ(q2, λ, <factor>) = (q2, <numero>)`                                       |
| `<numero><producto_opcional><suma_opcional>)<producto_opcional><suma_opcional><bloque>FIN.#`           | `3 ) * 2 FIN.`                              | `δ(q2, λ, <numero>) = (q2, <digito><num_rest>)`                             |
| `<digito><num_rest><producto_opcional><suma_opcional>)<producto_opcional><suma_opcional><bloque>FIN.#` | `3 ) * 2 FIN.`                              | `δ(q2, 3, <digito>) = (q2, λ)`                                              |
| `<num_rest><producto_opcional><suma_opcional>)<producto_opcional><suma_opcional><bloque>FIN.#`         | ` ) * 2 FIN.`                               | `δ(q2, ' ', λ) = (q2, λ)`                                                   |
| `<num_rest><producto_opcional><suma_opcional>)<producto_opcional><suma_opcional><bloque>FIN.#`         | `) * 2 FIN.`                                | `δ(q2, λ, <num_rest>) = (q2, λ)`                                            |
| `<producto_opcional><suma_opcional>)<producto_opcional><suma_opcional><bloque>FIN.#`                   | `) * 2 FIN.`                                | `δ(q2, λ, <producto_opcional>) = (q2, λ)`                                   |
| `<suma_opcional>)<producto_opcional><suma_opcional><bloque>FIN.#`                                      | `) * 2 FIN.`                                | `δ(q2, λ, <suma_opcional>) = (q2, λ)`                                       |
| `)<producto_opcional><suma_opcional><bloque>FIN.#`                                                     | `) * 2 FIN.`                                | `δ(q2, ')', ')') = (q2, λ)`                                                 |
| `<producto_opcional><suma_opcional><bloque>FIN.#`                                                      | ` * 2 FIN.`                                 | `δ(q2, ' ', λ) = (q2, λ)`                                                   |
| `<producto_opcional><suma_opcional><bloque>FIN.#`                                                      | `* 2 FIN.`                                  | `δ(q2, λ, <producto_opcional>) = (q2, <op_mul><factor><producto_opcional>)` |
| `<op_mul><factor><producto_opcional><suma_opcional><bloque>FIN.#`                                      | `* 2 FIN.`                                  | `δ(q2, *, *) = (q2, λ)`                                                     |
| `<factor><producto_opcional><suma_opcional><bloque>FIN.#`                                              | ` 2 FIN.`                                   | `δ(q2, ' ', λ) = (q2, λ)`                                                   |
| `<factor><producto_opcional><suma_opcional><bloque>FIN.#`                                              | `2 FIN.`                                    | `δ(q2, λ, <factor>) = (q2, <numero>)`                                       |
| `<numero><producto_opcional><suma_opcional><bloque>FIN.#`                                              | `2 FIN.`                                    | `δ(q2, λ, <numero>) = (q2, <digito><num_rest>)`                             |
| `<digito><num_rest><producto_opcional><suma_opcional><bloque>FIN.#`                                    | `2 FIN.`                                    | `δ(q2, 2, <digito>) = (q2, λ)`                                              |
| `<num_rest><producto_opcional><suma_opcional><bloque>FIN.#`                                            | ` FIN.`                                     | `δ(q2, ' ', λ) = (q2, λ)`                                                   |
| `<num_rest><producto_opcional><suma_opcional><bloque>FIN.#`                                            | `FIN.`                                      | `δ(q2, λ, <num_rest>) = (q2, λ)`                                            |
| `<producto_opcional><suma_opcional><bloque>FIN.#`                                                      | `FIN.`                                      | `δ(q2, λ, <producto_opcional>) = (q2, λ)`                                   |
| `<suma_opcional><bloque>FIN.#`                                                                         | `FIN.`                                      | `δ(q2, λ, <suma_opcional>) = (q2, λ)`                                       |
| `<bloque>FIN.#`                                                                                        | `FIN.`                                      | `δ(q2, λ, <bloque>) = (q2, λ)`                                              |
| `FIN.#`                                                                                                | `FIN.`                                      | `δ(q2, FIN, FIN) = (q2, λ)`                                                 |
| `#`                                                                                                    | `.`                                         | `δ(q2, ., .) = (q2, λ)`                                                     |
| `λ`                                                                                                    | `λ`                                         | `δ(q2, λ, #) = (q3, λ)  ACCEPT`                                             |



<img width="412" height="828" alt="image" src="https://github.com/user-attachments/assets/3ff55551-5018-44d0-9118-558312ab8215" />

