# Write a function that takes a list of numbers and returns a new list with each number squared.
nums = [1,2,3]

def num_square(nums):
    result = []
    for i in nums:
        result.append(i ** 2)
    return result

print(num_square(nums))

# Create a program that sorts a list of dictionaries by a specified key using a lambda function
students = [
    {"name": "Joshua", "score": 85},
    {"name": "David", "score": 92},
    {"name": "Michael", "score": 78}
]

key = input("Sort by (name/score): ")

sorted_students = sorted(students, key=lambda student: student[key])

print(sorted_students)