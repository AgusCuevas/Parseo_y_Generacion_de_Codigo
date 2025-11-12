# Semántica — Lenguaje Académico

## Tabla semantica
   
### Operadores relacionales

| Operadores              | numero |  nota  |  bool  | alumno |
| ----------------------: | :----: | :----: | :----: | :----: |
|    `<`, `>`, `<=`, `>=` | `bool` | `bool` |    —   |    —   |
|              `==`, `!=` | `bool` | `bool` | `bool` | `bool` |

### Reglas:

- Tratamos nota como numérico para aritmética y comparaciones, tipo compatible con numero.

- Igualdad/desigualdad válidas solo entre mismo tipo.

- No hay comparaciones ordenadas con alumno ni con bool.

### Asignación - compatibilidad de tipos

| Tipo             | numero | nota | bool | alumno | texto           |
| ---------------: | :----: | :--: | :--: | :----: | :-------------: |
|       **numero** |   OK   |  OK  |  -   |   -    |       -         |
|         **nota** |   OK   |  OK  |  -   |   -    |       -         |
|         **bool** |   -    |  -   |  OK  |   -    |       -         |
|       **alumno** |   -    |  -   |  -   |   OK   |        OK       |

## TT / TS

### TT:

- ```numero``` — numérico general.

- ```nota``` — numérico de calificaciones (Rango ```0..10```).

- ```alumno``` — string.

- ```bool``` — booleano.

### TS:

- ```n1 : nota = 8```

- ```n2 : nota = 6```

- ```a1 : alumno = "Agustin"```

- ```mayor : nota = n1 ⇒ 8```

## Cuadro de comprobaciones 
```
INICIO
  anotar nota n1 = 8
  anotar nota n2 = 6
  anotar alumno a1 = "Agustin"  
  anotar nota mayor = n1
  evaluar ( n2 > n1 ) si pasa:
    anotar mayor = n2
    mostrar "Se modifico la mayor nota"
  mostrar mayor
FIN.
```

| Paso | Sentencia                                         | Acción semántica                                                            | Consultas TT/TS                                |        Resultado                |
| :--: | ------------------------------------------------- | --------------------------------------------------------------------------- | ---------------------------------------------- | :-----------------------------: |
|   1  | `INICIO`                                          | Abrir ámbito global                                                         | —                                              |                OK               |
|   2  | `anotar nota n1 = 8`                              | Declarar `n1: nota`; verificar compatibilidad `nota ← numero`               | Asignación: `nota ← numero` = **OK**           |              `n1=8`             |
|   3  | `anotar nota n2 = 6`                              | Declarar `n2: nota`; `nota ← numero`                                        | Asignación: `nota ← numero` =**OK**            |              `n2=6`             |
|   4  | `anotar alumno a1 = "Agustin"`                    | Declarar `a1: alumno`; `alumno ← string`                                    | Asignación: `Alumno ← string` =**OK**          |          `a1="Agustin"`         |
|   5  | `anotar nota mayor = n1`                          | Declarar `mayor: nota`; `nota ← nota`                                       | Asignación: `nota ← numero` =**OK**            |            `mayor=8`            |
|   6  | `evaluar ( n2 > n1 )`                             | Tipar `n2>n1`: ambos `nota` → comparación ordenada válida; resultado `bool` | `nota vs nota` para `>` = **OK**               |       **false** (6>8 es falso)  |
|   7  | `si pasa:` bloque                                 | Requiere evaluar `bool == true`                                             | Condición calculada: **false**                 |              **No**             |
|   8  | `anotar mayor = n2` (en bloque)                   | (Se saltea por condición falsa)                                             |                      —                         |                 -               |
|   9  | `mostrar "Se modifico la mayor nota"` (en bloque) | (Se saltea)                                                                 |                      —                         |                 -               |
|  10  | `mostrar mayor`                                   | Verificar que se puede imprimir `nota` como texto                           | Conversión                                     |         **Imprime `8`**         |
|  11  | `FIN.`                                            | Cerrar                                                                      |                      —                         |                OK               |

### Salida del programa:
```
8
```
No se imprime ```Se modifico la mayor nota``` porque la condición es falsa.
