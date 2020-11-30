# cc-venue
Self hosted open source virtual venue.

## Objetives
The aim of this project is to provide a self-hosted solution for audio/video streamers who want to have full control over the monetization of their streams.

- **Run ticketed streams**: Fixed fee, pay what you want, completely free or even you can run a local advertising network to monetize your channel.
- **Scalable technologies:** The technologic stack used to build this project is made of open source projects that runs in your home computer or a cloud computing solution.

## How it works
The project uses Docker Compose to deploy some containers each providing a functionality

- **Django + PostgreSQL + Gunicorn**: This container runs an HTTP application where the streamer can set up the streams, audience users can register and log in.
- **Icecast server**: This container provides an audio/video streaming server to be the target of the stream source (OBS Studio, VLC, etc) and will provide the media streaming back to the audience.
- **IRC server**: This container works as robust chat backend to be used on the web application. Another container adds bots to control the channels and the users.
- **Jamulus Server**: If we're going full virtual, why not allowing small bands to run a virtual rehearsal place/stage?
