import logging

from flask import jsonify, request, make_response

from . import app
from .income_calculator import IncomeCalculator

logger = logging.getLogger(__name__)
income_calculator = IncomeCalculator()


@app.route('/calc_salary', methods=['GET'])
def calc_salary():
    def field_not_found(name: str):
        return make_response(jsonify({'code': 400, 'message': f"{name} field is not set"}), 400)

    logger.info("Get request")

    args = request.args

    year = args.get("year", type=int)
    if year is None:
        return field_not_found("year")

    month = args.get("month", type=int)
    if month is None:
        return field_not_found("month")

    salary = args.get("salary", type=int)
    if salary is None:
        return field_not_found("salary")

    logger.info(f"Recognized parameters: year={year}, month={month}, salary={salary}")

    hour_income = income_calculator.get_hour_income(year, month, salary)
    return make_response(jsonify({'year': year, 'month': month, 'salary': salary, 'hour_income': hour_income}), 200)
