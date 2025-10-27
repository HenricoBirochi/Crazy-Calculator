from typing import Dict
from src.calculators.calculator_1 import Calculator1

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculate():
    mock_request = MockRequest(body={"number": 1})

    calculator_1 = Calculator1()

    response = calculator_1.calculate(request=mock_request)

    print()
    print(response)