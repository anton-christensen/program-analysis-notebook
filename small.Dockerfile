FROM nbgallery/jupyter-alpine

# install dependencies
RUN apk update && apk add --no-cache \
	graphviz \
    ghc \
    cabal \
    && rm -rf /var/cache/apk/*

# Install parsec dependency
RUN cabal update && cabal install parsec

COPY ./kernels /root/kernels 

# Install echo kernel
WORKDIR /root/kernels/echo
RUN ./install.sh

# Install while kernel
WORKDIR /root/kernels/while
RUN ./install.sh
WORKDIR /root/kernels/while/module/while_kernel/hs
RUN ./compile.sh
RUN cp ./WhileParser /usr/bin/WhileParser


# disable 'stupid' tokens
RUN mkdir -p /root/.jupyter && echo "c.NotebookApp.token = ''" >> /root/.jupyter/jupyter_notebook_config.py

# create a directory for files people will create through jupyter
RUN mkdir /root/notebooks
WORKDIR /root/notebooks
