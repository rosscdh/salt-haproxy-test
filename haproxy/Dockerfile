FROM haproxy:latest

ADD ./bootstrap-salt.sh /
RUN sh bootstrap-salt.sh

ADD ./entrypoint.sh /
RUN chmod a+x /entrypoint.sh

RUN easy_install pip
RUN pip install haproxyctl

RUN service salt-minion stop

RUN if [ -f /etc/salt/pki/minion/minion.pub ]; then rm /etc/salt/pki/minion/minion.pub; fi
RUN if [ -f /etc/salt/pki/minion/minion.pem ]; then rm /etc/salt/pki/minion/minion.pem; fi
RUN if [ -f /etc/salt/minion_id ]; then rm /etc/salt/minion_id; fi

RUN service salt-minion start

ENTRYPOINT ["/entrypoint.sh"]
CMD ["haproxy", "-f", "/usr/local/etc/haproxy/haproxy.cfg"]