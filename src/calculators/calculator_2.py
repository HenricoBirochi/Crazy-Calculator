from typing import Dict, List
from flask import request as FlaskRequest
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class Calculator2:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler


    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)
        calculated_number = self.__process_data(input_data)
        return self.__format_response(calculated_number)


    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise Exception("Missing 'numbers' in request body")

        input_data = body["numbers"]
        return input_data


    def __process_data(self, input_data: List[float]) -> float:
        first_process_result = [(x * 11) ** 0.95 for x in input_data]
        result = self.__driver_handler.standard_derivation(first_process_result)
        return float(1.0 / result)


    def __format_response(self, calculated_number: float) -> Dict:
        return {
            "data": {
                "Calculator": 2,
                "result": round(calculated_number, 2)
            }
        }