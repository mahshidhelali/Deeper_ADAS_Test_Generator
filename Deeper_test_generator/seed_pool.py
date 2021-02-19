from Deeper_test_generator.problem import Problem
from Deeper_test_generator.member import Member


class SeedPool:
    def __init__(self, problem: Problem):
        self.problem = problem

    def __len__(self):
        raise NotImplemented()

    def __getitem__(self, item) -> Member:
        raise NotImplemented()
