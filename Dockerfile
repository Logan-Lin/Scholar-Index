FROM continuumio/anaconda3:latest
ENV PATH /opt/conda/bin:$PATH
ENV ACC "-i https://pypi.tuna.tsinghua.edu.cn/simple"
RUN pip install flask_sqlalchemy ${ACC} && \
    pip install waitress ${ACC} && \
    pip install Markdown ${ACC} && \
    rm -rf ~/.cache/pip
RUN mkdir /workdir
WORKDIR /workdir
COPY . .
EXPOSE 8080
CMD ["waitress-serve", "--call", "index_app:create_app"]