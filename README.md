![image](https://user-images.githubusercontent.com/31430673/39391654-f88c7d68-4a5b-11e8-843c-480206da5329.png)

# Betty Docker Hackathon 2018

## Docker Hackathon Project for Holberton School

This project was created for Holberton School's 2018 Docker Hackathon. Our task was simply to use Docker to make something.

### Team

- Lee Gaines [<img src="https://user-images.githubusercontent.com/23224088/27935507-4e614b68-6260-11e7-8b20-d0352ef3ff53.png" height="18px"/>](https://twitter.com/eightlimbed)
- Robert Malmstein  [<img src="https://user-images.githubusercontent.com/23224088/27935507-4e614b68-6260-11e7-8b20-d0352ef3ff53.png" height="18px"/>](https://twitter.com/RobertMalmstein)
- Elaine Yeung [<img src="https://user-images.githubusercontent.com/23224088/27935507-4e614b68-6260-11e7-8b20-d0352ef3ff53.png" height="18px"/>](https://twitter.com/egsy)

### Requirements

- [Make](https://www.gnu.org/software/make/)
- [Docker](https://www.docker.com/get-docker) version 18.02.0+

    Check correct version: `docker --version`
- [Docker Compose](https://docs.docker.com/compose/overview/) version 1.21

    Check correct version: `docker-compose --version`

### Installation

```bash
git clone https://github.com/eightlimbed/betty-docker.git
cd betty-docker
make hbtn
```

### Description

Betty Docker aims to create an easier user experience and workflow for Holberton Students. Since students often program on their own machines, Docker provides an ideal solution that allows us to streamline and standardize the set up of Holberton School's development environment. By removing barriers to setup, this project allows students to spend less time setting up tools and more time programming! 💪

### Goal

Dockerize [Betty](https://github.com/holbertonschool/Betty) - Holberton's C code style checker

<!-- Our full project will do the following:

1. Pull the image from Docker on to your local machine.
2. Set up the Betty Docker container.
3. Create an alias for the command "Betty"
    - This command will start the Docker container if it's not started.
    - Send the file to containerized Betty service to process.
    - Run the Betty script on it.
    - Output Betty information.
 -->

#### Stretch Goals and Roadmap

- [x] select base image
- [x] set up automated builds using docker cloud
- [x] write prototype for script
- [x] include PEP8 and Shellcheck using Docker Compose.
- [ ] make Betty Docker a web service.
- [ ] expand social media presence by creating Twitter account
- [ ] livestream team progress
- [ ] create GUI interface for Betty

---

💡 Updates to project will be posted throughout the Hackathon

---

### Usage

### Credits

- [Sid Carroll](sidcarroll7), logo design