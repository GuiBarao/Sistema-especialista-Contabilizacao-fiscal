from ClipsInterface import ClipsInterface
from Fact import Fact

clips = ClipsInterface()

clips.insert_new_fact(Fact.UTILIZA_CREDITO)
clips.insert_new_fact(Fact.NAO_PAGOU_TOTAL_DA_FATURA)


clips.run_inference()

facts = clips.actual_facts()
for i in range(len(facts)):
    print(f"{i+1} - {facts[i]}")