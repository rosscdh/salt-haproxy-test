Salt HAProxy Services Docker
----------------------------


## Get started

1. docker-compose up salt
2. copy the master key that gets generated from ./salt/master/.root_key into the `master_finger:` of the ./salt/minion file
3. docker-compose up haproxy service_a service_a_1 service_b service_b_1
4. exec salt master commands