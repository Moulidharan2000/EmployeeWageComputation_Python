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

    def remove_emp(self, emp_name):
        if emp_name in self.emp_dict:
            self.emp_dict.pop(emp_name)

    def display(self):
        keys_list = list(self.emp_dict.keys())
        values_list = list(self.emp_dict.values())
        for i in range(len(keys_list)):
            print(keys_list[i], " : ", values_list[i])


if __name__ == '__main__':
    company = Company("ABC")
    while True:
        option = int(input("\n1.Add Employee\n2.Update Employee\n3.Delete Employee\n4.Display Details\n0.Exit\nEnter the Option : "))
        if option == 1 or option == 2:
            emp_name = input("Enter the Employee Name : ")
            wage_per_hr = int(input("Enter the Wage per Hour : "))
            working_days = int(input("Enter the number of working days : "))
            total_working_hrs = int(input("Enter the total working hours : "))
            employee = Employee(emp_name, wage_per_hr, working_days, total_working_hrs)
            employee.calculate_wage()
            company.add_emp(employee) if option == 1 else company.update_emp(employee)
            print("Employee Details Added...") if option == 1 else print("Employee Details Updated...")
        elif option == 3:
            emp_name = input("Enter the Employee Name : ")
            company.remove_emp(emp_name)
            print("Employee Details Deleted...")
        elif option == 4:
            print("Employee Details : ")
            company.display()
        elif option == 0:
            print("Exited...")
            break
