# Análisis Sintáctico Ascendente 

## Cadena
```
INICIO

anotar nota x = (2 + 3) * 2

FIN.
```

| Pila																		| Entrada											| Transición															|
| ------------------------------------------------------------------------- | ------------------------------------------------- | --------------------------------------------------------------------- |
| ```λ```																	| ```INICIO anotar nota x = ( 2 + 3 ) * 2 FIN . ```	|``` δ(q0, λ, λ) = (q1, #)```											|
| ```#```																	| ```INICIO anotar nota x = ( 2 + 3 ) * 2 FIN . ```	|``` shift(INICIO)```													|
| ```# INICIO ```															| ```anotar nota x = ( 2 + 3 ) * 2 FIN .```			|``` shift(anotar)```													|
| ```# INICIO anotar```														| ```nota x = ( 2 + 3 ) * 2 FIN . ```				|``` shift(nota)```														|
| ```# INICIO anotar nota ```												| ```x = ( 2 + 3 ) * 2 FIN .```						|``` reduce: nota ⇒ <tipo> ```											|
| ```# INICIO anotar <tipo> ```												| ```x = ( 2 + 3 ) * 2 FIN .```						|``` shift(x) ```														|
| ```# INICIO anotar <tipo> x ```											| ```= ( 2 + 3 ) * 2 FIN .```						|``` reduce: x ⇒ <identificador> ```									|
| ```# INICIO anotar <tipo> <identificador> ```								| ```= ( 2 + 3 ) * 2 FIN .```						|``` shift(=) ```														|
| ```# INICIO anotar <tipo> <identificador> = ```							| ```( 2 + 3 ) * 2 FIN .```							|``` shift(() ```														|
| ```# INICIO anotar <tipo> <identificador> = ( ```							| ```2 + 3 ) * 2 FIN .```							|``` shift(2) ```														|
| ```# INICIO anotar <tipo> <identificador> = ( 2 ```						| ```+ 3 ) * 2 FIN .```								|``` reduce: 2 ⇒ <numero>```											|
| ```# INICIO anotar <tipo> <identificador> = ( <numero>```					| ```+ 3 ) * 2 FIN .```								|``` reduce: <numero> ⇒ <factor> ```									|
| ```# INICIO anotar <tipo> <identificador> = ( <factor>```					| ```+ 3 ) * 2 FIN .```								|``` reduce: <factor> ⇒ <termino>```									|
| ```# INICIO anotar <tipo> <identificador> = ( <termino> ```				| ```+ 3 ) * 2 FIN .```								|``` shift(+) ```														|
| ```# INICIO anotar <tipo> <identificador> = ( <termino> + ```				| ```3 ) * 2 FIN .```								|``` shift(3) ```														|
| ```# INICIO anotar <tipo> <identificador> = ( <termino> + 3 ```			| ```) * 2 FIN .```									|``` reduce: 3 ⇒ <numero>```											|
| ```# INICIO anotar <tipo> <identificador> = ( <termino> + <numero>```		| ```) * 2 FIN .```									|``` reduce: <numero> ⇒ <factor> ```									|
| ```# INICIO anotar <tipo> <identificador> = ( <termino> + <factor>```		| ```) * 2 FIN .```									|``` reduce: <factor> ⇒ <termino>```									|
| ```# INICIO anotar <tipo> <identificador> = ( <termino> + <termino> ```	| ```) * 2 FIN .```									|``` reduce: <termino>+<termino> ⇒ <expresion> ```						|
| ```# INICIO anotar <tipo> <identificador> = ( <expresion> ```				| ```) * 2 FIN .```									|``` shift()) ```														|
| ```# INICIO anotar <tipo> <identificador> = ( <expresion> ) ```			| ```* 2 FIN .```									|``` reduce: (<expresion>) ⇒ <factor>```								|
| ```# INICIO anotar <tipo> <identificador> = <factor>```					| ```* 2 FIN .```									|``` reduce: <factor> ⇒ <termino>```									|
| ```# INICIO anotar <tipo> <identificador> = <termino> ```					| ```* 2 FIN .```									|``` shift(*) ```														|
| ```# INICIO anotar <tipo> <identificador> = <termino> * ```				| ```2 FIN .```										|``` shift(2) ```														|
| ```# INICIO anotar <tipo> <identificador> = <termino> * 2 ```				| ```FIN .```										|``` reduce: 2 ⇒ <numero>```											|
| ```# INICIO anotar <tipo> <identificador> = <termino> * <numero>```		| ```FIN .```										|``` reduce: <numero> ⇒ <factor> ```									|
| ```# INICIO anotar <tipo> <identificador> = <termino> * <factor>```		| ```FIN .```										|``` reduce: <termino>*<factor> ⇒ <termino>```							|
| ```# INICIO anotar <tipo> <identificador> = <termino> ```					| ```FIN .```										|``` reduce: <termino>=<identificador><tipo>anotar ⇒ <asignacion>```	|
| ```# INICIO <asignacion>```												| ```FIN .```										|``` reduce: <asignacion> ⇒ <sentencia>```								|
| ```# INICIO <sentencia> ```												| ```FIN .```										|``` reduce: <sentencia> ⇒ <bloque>```									|
| ```# INICIO <bloque>```													| ```FIN .```										|``` shift(FIN) con guarda <bloque>INICIO → FIN<bloque>INICIO ```		|
| ```# INICIO<bloque>FIN```													| ```.```											|``` shift(.) con guarda FIN<bloque>INICIO → .FIN<bloque>INICIO ```		|
| ```# INICIO<bloque>FIN. ```												| ```λ```											|``` reduce: .FIN<bloque>INICIO ⇒ <programa> ```						|
| ```# <programa> ```														| ```λ```											|``` δ(q1, λ, <programa>) = (q2, λ) ```									|
| ```#```																	| ```λ```											|``` δ(q2, λ, #) = (q3, λ)```											|
| ```λ```																	| ```λ```											|``` accept ```															|
