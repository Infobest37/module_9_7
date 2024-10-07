
def is_prime(func):
    def wrapper(*args, **kwargs):
        num = func(*args, **kwargs)
        j = 1
        for i in range(1, num):

            if num % i == 0:
                j += 1
        if j == 2:
            return(f"Делений: {j} поэтому число - Простое ")
        else:
            return (f"Делений: {j} поэтому число - Составное ")



    return wrapper


@is_prime
def sum_three(*n):
    print(sum(n))
    return sum(n)



result = sum_three(2,3,6)
print(result)