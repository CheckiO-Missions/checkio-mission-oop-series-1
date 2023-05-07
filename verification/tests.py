checking = """
if not "Car" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Car'?")

if not "my_car" in USER_GLOBAL:
    raise NotImplementedError("Where is 'my_car'?")

if not isinstance(my_car, Car):
    raise Warning("my_car should be an instance of Car class")
"""

TESTS = {
    "Basics": [
        {
        "input": [],
        "answer": None,
        },
    ]
}