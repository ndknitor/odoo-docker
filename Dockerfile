FROM odoo:15
USER root
RUN apt-get update && apt-get upgrade -y
# Install custom module here
RUN pip3 install --upgrade google-api-python-client httpagentparser
RUN apt install -y git
##################################
RUN pip3 install debugpy
RUN groupadd docker
RUN apt update && apt upgrade -y
RUN mkdir -p /var/lib/odoo/sessions && \
    chown -R odoo /var/lib/odoo/sessions && \ 
    chmod +w /var/lib/odoo/sessions &&\
    chown -R odoo /var/lib/odoo && \ 
    chown -R odoo /etc/odoo
RUN chown :docker /mnt/extra-addons
USER odoo:docker