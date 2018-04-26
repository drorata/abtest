FROM jupyter/datascience-notebook

RUN mkdir abtest
WORKDIR abtest
COPY abtest/ ./abtest
COPY requirements.txt README.md setup.py ./
# Second part is needed for pymc3 appearing in requirements.txt
RUN pip install -r requirements.txt && conda install mkl-service

# Needed for Thenao
ENV MKL_THREADING_LAYER=GNU

# Remove security from Jupyter!
RUN mkdir ~/.jupyter && \
    echo "c.NotebookApp.token = u''" >> ~/.jupyter/jupyter_notebook_config.py
# Notebooks have the naming patter xy-name_of_notebook.ipynb
COPY ./notebooks/[0-9][0-9]*.ipynb ./notebooks/
CMD /opt/conda/bin/jupyter notebook --ip 0.0.0.0 --no-browser
