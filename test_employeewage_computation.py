from employeewage_computation import Employee, Company, MultipleCompany
import pytest


@pytest.fixture
def employee():
    return Employee("Ram", 20, 20, 100)


@pytest.fixture
def company():
    return Company("ABC")


@pytest.fixture
def multiple_company():
    return MultipleCompany()


def test_add_emp(employee, company):
    assert len(company.emp_dict) == 0
    employee.calculate_wage()
    company.add_emp(employee)
    assert len(company.emp_dict) == 1


def test_update_emp(employee, company):
    employee.calculate_wage()
    company.add_emp(employee)
    assert len(company.emp_dict) == 1
    employee = Employee("Ram", 30, 25, 120)
    company.update_emp(employee)
    assert employee.emp_name in company.emp_dict


def test_delete_emp(employee, company):
    employee.calculate_wage()
    company.add_emp(employee)
    assert len(company.emp_dict) == 1
    company.remove_emp(employee.emp_name)
    assert len(company.emp_dict) == 0


def test_add_multiple_company(employee, company, multiple_company):
    assert len(multiple_company.company_dict) == 0
    employee.calculate_wage()
    company.add_emp(employee)
    multiple_company.add_company(company)
    assert len(multiple_company.company_dict) == 1


def test_update_company(employee, company, multiple_company):
    employee.calculate_wage()
    company.add_emp(employee)
    multiple_company.add_company(company)
    assert len(multiple_company.company_dict) == 1
    employee = Employee("Ram", 30, 25, 120)
    company.update_emp(employee)
    multiple_company.update_company(company)
    assert company.company_name in multiple_company.company_dict


def test_remove_company(employee, company, multiple_company):
    employee.calculate_wage()
    company.add_emp(employee)
    multiple_company.add_company(company)
    assert len(multiple_company.company_dict) == 1
    company.remove_emp(employee.emp_name)
    multiple_company.remove_company(company.company_name)
    assert len(multiple_company.company_dict) == 0
