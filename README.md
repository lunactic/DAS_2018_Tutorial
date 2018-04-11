# DAS2018 Tutorial
This github repository contains all documents, files, etc. necessary for the Tutorial on "Reproducible Research in Document Image Analysis" at the 13th Workshop On Document Analysis Systems (DAS) 2018 in Vienna.

## Presenters
Marcel Würsch, Vinay Chandran Pondenkandath

# Introduction
This tutorial is split into two parts: The first part deals with [DIVAServices](http://divaservices.unifr.ch) a RESTful Web Service framework for providing access to Document Image Analysis methods. And the second part with [DeepDIVA]() an Open Source Deep Learning Framework with a focus on reproducibility.

## Tutorial on DIVAServices
The tutorial on DIVAServices itself is also split in two parts: The [first part](01-UseDivaServices/01-UseDivaServices.md) introduces how to use methods provided on DIVAServices, and the [second part]((02-InstallMethod/02-InstallMethodOnDivaServices.md)) explains how one can provide his/her own method on the platform.

## Tutorial on DeepDIVA

# Some Words about Docker
As you will see in this tutorial we make extensive use of the Docker platform.
With Docker, you can "virtualize" your application similar to running it within a Virtual Machine, without the necessity of virtualizing the complete system.

Docker calls each virtualized application a Container (see Figure below) and describes them as follows:
 > A container image is a lightweight, stand-alone, executable package of a piece of software that includes everything needed to run it: code, runtime, system tools, system libraries, settings. Available for both Linux and Windows based apps, containerized software will always run the same, regardless of the environment. Containers isolate software from its surroundings, for example differences between development and staging environments and help reduce conflicts between teams running different software on the same infrastructure. [(Source)](https://www.docker.com/what-container#/virtual_machines)

![Docker Container](https://www.docker.com/sites/default/files/Package%20software.png)

We make use of Docker for various reasons.

First of all, it allows us to avoid the [dependency hell](https://en.wikipedia.org/wiki/Dependency_hell). Because every application is encapsulated within its own container it can link to dependencies exactly in the version it needs it to have. This ensoures that the machine where Docker is running on remains clean and we don't need to manually take care of libraries in different versions etc.

Second, Docker provides a very easy way for distributing applications to other machines. You simply need access to the container (usually hosted on [Docker Hub](https://hub.docker.com/), or a private repository) and it can be distributed to any computer running Docker and it will work there. 
Furthermore, Docker scales really well. With [Swarm](https://docs.docker.com/engine/swarm/) it has its own built-in cluster engine.