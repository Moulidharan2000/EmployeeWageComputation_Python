from random import randint


def employee_check(random_num):
    if random_num == 1:
        print("Employee is Present")
    else:
        print("Employee is Absent")


if __name__ == "__main__":
    random_num = randint(0, 1)
    employee_check(random_num)
