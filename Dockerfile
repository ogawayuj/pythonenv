# ベースイメージ python v3.6 
FROM python:3.6
# USER指定
USER root
# 以降の RUN, CMD コマンドで使われる作業ディレクトリを指定する 今回はcoomposeで指定
WORKDIR /app
ADD ./requirements.txt /app/

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

# vim は一旦外す
#RUN apt-get install -y vim less
#ADD requirements.txt
RUN pip install -r requirements.txt

