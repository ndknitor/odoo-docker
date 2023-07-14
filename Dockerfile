FROM odoo:15
USER root
RUN pip3 install paramiko debugpy pysftp
RUN mkdir -p /var/lib/odoo/sessions && \
    chown -R odoo /var/lib/odoo/sessions && \ 
    chmod +w /var/lib/odoo/sessions &&\
    chown -R odoo /var/lib/odoo 
USER odoo
EXPOSE 8069
COPY odoo-server /app/odoo-server
CMD ["odoo", "/app/odoo-server/odoo-bin" , "--config=/etc/odoo-server.conf"]