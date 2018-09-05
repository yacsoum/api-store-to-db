FROM api-bracelet
RUN apt-get update
RUN wget https://github.com/fabriqueit/26-academy/tree/master/DevOps/Projet2/api-store-to-db/__main__.py
RUN wget https://github.com/fabriqueit/26-academy/tree/master/DevOps/Projet2/api-store-to-db/_version.py
RUN wget https://github.com/fabriqueit/26-academy/tree/master/DevOps/Projet2/api-store-to-db/requirements.txt
RUN mkdir scripts
COPY *.py scripts/
COPY *txt scripts/
CMD -I _main_.py
