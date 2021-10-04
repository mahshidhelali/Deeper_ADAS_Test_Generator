# Deeper_ADAS_Test_Generator

<a href= "https://ieeexplore.ieee.org/abstract/document/9476240"> **Deeper** </a> [1] is a simulation-based test generator that uses an evolutionary process (i.e., mainly NSGAII) for generating test cases to test a DNN-based lane keeping system in automotive domain. It uses a set of quality population seed to augment the search process effectively with regard to the limited test budget. It has been developed based on DeepJanus Test input generator (https://github.com/testingautomated-usi/DeepJanus/tree/master/DeepJanus-BNG) [2], which is to explore the Frontier of Behaviours for Deep Learning System Testing and is shared under the MIT license. It features enhanced customized objective functions and quality population seed to boost the search process.
The current test generator has been customized for <a href="https://sbst21.github.io/tools/">Cyber-Physical Systems Testing Competition</a> in <a href="https://sbst21.github.io/">SBST 2021</a>. It uses the provided code pipelines by the <a href="https://github.com/se2p/tool-competition-av">competition repository</a>.  

**Installation:**

For the installation of *BeamNG simulator*, please read the <a href="https://github.com/se2p/tool-competition-av/blob/main/documentation/INSTALL.md">installation guide</a> at the Cyber-Physical Systems Testing Competition repository.  

*Python:*

This code has been tested with Python 3.7.

*Other Libraries:*

To easily install the other dependencies with rely on pip, we suggest to create a dedicated virtual environment (we tested venv), activate and run the following command:

pip install -r requirements.txt

Then, please install the additional librararies, stated in "additional-requirements.txt", using the following command:

pip install -r additional-requirements.txt

*Shapely:*

You should download the wheel file matching you Python version, i.e. download the file with cp37 in the name if you use Python 3.7. The wheel file should also match the architecture of your machine, i.e., you should install the file with either win32 or win_amd64 in the name.

**Deeper_Test_Generator:**

The proposed generator has been placed in folder "Deeper Test Generators" and can be exeuted using a script like the following one:

python competition.py --time-budget INTEGER --executor beamng --beamng-home PATH --map-size INTEGER --oob-tolerance FLOAT --module-name Deeper_test_generator.deeper_test_generator --class-name DeeperTestGenerator

(P.S., It uses a set of initial seed population in folder "data -> member_seeds -> Seed_Population". Please do not remove the folder data and note that Deeper does not work with "mock" executor.)

**References:**

[1]. Moghadam, M. H., Borg, M., & Mousavirad, S. J. (2021, May). Deeper at the SBST 2021 tool competition: ADAS testing using multi-objective search. In 2021 IEEE/ACM 14th International Workshop on Search-Based Software Testing (SBST) (pp. 40-41). IEEE.

[2]. Riccio, V., & Tonella, P. (2020, November). Model-based exploration of the frontier of behaviours for deep learning system testing. In Proceedings of the 28th ACM Joint Meeting on European Software Engineering Conference and Symposium on the Foundations of Software Engineering (pp. 876-888).
