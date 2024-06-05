def filter_factorial(numbers):
        factorials=[1]
        n=max(numbers)
        temp=1
        for i in range(1,n+1):
                temp*=i
                factorials.append(temp)
        return [i for i in numbers if i in factorials]
print(filter_factorial([1,2,3,4,5,6,7,8]))