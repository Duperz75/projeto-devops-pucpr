from app import soma, multiplicacao

def test_soma_positivos():
    assert soma(2, 3) == 5

def test_soma_negativos():
    assert soma(-2, -3) == -5

def test_soma_zero():
    assert soma(0, 0) == 0

def test_multiplicacao_positivos():
    assert multiplicacao(2, 3) == 6

def test_multiplicacao_zero():
    assert multiplicacao(5, 0) == 0
