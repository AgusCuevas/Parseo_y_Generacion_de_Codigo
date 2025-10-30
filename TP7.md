INICIO 
  anotar nota x = ( 2 + 3 ) * 2 
FIN.

## TT
| Cod  | Nombre | TipoBase | Padre  | Dimensión | Mínimo | Máximo | Ámbito      |
| ---- | ------ | -------- | ------ | --------- | ------ | ------ | ----------- |
| T001 | nota   | numero   | numero | 1         | -1     | -1     | 0           |

## TS
| Cod  | Nombre | Categoría | Tipo | NumPar | ListaPar | Ámbito |
| ---- | ------ | --------- | ---- | ------ | -------- | ------ |
| S001 | x      | variable  | nota | -1     | —1       | 0      |

------------------------------------------

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

## TT
| Nombre | TipoBase | Padre | Dimensión | Mínimo | Máximo | Ámbito      |
| ------ | -------- | ----- | --------- | ------ | ------ | ----------- |
| nota   | —        | —     | 1         | —      | —      | 0           |
| alumno | —        | —     | 1         | —      | —      | 0           |

## TS
### Linea 1
| Cod  | Nombre  | Categoría     | Tipo | NumPar | ListaPar | Ámbito      |
| ---- | ------- | ------------- | ---- | ------ | -------- | ----------- |
| S001 | n1      | variable      | nota | 0      | —        | 0           |

### Linea 2
| Cod  | Nombre  | Categoría     | Tipo | NumPar | ListaPar | Ámbito      |
| ---- | ------- | ------------- | ---- | ------ | -------- | ----------- |
| S001 | n1      | variable      | nota | 0      | —        | 0           |
| S002 | n2      | variable      | nota | 0      | —        | 0           |

### Linea 3
| Cod  | Nombre  | Categoría     | Tipo   | NumPar | ListaPar | Ámbito      |
| ---- | ------- | ------------- | ------ | ------ | -------- | ----------- |
| S001 | n1      | variable      | nota   | 0      | —        | 0           |
| S002 | n2      | variable      | nota   | 0      | —        | 0           |
| S003 | a1      | variable      | alumno | 0      | —        | 0           |

### Linea 4
| Cod  | Nombre  | Categoría     | Tipo   | NumPar | ListaPar | Ámbito      |
| ---- | ------- | ------------- | ------ | ------ | -------- | ----------- |
| S001 | n1      | variable      | nota   | 0      | —        | 0           |
| S002 | n2      | variable      | nota   | 0      | —        | 0           |
| S003 | a1      | variable      | alumno | 0      | —        | 0           |
| S004 | mayor   | variable      | nota   | 0      | —        | 0           |

### Linea 7
| Cod  | Nombre  | Categoría     | Tipo   | NumPar | ListaPar | Ámbito      |
| ---- | ------- | ------------- | ------ | ------ | -------- | ----------- |
| S001 | n1      | variable      | nota   | 0      | —        | 0           |
| S002 | n2      | variable      | nota   | 0      | —        | 0           |
| S003 | a1      | variable      | alumno | 0      | —        | 0           |
| S004 | mayor   | variable      | nota   | 0      | —        | 0           |
| S005 | mostrar | procedimiento | —      | 1      | String   | 1           |



