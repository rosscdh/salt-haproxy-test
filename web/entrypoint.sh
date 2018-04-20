#!/bin/sh
service salt-minion restart
nginx -g "daemon off;"