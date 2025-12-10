from Fact import Fact
from typing import List
from clips import Environment

class ClipsInterface:

    __clips_enviroment : Environment = None

    def __init__(self):
        self.__clips_enviroment = self.__charge_rules(Environment())


    def __charge_rules(self, env: Environment) -> Environment:
        env.load("src/myapp/rules/test.clp")
        return env        

    def run_inference(self):
        self.__clips_enviroment.run()

    def actual_facts(self) -> List[Fact]:
        return list(map(lambda f: Fact(f.template.name), self.__clips_enviroment.facts()))

    def insert_new_fact(self, new_fact: Fact):
        self.__clips_enviroment.assert_string(f"({new_fact.value})")
