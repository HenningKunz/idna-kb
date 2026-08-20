---
title: "Appliance Maintenance and Updates"
weight: 54
date: 2024-07-05
source_confluence_id: 119439619
draft: false
---
It is important to understand the components that make up a panagenda
virtual appliance in order to secure and maintain them properly.

  

### **Base Operating System**

The operating system contained in the virtual appliance is Alma Linux 9.
When a virtual image is packaged and published for download, panagenda
takes great care to update all installed packages to their latest
versions and applies security updates for the operating system. All
passwords are set to default passwords as described in the Setup Guides
for each product.

  

Once the virtual appliance is deployed in the customer environment, the
customer's own network and security teams take control and
responsibility over securing and maintaining the operating system. This
allows you as the customer to apply your own security policies according
to your internal guidelines. It also means you control how and when
which updates are applied to packages installed directly on the
operating system. <u>panagenda application update packages DO NOT
contain updates for the base operating system</u>.  
  

{{% callout type="info" %}}

**panagenda strongly recommends that all default passwords (e.g. Linux
"root" user, Web-UI "config" user) are changed after setup and periodic
security updates for the operating system are enabled!**

{{% /callout %}}

  

The only two services installed on the base operating system that should
be accessible from the network are SSH (port 22) and VNC (port 5901).
While SSH runs constantly, the VNC server is only started on demand for
maintenance that requires a graphical user interface and should be shut
down once the work is completed to minimize a possible attack vector. In
addition, the Docker service will forward ports HTTP (port 80) and HTTPS
(port 443) from the application layer to enable access to the panagenda
application.

  

### **Application Layer**

As part of the Docker infrastructure, panagenda deploys a number of
Docker images and containers that make up the panagenda application.
These containers work together and communicate over Docker-internal
networks that are only accessible within the virtual appliance, except
where ports are exposed by the Docker service (HTTP/HTTPS).

  

panagenda publishes updates for these containers on a regular basis in
the form of application update packages. These packages do not only
contain new features, but also updates for components/services that
provide the base layer for our applications inside the docker containers
(e.g. Container OS, Tomcat, Postgres, etc.). However, application update
packages do not contain updates for the base operating system of the
Alma Linux virtual appliance.

  

  
