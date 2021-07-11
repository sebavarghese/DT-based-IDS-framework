This is the code repository for my master thesis project titled '**Digital Twin based Intrusion Detection for Industrial Control Systems**'. The main contribution of this work is a security framework for ICS that uses a digital twin of an ICS for security monitoring and has an ML-based IDS for intrusion detection. The digital twin solution used in this work is the framework proposed in 'https://dl.acm.org/doi/10.1145/3407023.3407039' and cloned from the authors' github repo: https://github.com/FrauThes/DigitalTwin-SIEM-integration. 

Folders in this repository (README files are further provided separately for different folders)
1) **DigitalTwin-SIEM-integration**: Cloned from https://github.com/FrauThes/DigitalTwin-SIEM-integration.
Changes made as part of the project are related to:
  (a) Modelling of different process-aware attacks.
  (b) Collecting process measurements & labelling of generated dataset
  (c) Added changes to extend the docker compose framework with a new docker container that will be running ML-based IDS
2) **ML_IDS**: This folder contains Jupyter notebooks for different ML algorithms (Supervised, Stacking) and dataset used to train the models. (FIINNAAL IMPLEMENTATION RUNNING IN IDS???)
3) **Plots:** This folder has plots showing effect of modelled attacks on different process measurements.
4) **siem:** standalone digital twin as a docker container
5) **Makefile**: Run 'make clean' to clean up mininet configurations and log files.
