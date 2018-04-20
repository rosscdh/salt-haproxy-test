#!/bin/sh
service salt-minion restart
haproxy -f /usr/local/etc/haproxy/haproxy.cfg