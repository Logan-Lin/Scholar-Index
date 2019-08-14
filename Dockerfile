FROM python:3.7.4
ENV PATH /usr/local/bin/:$PATH
ENV ACC "-i https://pypi.tuna.tsinghua.edu.cn/simple"
COPY requirements.txt ./
RUN pip install -r requirements.txt ${ACC} && rm -rf ~/.cache/pip
RUN mkdir /workdir
WORKDIR /workdir
COPY . .
EXPOSE 8080
CMD ["waitress-serve", "--call", "index_app:create_app"]