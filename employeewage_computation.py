from random import randint

WAGE_PER_HR = 20
WORKING_DAYS = 20
TOTAL_WORKING_HRS = 100


def calculate_wage():
    total_emp_hrs = 0
    total_working_days = 1
    working_hrs = 0
    while total_working_days < WORKING_DAYS and total_emp_hrs < TOTAL_WORKING_HRS:
        random_num = randint(0, 2)
        if random_num:
            working_hrs_dict = {1: 8, 2: 4, 0: 0}
            working_hrs = working_hrs_dict.get(random_num)
        total_emp_hrs += working_hrs
        total_working_days += 1
    monthly_wages = total_emp_hrs * WAGE_PER_HR
    print("Employee's Total Working Hours : ", total_emp_hrs)
    print("Employee's Total Working Days : ", total_working_days)
    print("Employee Wage for Month : ", monthly_wages)


if __name__ == "__main__":
    calculate_wage()
