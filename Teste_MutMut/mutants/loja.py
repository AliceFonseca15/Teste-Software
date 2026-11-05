

from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_calcular_desconto__mutmut: MutantDict = {}  # type: ignore
@_mutmut_mutated(mutants_x_calcular_desconto__mutmut)
def calcular_desconto(valor_total: float, fidelidade: bool) -> float:
  if valor_total > 100.0:
     desconto = 0.10
  else:
    desconto = 0.0
  if fidelidade:
     desconto += 0.05
  return valor_total * (1.0 - desconto)

  
def x_calcular_desconto__mutmut_orig(valor_total: float, fidelidade: bool) -> float:
  if valor_total > 100.0:
     desconto = 0.10
  else:
    desconto = 0.0
  if fidelidade:
     desconto += 0.05
  return valor_total * (1.0 - desconto)

  
def x_calcular_desconto__mutmut_1(valor_total: float, fidelidade: bool) -> float:
  if valor_total >= 100.0:
     desconto = 0.10
  else:
    desconto = 0.0
  if fidelidade:
     desconto += 0.05
  return valor_total * (1.0 - desconto)

  
def x_calcular_desconto__mutmut_2(valor_total: float, fidelidade: bool) -> float:
  if valor_total > 101.0:
     desconto = 0.10
  else:
    desconto = 0.0
  if fidelidade:
     desconto += 0.05
  return valor_total * (1.0 - desconto)

  
def x_calcular_desconto__mutmut_3(valor_total: float, fidelidade: bool) -> float:
  if valor_total > 100.0:
     desconto = None
  else:
    desconto = 0.0
  if fidelidade:
     desconto += 0.05
  return valor_total * (1.0 - desconto)

  
def x_calcular_desconto__mutmut_4(valor_total: float, fidelidade: bool) -> float:
  if valor_total > 100.0:
     desconto = 1.1
  else:
    desconto = 0.0
  if fidelidade:
     desconto += 0.05
  return valor_total * (1.0 - desconto)

  
def x_calcular_desconto__mutmut_5(valor_total: float, fidelidade: bool) -> float:
  if valor_total > 100.0:
     desconto = 0.10
  else:
    desconto = None
  if fidelidade:
     desconto += 0.05
  return valor_total * (1.0 - desconto)

  
def x_calcular_desconto__mutmut_6(valor_total: float, fidelidade: bool) -> float:
  if valor_total > 100.0:
     desconto = 0.10
  else:
    desconto = 1.0
  if fidelidade:
     desconto += 0.05
  return valor_total * (1.0 - desconto)

  
def x_calcular_desconto__mutmut_7(valor_total: float, fidelidade: bool) -> float:
  if valor_total > 100.0:
     desconto = 0.10
  else:
    desconto = 0.0
  if fidelidade:
     desconto = 0.05
  return valor_total * (1.0 - desconto)

  
def x_calcular_desconto__mutmut_8(valor_total: float, fidelidade: bool) -> float:
  if valor_total > 100.0:
     desconto = 0.10
  else:
    desconto = 0.0
  if fidelidade:
     desconto -= 0.05
  return valor_total * (1.0 - desconto)

  
def x_calcular_desconto__mutmut_9(valor_total: float, fidelidade: bool) -> float:
  if valor_total > 100.0:
     desconto = 0.10
  else:
    desconto = 0.0
  if fidelidade:
     desconto += 1.05
  return valor_total * (1.0 - desconto)

  
def x_calcular_desconto__mutmut_10(valor_total: float, fidelidade: bool) -> float:
  if valor_total > 100.0:
     desconto = 0.10
  else:
    desconto = 0.0
  if fidelidade:
     desconto += 0.05
  return valor_total / (1.0 - desconto)

  
def x_calcular_desconto__mutmut_11(valor_total: float, fidelidade: bool) -> float:
  if valor_total > 100.0:
     desconto = 0.10
  else:
    desconto = 0.0
  if fidelidade:
     desconto += 0.05
  return valor_total * (1.0 + desconto)

  
def x_calcular_desconto__mutmut_12(valor_total: float, fidelidade: bool) -> float:
  if valor_total > 100.0:
     desconto = 0.10
  else:
    desconto = 0.0
  if fidelidade:
     desconto += 0.05
  return valor_total * (2.0 - desconto)

  

mutants_x_calcular_desconto__mutmut['_mutmut_orig'] = x_calcular_desconto__mutmut_orig # type: ignore # mutmut generated
mutants_x_calcular_desconto__mutmut['x_calcular_desconto__mutmut_1'] = x_calcular_desconto__mutmut_1 # type: ignore # mutmut generated
mutants_x_calcular_desconto__mutmut['x_calcular_desconto__mutmut_2'] = x_calcular_desconto__mutmut_2 # type: ignore # mutmut generated
mutants_x_calcular_desconto__mutmut['x_calcular_desconto__mutmut_3'] = x_calcular_desconto__mutmut_3 # type: ignore # mutmut generated
mutants_x_calcular_desconto__mutmut['x_calcular_desconto__mutmut_4'] = x_calcular_desconto__mutmut_4 # type: ignore # mutmut generated
mutants_x_calcular_desconto__mutmut['x_calcular_desconto__mutmut_5'] = x_calcular_desconto__mutmut_5 # type: ignore # mutmut generated
mutants_x_calcular_desconto__mutmut['x_calcular_desconto__mutmut_6'] = x_calcular_desconto__mutmut_6 # type: ignore # mutmut generated
mutants_x_calcular_desconto__mutmut['x_calcular_desconto__mutmut_7'] = x_calcular_desconto__mutmut_7 # type: ignore # mutmut generated
mutants_x_calcular_desconto__mutmut['x_calcular_desconto__mutmut_8'] = x_calcular_desconto__mutmut_8 # type: ignore # mutmut generated
mutants_x_calcular_desconto__mutmut['x_calcular_desconto__mutmut_9'] = x_calcular_desconto__mutmut_9 # type: ignore # mutmut generated
mutants_x_calcular_desconto__mutmut['x_calcular_desconto__mutmut_10'] = x_calcular_desconto__mutmut_10 # type: ignore # mutmut generated
mutants_x_calcular_desconto__mutmut['x_calcular_desconto__mutmut_11'] = x_calcular_desconto__mutmut_11 # type: ignore # mutmut generated
mutants_x_calcular_desconto__mutmut['x_calcular_desconto__mutmut_12'] = x_calcular_desconto__mutmut_12 # type: ignore # mutmut generated