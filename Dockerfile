# 1) choose base container
# generally use the most recent tag


# Base image https://hub.docker.com/u/rocker/
ARG BASE_CONTAINER=ucsdets/datascience-notebook:2020.2-stable
FROM $BASE_CONTAINER
LABEL maintainer="UC San Diego ITS/ETS <ets-consult@ucsd.edu>"

USER root
RUN pip install --no-cache-dir pandas numpy scikit-learn matplotlib seaborn

COPY /run_jupyter.sh /
RUN chmod 755 /run_jupyter.sh
USER $NB_UID

# Override command to disable running jupyter notebook at launch
# CMD ["/bin/bash"]
