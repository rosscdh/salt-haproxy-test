FROM nginx:mainline

ADD ./bootstrap-salt.sh /
RUN sh bootstrap-salt.sh

CMD ["service", "salt-minion", "start"]