from random import randint


class Employee:

    def __init__(self, wage_per_hr, working_days, total_working_hrs, emp_name):
        self.wage_per_hr = wage_per_hr
        self.working_days = working_days
        self.total_working_hrs = total_working_hrs
        self.emp_name = emp_name
        self.total_wage = 0

    def calculate_wage(self):
        emp_hrs = 0
        emp_working_days = 0
        working_hrs = 0
        while emp_working_days < self.working_days and emp_hrs < self.total_working_hrs:
            random_num = randint(0, 2)
            if random_num:
                working_hrs_dict = {1: 8, 2: 4, 0: 0}
                working_hrs = working_hrs_dict.get(random_num)
            emp_hrs += working_hrs
            emp_working_days += 1
        self.total_wage = emp_hrs * self.wage_per_hr


class Company:

    def __init__(self, company_name):
        self.company_name = company_name
        self.emp_dict = {}

    def add_emp(self, emp_obj):
        self.emp_dict.update({emp_obj.emp_name: emp_obj})
        print(self.emp_dict)


if __name__ == '__main__':
    employee = Employee(20, 20, 100, 'Sathish')
    employee.calculate_wage()
    company = Company("ABC")
    company.add_emp(employee)
