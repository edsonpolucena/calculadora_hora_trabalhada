import unittest
from datetime import timedelta
from calculadora_horas import calcular_horas_trabalhadas  

class TestCalculadoraHoras(unittest.TestCase):

    def test_calculo_basico(self):
        """Testa o cálculo de horas trabalhadas em um caso simples."""
        resultado = calcular_horas_trabalhadas('08:00', '17:00')
        esperado = timedelta(hours=9)
        self.assertEqual(resultado, esperado)

    def test_com_intervalo(self):
        """Testa o cálculo com um intervalo de almoço."""
        resultado = calcular_horas_trabalhadas('08:00', '17:00', '01:00')
        esperado = timedelta(hours=8)
        self.assertEqual(resultado, esperado)

    def test_horarios_invertidos(self):
        """Testa a inversão dos horários (UC3), sem interpretar como outro dia."""
        resultado = calcular_horas_trabalhadas('17:00', '08:00')
        esperado = timedelta(hours=9) 
        self.assertEqual(resultado, esperado)

    def test_horarios_sem_dois_pontos(self):
        """Testa a entrada de horários no formato HHmm ou H:mm (UC4)."""
        resultado = calcular_horas_trabalhadas('0800', '1700')
        esperado = timedelta(hours=9)
        self.assertEqual(resultado, esperado)

        resultado2 = calcular_horas_trabalhadas('800', '1700')
        esperado2 = timedelta(hours=9)
        self.assertEqual(resultado2, esperado2)

    def test_intervalo_sem_dois_pontos(self):
        """Testa a entrada de intervalo no formato HHmm (UC4)."""
        resultado = calcular_horas_trabalhadas('0800', '1700', '0100')
        esperado = timedelta(hours=8)
        self.assertEqual(resultado, esperado)

    def test_formato_invalido(self):
        """Testa a entrada com formato inválido."""
        resultado = calcular_horas_trabalhadas('0800', '17:00a')  
        self.assertIsNone(resultado) 

    def test_inversao_horarios_com_intervalo(self):
        """Testa a inversão dos horários com um intervalo."""
        resultado = calcular_horas_trabalhadas('1700', '0800', '0100')
        esperado = timedelta(hours=8)
        self.assertEqual(resultado, esperado)

if __name__ == '__main__':
    unittest.main()
