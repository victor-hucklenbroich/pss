import preprocessor as preproc
import pss
from constants import *
from src import logger, genetics


def compare_to_repo():
    preproc.clean(Path(TEST_PROGRAM_PATH))
    (v0, w0) = pss.compute_features(TEST_PROGRAM_PATH)
    comparisons: [dict] = []
    for p1 in REPO_DATA:
        name: str = p1['name'] + "[" + p1['optimization'] + "]"
        pss_value: float = pss.compare(v0, w0, p1['v'], p1['w'])
        comparison: dict = dict(name=name, pss=pss_value)
        comparisons.append(comparison)

    comparisons.sort(key=lambda c: c.get('pss'))
    for comparison in comparisons:
        logger.log("pss(" + TEST_PROGRAM + "*, " + comparison.get('name') + ") = " + str(comparison.get('pss')),
                   level=1)


if __name__ == '__main__':
    features: (list, list) = find_entry("lua", 0)["v"], find_entry("lua", 0)["w"]
    pop: list = genetics.initial_population(TEST_PROGRAM_PATH, POPULATION_SIZE)
    genetics.evolutionary_cycle(pop, features)
    x = 0
