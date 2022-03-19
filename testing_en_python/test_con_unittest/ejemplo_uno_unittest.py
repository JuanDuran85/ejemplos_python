"""_summary_

    Usando la libreria unittest para realizar pruebas unitarias.

"""

from unittest import TestCase, main

def multiplicar(num_uno: int, num_dos: int) -> int:
    return num_uno * num_dos

resultado: int = multiplicar(2,3)
print(f"{ resultado = }")

class prueba(TestCase):
    def test(self) -> None:
        self.assertEqual(multiplicar(2,5), 10)
        self.assertEqual(multiplicar(3,5), 15)
        self.assertEqual(multiplicar(1,5), 5)
        
if __name__ == '__main__':
    main()