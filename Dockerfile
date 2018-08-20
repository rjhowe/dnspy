FROM registry.access.redhat.com/rhel7/rhel-tools

COPY dns.py . 
CMD python dns.py
