FROM mysql:8-debian

# 言語周りの設定
USER root
RUN rm -fR /etc/apt/sources.list.d/* && \
    apt update && \
    apt install -y \
        locales \
        locales-all && \
    echo ja_JP.UTF-8 >> /etc/locale.gen && \
    locale-gen

# 起動時の処理を定義
USER mysql
CMD /entrypoint.sh mysqld \
    --character-set-server=utf8mb4 \
    --collation-server=utf8mb4_unicode_ci