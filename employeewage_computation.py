from random import randint


def employee_check(random_num):
    if random_num == 1:
        return True
    return False


def calculate_wage():
    wage_per_hr = 20
    working_hr = 8
    if employee_check(random_num):
        wage_per_day = wage_per_hr * working_hr
        print("Employee Wage Per Day : ", wage_per_day)
    else:
        print("Employee Wage Per Day : ", 0)


if __name__ == "__main__":
    random_num = randint(0, 1)
    if employee_check(random_num):
       print("Employee is Present")
    else:
       print("Employee is Absent")
    calculate_wage()
