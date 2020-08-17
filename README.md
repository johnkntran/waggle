# Waggle

Welcome to Waggle! This is just a demo repository for setting up a
[Wagtail](https://docs.wagtail.io/en/stable/index.html) site with the following tech stack:

- [Docker](https://docs.docker.com/reference/) as the containerization software
- [NGINX](https://docs.nginx.com/nginx/) as the HTTP proxy server
- [PostgreSQL v9.6](https://www.postgresql.org/docs/9.6/index.html) as the database
- [Redis v5](https://redis.io/commands) as the caching layer
- [Elasticsearch v6](https://www.elastic.co/guide/en/elasticsearch/reference/6.8/index.html) for search


## Getting Started

If you don't have it already, install [Docker Desktop](https://www.docker.com/products/docker-desktop) for your operating system. Make sure the Docker Desktop *daemon* is up and running on your machine.

The site is hosted at [waggle.com](http://waggle.com/). To forward local traffic from NGINX to this domain:
- On **Mac or Linux**, open up the `/etc/hosts` file using a file editor, such as Vim or Nano, in `sudo` mode. Then add the line `127.0.0.1 waggle.com` at the bottom. Save and close the file.
- On **Windows**, open up the `C:\Windows\System32\Drivers\etc\hosts` file using a file editor, such as Notepad. Then add the line `127.0.0.1 waggle.com` at the bottom. Save and close the file.

In the terminal, execute `docker-compose up --build --remove-orphans`.

Once the containers are up and running, we need to create a Django superuser. Run `docker exec -ti web bash` to SSH into the running web container. Then run `python manage.py createsuperuser`, supplying your credentials in the subsequent prompts.

In the your browser, navigate to [waggle.com](http://waggle.com/) (or [http://127.0.0.1:8000](http://127.0.0.1:8000/)) to see the running Wagtail website.

To stop the containers, hit `CTRL + C` on the terminal. Then execute `docker-compose down --remove-orphans` to kill the stopped containers.


## Help

Contact me on GitHub if you need any help!
<br>
[@johnkntran](https://github.com/johnkntran)
