FROM nginx:mainline

ADD ./bootstrap-salt.sh /
RUN sh bootstrap-salt.sh

RUN service salt-minion stop

RUN if [ -f /etc/salt/pki/minion/minion.pub ]; then rm /etc/salt/pki/minion/minion.pub; fi
RUN if [ -f /etc/salt/pki/minion/minion.pem ]; then rm /etc/salt/pki/minion/minion.pem; fi
RUN if [ -f /etc/salt/minion_id ]; then rm /etc/salt/minion_id; fi

RUN service salt-minion start

CMD ["service", "salt-minion", "restart", "&&", "nginx", "-g", "daemon off;"]