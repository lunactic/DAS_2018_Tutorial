# DAS2018 Tutorial
This github repository contains all documents, files, etc. necessary for the Tutorial on "Reproducible Research in Document Image Analysis" at the 13th Workshop On Document Analysis Systems (DAS) 2018 in Vienna.

## Presenters
[Marcel Würsch](http://diuf.unifr.ch/main/diva/home/people/marcel-w%C3%BCrsch), [Vinay Chandran Pondenkandath](http://diuf.unifr.ch/main/diva/home/people/vinay-chandran-pondenkandath)

# Introduction
This tutorial is split into two parts: The first part deals with [DIVAServices](http://divaservices.unifr.ch) a RESTful Web Service framework for providing access to Document Image Analysis methods. And the second part with [DeepDIVA]() an Open Source Deep Learning Framework with a focus on reproducibility.

## Tutorial on DIVAServices
The tutorial on DIVAServices itself is also split in two parts: The [first part](01-UseDivaServices/01-UseDivaServices.md) introduces how to use methods provided on DIVAServices, and the [second part](02-InstallMethod/02-InstallMethodOnDivaServices.md) explains how one can provide his/her own method on the platform.

### Pre-Requisites
In order to do the first part of the tutorial you will need the following:

- docker (see: [Docker Installation](https://docs.docker.com/install/), for this purposes the Docker Community Edition is enough)
- python
- Java (>= java 8)
- An account on [Docker Hub](http://hub.docker.com), remember your username as we will need it later for tagging your Docker Image.
- A modern browser (Firefox, Edge, Chrome)
- A decent text editor (e.g. [Visual Studio Code](https://code.visualstudio.com/), [Sublime Text](https://www.sublimetext.com/), [Notepad++](https://notepad-plus-plus.org/))

The allocated time for the tutorial should allow you to complete both parts.
But feel free to spend more time on either of the two tasks if you feel like it.
## Tutorial on DeepDIVA

# Some Words about Docker
As you will see in this tutorial we make extensive use of the Docker platform.
With Docker, you can "virtualize" your application similar to running it within a Virtual Machine, without the necessity of virtualizing the complete system.

Docker uses two main concepts: Images and Container and they are described as follow:
>An **image** is an executable package that includes everything needed to run an application--the code, a runtime, libraries, environment variables, and configuration files.

>A **container** is a runtime instance of an **image**--what the image becomes in memory when executed (that is, an image with state, or a user process). You can see a list of your running containers with the command, `docker ps`, just as you would in Linux.
(source: [docs.docker.com](https://docs.docker.com/get-started/#docker-concepts))

and additionally:
> A container image is a lightweight, stand-alone, executable package of a piece of software that includes everything needed to run it: code, runtime, system tools, system libraries, settings. Available for both Linux and Windows based apps, containerized software will always run the same, regardless of the environment. Containers isolate software from its surroundings, for example differences between development and staging environments and help reduce conflicts between teams running different software on the same infrastructure. 
(source: [docker.com](https://www.docker.com/what-container))

The two following graphics visualize these concepts. The first one shows the Docker approach and the second shows the differences between Docker and traditional Virtual Machines.

![Docker Container](https://www.docker.com/sites/default/files/Package%20software.png)

(source: [docker.com](https://www.docker.com/sites/default/files/Package%20software.png))

![Docker vs Virtual Machines](https://insights.sei.cmu.edu/assets/content/VM-Diagram.png)

(source: [sei.cmu.edu](https://insights.sei.cmu.edu/assets/content/VM-Diagram.png))

We make use of Docker for various reasons.

First of all, it allows us to avoid the [dependency hell](https://en.wikipedia.org/wiki/Dependency_hell). Because every application is encapsulated within its own container it can link to dependencies exactly in the version it needs it to have. This ensoures that the machine where Docker is running on remains clean and we don't need to manually take care of libraries in different versions etc.

Second, Docker provides a very easy way for distributing applications to other machines. You simply need access to the container (usually hosted on [Docker Hub](https://hub.docker.com/), or a private repository) and it can be distributed to any computer running Docker and it will work there. 
Furthermore, Docker scales really well. With [Swarm](https://docs.docker.com/engine/swarm/) it has its own built-in cluster engine.