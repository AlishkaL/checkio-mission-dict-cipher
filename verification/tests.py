"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": ["hello"],
            "answer":{4: {4: {8: {3: {7: {2: {2: {}}, 0: {4: {}, 7: {}}}, 8: {3: {}}}}}}},

            "explanation": "hello"
        },
        {
            "input": ["This is a plain text."],
            "answer": {1: {3: {2: {1: {4: {7: {6: {8: {1: {}, 4: {}, 9: {}}}, 4: {8: {3: {}}, 4: {9: {}}, 1: {7: {}, 2: {}, 0: {}}}}}, 9: {5: {5: {6: {1: {}, 4: {}}, 8: {}}}}}}}}, 2: {6: {2: {8: {4: {9: {5: {8: {}, 2: {}}}}}}}}, 3: {2: {4: {3: {5: {3: {5: {4: {}, 7: {}}}}}, 1: {4: {8: {3: {2: {}, 0: {}}}}}}}}},
            "explanation": "This is a plain text."
        },
        {
            "input": ["I'm so grateful for your support."],
            "answer": {8: {4: {7: {0: {6: {5: {5: {5: {5: {6: {6: {0: {3: {}, 9: {}}, 8: {9: {}, 7: {}, 2: {}}}, 2: {7: {6: {}, 8: {}}, 2: {0: {}}}}, 8: {3: {7: {4: {}, 7: {}}, 8: {7: {}, 2: {}, 1: {}}}, 7: {4: {5: {}}, 2: {1: {}}, 1: {8: {}}}, 9: {8: {}}}}, 7: {7: {7: {5: {}}, 0: {6: {}}}, 0: {5: {3: {}}, 7: {8: {}}}}}, 2: {1: {4: {1: {8: {}, 1: {}, 0: {}}, 0: {1: {}, 5: {}, 9: {}}}, 5: {0: {1: {}, 0: {}}, 4: {1: {}, 2: {}, 4: {}}}, 7: {2: {1: {}}, 1: {3: {}}, 0: {2: {}}}}}}}}}}}}},

            "explanation": "a little long"
        },
    ],
    "Extra": [
        {
            "input": ["15234928342341098"],
            "answer": {1: {4: {5: {8: {5: {8: {3: {}}}}}, 7: {5: {8: {6: {9: {}}}}}}}, 6: {4: {1: {9: {6: {7: {0: {}}}, 5: {5: {6: {}, 7: {}}, 3: {4: {}}, 1: {4: {}}}}}}, 5: {6: {6: {7: {1: {}, 5: {}}}}}}, 7: {4: {2: {7: {5: {4: {}}, 4: {9: {}}}}}}},
            "explanation": "number"
        },
        {
            "input": ["@;:/.-^."],
            "answer": {4: {2: {3: {0: {6: {5: {}, 6: {}, 9: {}}}}}}, 6: {8: {5: {1: {5: {4: {}}}, 6: {9: {}}}, 7: {3: {1: {}}}}}},
            "explanation": "punctuation"
        }
    ]
}