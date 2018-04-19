Salt HAProxy Services Docker
----------------------------


## Get started

1. docker-compose up salt
2. copy the master key that gets generated from ./salt/master/.root_key into the `master_finger:` of the ./salt/minion file `docker-compose exec salt salt-key -F master`
3. docker-compose up haproxy service_a service_a_1 service_b service_b_1
4. exec salt master commands


```
docker-compose up haproxy service_a service_a_1 service_b service_b_1
docker-compose exec haproxy service salt-minion start
docker-compose exec service_a service salt-minion start
docker-compose exec service_a_1 service salt-minion start
docker-compose exec service_b service salt-minion start
docker-compose exec service_b_1 service salt-minion start

docker-compose exec salt salt-key --list all

get unaccepted key

docker-compose exec salt salt-key -a cb49e1ee6d8d

or, accept all

docker-compose exec salt salt-key -A
```

```
docker-compose exec salt salt '*' test.ping
```