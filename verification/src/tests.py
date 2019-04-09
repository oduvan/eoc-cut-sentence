"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ["Hi my name is Alex", 8],
            "answer": "Hi my..."
        },{
            "input": ["Hi my name is Alex", 4],
            "answer": "Hi..."
        },{
            "input": ["Hi my name is Alex", 20],
            "answer": "Hi my name is Alex"
        },{
            "input": ["Hi my name is Alex", 18],
            "answer": "Hi my name is Alex"
        }
    ],
    "Extra": [
        {
            "input": ["Hi my name is Alex", 9],
            "answer": "Hi my..."
        },{
            "input": ["Hi my name is Alex", 11],
            "answer": "Hi my name..."
        },{
            "input": ["OMG you did it", 4],
            "answer": "OMG..."
        },{
            "input": ["Hi my name is Alex", 10],
            "answer": "Hi my name..."
        },{
            "input": ["Hi my name is Alex", 1],
            "answer": "..."
        },{
            "input": ["Hi my name is Bartholomew", 22],
            "answer": "Hi my name is..."
        },{
            "input": ["Hello my name is Alex", 2],
            "answer": "..."
        }
    ]
}
