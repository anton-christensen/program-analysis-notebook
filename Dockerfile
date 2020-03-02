FROM jupyter/minimal-notebook

USER root

# Install all OS dependencies for fully functional notebook server
RUN apt-get update && apt-get install -yq --no-install-recommends \
    graphviz \
    ghc \
    cabal-install \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN cabal update && cabal install parsec

# make a pip3 symbolic link
RUN /bin/bash -c 'ln -s /opt/conda/bin/pip /opt/conda/bin/pip3'

USER $NB_UID

COPY ./kernels /home/$NB_USER/kernels 

# Install echo kernel
WORKDIR /home/$NB_USER/kernels/echo
RUN ./install.sh

# Install while kernel
WORKDIR /home/$NB_USER/kernels/while
RUN ./install.sh

USER root
WORKDIR /home/$NB_USER/kernels/while/module/while_kernel/hs
RUN ./compile.sh
RUN cp ./WhileParser /usr/bin/WhileParser
RUN apt-get purge -yq ghc cabal-install && apt-get  -yq autoremove && apt-get clean && rm -rf /var/lib/apt/lists/*
USER $NB_UID


# disable 'stupid' tokens
Run echo "c.NotebookApp.token = ''" > /home/$NB_USER/.jupyter/jupyter_notebook_config.py

# create a directory for files people will create through jupyter
RUN mkdir /home/$NB_USER/notebooks
WORKDIR /home/$NB_USER/notebooks


# Switch back to jovyan to avoid accidental container runs as root

# CMD ['bash', "-c", '"echo \"skip; skip;\" | WhileParser"']
CMD ["jupyter", "notebook"]