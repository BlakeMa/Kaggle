x = True
print(x)
print(type(x))


def can_run_age_present(age):
    return age >= 35


print("your age are great than 35 ", can_run_age_present(20))
print("your age are great than 35 ", can_run_age_present(35))

print(-1 % 2)


def inspect(a):
    if a == 0:
        print("data is ", 0)
    elif a > 0:
        print("data great than", 0)
    elif a < 0:
        print("data less than", 0)
    else:
        print("I cannot understand the data you entered ", x)
inspect(0)
inspect(1)
inspect(-2)
#inspect("Hello")