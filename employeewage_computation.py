from random import randint

WAGE_PER_HR = 20
WORKING_HR = 8
PART_TIME_HR = 4


def calculate_wage():
    check = True if random_num == 1 or random_num == 2 else False
    wage_per_day = 0
    if check:
        print("Employee is Present")
        match random_num:
            case 1:
                wage_per_day = WAGE_PER_HR * WORKING_HR
            case 2:
                print("Employee is Part Time")
                wage_per_day = PART_TIME_HR * WAGE_PER_HR
    else:
        print("Employee is Absent")
    print("Employee Wage Per Day : ", wage_per_day)


if __name__ == "__main__":
    random_num = randint(0, 2)
    calculate_wage()
