docker image rm odoo-docker_odoo
docker-compose up -d
docker cp odoo-docker_odoo_1:/usr/lib/python3/dist-packages/odoo - | tar -x
docker cp odoo-docker_odoo_1:/usr/local/lib/python3.9/dist-packages - | tar -x
docker-compose down