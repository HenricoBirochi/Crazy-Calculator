from typing import Dict
from src.calculators.calculator_4 import Calculator4

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculate():
    mock_request = MockRequest({"numbers": [10, 30, 20, 10]})
    calculator_4 = Calculator4()

    response = calculator_4.calculate(mock_request)

    assert response == {'data': {'Calculator': 4, 'value': 17.5}}