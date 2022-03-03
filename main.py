from application.salary import calculate_salary
from application.people import get_employees
from datetime import date


def main():
    print(date.today())
    print()


if __name__ == '__main__':
    main()
    calculate_salary()
    get_employees()
