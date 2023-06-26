from random import randint


class Employee:

    def __init__(self, emp_name, wage_per_hr, working_days, total_working_hrs):
        self.emp_name = emp_name
        self.wage_per_hr = wage_per_hr
        self.working_days = working_days
        self.total_working_hrs = total_working_hrs
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
        self.emp_dict.update({emp_obj.emp_name: emp_obj.total_wage})

    def update_emp(self, emp_obj):
        if emp_obj.emp_name in self.emp_dict:
            self.emp_dict.update({emp_obj.emp_name: emp_obj.total_wage})
        else:
            print("Employee is not Found...")

    def remove_emp(self, emp_name):
        if emp_name in self.emp_dict:
            self.emp_dict.pop(emp_name)
            print("Employee Details are Deleted...")
        else:
            print("Employee is not Found...")

    def display(self):
        for i, j in self.emp_dict.items():
            print(i, " : ", j)


class MultipleCompany:
    def __init__(self):
        self.company_dict = {}

    def add_company(self, comp_obj):
        self.company_dict.update({comp_obj.company_name: comp_obj})

    def update_company(self, comp_obj):
        if comp_obj.company_name in self.company_dict:
            self.company_dict.update({comp_obj.company_name: comp_obj})
        else:
            print("Company Details not Found...")

    def remove_company(self, company_name):
        if company_name in self.company_dict:
            self.company_dict.pop(company_name)
            print("Company Details are Deleted...")
        else:
            print("Company not Found...")

    def get_company(self):
        for i, j in self.company_dict.items():
            print(i, " : ", len(j.emp_dict))


if __name__ == '__main__':
    multiple_company = MultipleCompany()
    while True:
        option = int(input("\n1.Add Employee\n2.Update Employee\n3.Delete Employee\n4.Delete Company\n5.Display  Details\n6.Multiple Companies Details\n0.Exit\nEnter the Option : "))
        if option == 1 or option == 2:
            company_name = input("\nEnter the Company Name : ")
            company = multiple_company.company_dict.get(company_name)
            if not company:
                company = Company(company_name)
            emp_name = input("Enter the Employee Name : ")
            wage_per_hr = int(input("Enter the Wage per Hour : "))
            working_days = int(input("Enter the number of working days : "))
            total_working_hrs = int(input("Enter the total working hours : "))
            employee = Employee(emp_name, wage_per_hr, working_days, total_working_hrs)
            employee.calculate_wage()
            if option == 1:
                company.add_emp(employee)
                multiple_company.add_company(company)
                print("Employee and Company Details are Added...")
            else:
                company.update_emp(employee)
                multiple_company.update_company(company)
                print("Employee Details are Updated...")
        elif option == 3:
            company_name = input("Enter the Company Name : ")
            emp_name = input("Enter the Employee Name : ")
            company.remove_emp(emp_name)
        elif option == 4:
            company_name = input("Enter the Company Name : ")
            multiple_company.remove_company(company_name)
        elif option == 5:
            print("Employee Details : ")
            companies = input("Enter Company Name : ")
            company_employees = multiple_company.company_dict.get(companies)
            if not company_employees:
                print("Company Not Found....")
            else:
                company_employees.display()
        elif option == 6:
            if not multiple_company.company_dict:
                print("No Companies Present...")
            else:
                multiple_company.get_company()
        elif option == 0:
            print("Exited...")
            break
