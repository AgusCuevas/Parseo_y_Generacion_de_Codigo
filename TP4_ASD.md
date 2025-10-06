<img width="412" height="828" alt="image" src="https://github.com/user-attachments/assets/3ff55551-5018-44d0-9118-558312ab8215" />


| **Pila**                                                                      | **Entrada**                               | **Transición δ**                                                         |
| ------------------------------------------------------------------------------| ----------------------------------------- | ------------------------------------------------------------------------ |
| ```λ```                                                                       | INICIO anotar nota x = ( 2 + 3 ) * 2 FIN. | ```δ(q0, λ, λ) = (q1, #)```                                              |
| ```#```                                                                       | INICIO anotar nota x = ( 2 + 3 ) * 2 FIN. | ```δ(q1, λ, λ) = (q2, <programa>)```                                     |
| ```<programa>#```                                                             | INICIO anotar nota x = ( 2 + 3 ) * 2 FIN. | ```δ(q2, λ, <programa>) = (q2, INICIO<sentencias>FIN.)```                |
| ```INICIO<sentencias>FIN.#```                                                 | INICIO anotar nota x = ( 2 + 3 ) * 2 FIN. | ```δ(q2, INICIO, INICIO) = (q2, λ)```                                    |
| ```<sentencias>FIN.#```                                                       | anotar nota x = ( 2 + 3 ) * 2 FIN.        | ```δ(q2, λ, <sentencias>) = (q2, <sentencia><sentencias>)```             |
| ```<sentencia><sentencias>FIN.#```                                            | anotar nota x = ( 2 + 3 ) * 2 FIN.        | ```δ(q2, λ, <sentencia>) = (q2, <asignacion>)```                         |
| ```<asignacion><sentencias>FIN.#```                                           | anotar nota x = ( 2 + 3 ) * 2 FIN.        | ```δ(q2, λ, <asignacion>) = (q2, anotar<tipo><identificador>=<valor>)``` |
| ```anotar<tipo><identificador>=<valor><sentencias>FIN.#```                    | anotar nota x = ( 2 + 3 ) * 2 FIN.        | ```δ(q2, anotar, anotar) = (q2, λ)```                                    |
| ```<tipo><identificador>=<valor><sentencias>FIN.#```                          | nota x = ( 2 + 3 ) * 2 FIN.               | ```δ(q2, λ, <tipo>) = (q2, nota)```                                      |
| ```nota<identificador>=<valor><sentencias>FIN.#```                            | nota x = ( 2 + 3 ) * 2 FIN.               | ```δ(q2, nota, nota) = (q2, λ)```                                        |
| ```<identificador>=<valor><sentencias>FIN.#```                                | x = ( 2 + 3 ) * 2 FIN.                    | ```δ(q2, λ, <identificador>) = (q2, <letra><ident_rest>)```              |
| ```<letra><ident_rest>=<valor><sentencias>FIN.#```                            | x = ( 2 + 3 ) * 2 FIN.                    | ```δ(q2, x, <letra>) = (q2, λ)```                                        |
| ```<ident_rest>=<valor><sentencias>FIN.#```                                   | = ( 2 + 3 ) * 2 FIN.                      | ```δ(q2, λ, <ident_rest>) = (q2, λ)```                                   |
| ```=<valor><sentencias>FIN.#```                                               | = ( 2 + 3 ) * 2 FIN.                      | ```δ(q2, =, =) = (q2, λ)```                                              |
| ```<valor><sentencias>FIN.#```                                                | ( 2 + 3 ) * 2 FIN.                        | ```δ(q2, λ, <valor>) = (q2, <termino><op_suma><termino>)```              |
| ```<termino><sentencias>FIN.#```                                              | ( 2 + 3 ) * 2 FIN.                        | ```δ(q2, λ, <termino>) = (q2, <termino><op_mul><factor>)```              |
| ```<termino><op_mul><factor><sentencias>FIN.#```                              | ( 2 + 3 ) * 2 FIN.                        | ```δ(q2, λ, <termino>) = (q2, <factor>)```                               |
| ```<factor><op_mul><factor><sentencias>FIN.#```                               | ( 2 + 3 ) * 2 FIN.                        | ```δ(q2, λ, <factor>) = (q2, ( <valor> ))```                             |
| ```(<valor>)<op_mul><termino><sentencias>FIN.#```                             | ( 2 + 3 ) * 2 FIN.                        | ```δ(q2, (, () = (q2, λ)```                                              |
| ```<valor>)<op_mul><termino><sentencias>FIN.#```                              | 2 + 3 ) * 2 FIN.                          | ```δ(q2, λ, <valor>) = (q2, <termino><op_suma><termino>)```              |
| ```<valor><op_suma><termino>)<op_mul><termino><sentencias>FIN.#```            | 2 + 3 ) * 2 FIN.                          | ```δ(q2, λ, <termino>) = (q2, <factor>)```                               |
| ```<termino><op_suma><termino>)<op_mul><termino><sentencias>FIN.#```          | 2 + 3 ) * 2 FIN.                          | ```δ(q2, λ, <factor>) = (q2, <numero>)```                                |
| ```<factor><op_suma><termino>)<op_mul><termino><sentencias>FIN.#```           | 2 + 3 ) * 2 FIN.                          | ```δ(q2, λ, <numero>) = (q2, <digito><num_rest>)```                      |
| ```<numero><op_suma><termino>)<op_mul><termino><sentencias>FIN.#```           | 2 + 3 ) * 2 FIN.                          | ```δ(q2, λ, <numero>) = (q2, <digito><num_rest>)```                      |
| ```<digito><num_rest><op_suma><termino>)<op_mul><termino><sentencias>FIN.#``` | 2 + 3 ) * 2 FIN.                          | ```δ(q2, 2, <digito>) = (q2, λ)```                                       |
| ```<num_rest><op_suma><termino>)<op_mul><termino><sentencias>FIN.#```         | + 3 ) * 2 FIN.                            | ```δ(q2, λ, <num_rest>) = (q2, λ)```                                     |
| ```<op_suma><termino>)<op_mul><termino><sentencias>FIN.#```                   | + 3 ) * 2 FIN.                            | ```δ(q2, λ, <op_suma>) = (q2, +)```                                      |
| ```+<termino>)<op_mul><termino><sentencias>FIN.#```                           | + 3 ) * 2 FIN.                            | ```δ(q2, +, +) = (q2, λ)```                                              |
| ```<termino>)<op_mul><termino><sentencias>FIN.#```                            | 3 ) * 2 FIN.                              | ```δ(q2, λ, <termino>) = (q2, <factor>)```                               |
| ```<factor>)<op_mul><termino><sentencias>FIN.#```                             | 3 ) * 2 FIN.                              | ```δ(q2, λ, <factor>) = (q2, <numero>)```                                |
| ```<numero>)<op_mul><termino><sentencias>FIN.#```                             | 3 ) * 2 FIN.                              | ```δ(q2, λ, <numero>) = (q2, <digito><num_rest>)```                      |
| ```<digito><num_rest>)<op_mul><termino><sentencias>FIN.#```                   | 3 ) * 2 FIN.                              | ```δ(q2, 3, <digito>) = (q2, λ)```                                       |
| ```<num_rest>)<op_mul><termino><sentencias>FIN.#```                           | ) * 2 FIN.                                | ```δ(q2, λ, <num_rest>) = (q2, λ)```                                     |
| ```)<op_mul><termino><sentencias>FIN.#```                                     | ) * 2 FIN.                                | ```δ(q2, ), )) = (q2, λ)```                                              |
| ```<op_mul><factor><sentencias>FIN.#```                                       | * 2 FIN.                                  | ```δ(q2, λ, context) = (q2, <op_mul><factor>)```                         |
| ```*<factor><sentencias>FIN.#```                                              | * 2 FIN.                                  | ```δ(q2, λ, <op_mul>) = (q2, *)```                                       |
| ```<factor><sentencias>FIN.#```                                               | 2 FIN.                                    | ```δ(q2, *, *) = (q2, λ)```                                              |
| ```<numero><sentencias>FIN.#```                                               | 2 FIN.                                    | ```δ(q2, λ, <factor>) = (q2, <numero>)```                                |
| ```<digito><num_rest><sentencias>FIN.#```                                     | 2 FIN.                                    | ```δ(q2, λ, <numero>) = (q2, <digito><num_rest>)```                      |
| ```<num_rest><sentencias>FIN.#```                                             | FIN.                                      | ```δ(q2, 2, <digito>) = (q2, λ)```                                       |
| ```<sentencias>FIN.#```                                                       | FIN.                                      | ```δ(q2, λ, <num_rest>) = (q2, λ)```                                     |
| ```FIN.#```                                                                   | FIN.                                      | ```δ(q2, λ, <sentencias>) = (q2, λ)```                                   |
| ```#```                                                                       | .                                         | ```δ(q2, FIN, FIN) = (q2, λ) ```                                         |
| ```#```                                                                       | λ                                         | ```δ(q2, ., .) = (q2, λ)```                                              |
| ```λ```                                                                       | λ                                         | ```δ(q2, λ, #) = (q3, λ)``` **ACCEPT**                                   |
