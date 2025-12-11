from typing import List
from clips import Environment

class ClipsInterface:

    __clips_enviroment : Environment = None

    def __init__(self):
        self.__clips_enviroment = self.__charge_rules(Environment())


    def __charge_rules(self, env: Environment) -> Environment:
        env.load("src/myapp/resources/rules/test.clp")
        return env        

    def run_inference(self):
        self.__clips_enviroment.run()

    def actual_facts(self) -> List[str]:
        return list(map(lambda f: f.template.name, self.__clips_enviroment.facts()))

    def insert_new_fact(self, new_fact: str):
        self.__clips_enviroment.assert_string(new_fact)
