<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<br />
<div align="center">
  <a href="#">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Jenkins Bot</h3>

  <p align="center">
    Jenkins bot is the product of a will to provide automations to my team using discord and jenkins to create easy to use/mantain automations.
    <br />
    <a href="https://github.com/fulviocoelho/jenkins-bot/issues">Report Bug</a>
    ·
    <a href="https://github.com/fulviocoelho/jenkins-bot/issues">Request Feature</a>
  </p>
</div>


## About The Project

[![Product Name Screen Shot][product-screenshot]](https://github.com/fulviocoelho/jenkins-bot)

Jenkins bot is a small project that focus on delivery a functional integration between jenkins and discord. This interface should be able to make it easy and mantainable automations used on daily bases accessible on discord.

The integration was also planned to have a friendly communication with the user, making the project close to a real discord bot but more flexible.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python.py]][Python-url]
* [![Jenkins][Jenkins]][Jenkins-url]
* [![Docker][Docker]][Docker-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

To get a local copy up and running follow these simple example steps.
1. Clone the repo
   ```sh
   git clone https://github.com/fulviocoelho/jenkins-bot.git
   ```
2. Install NPM packages
   ```sh
   yarn
   ```
3. Install husky package (NPM) - Only needed if you want to use Git
   ```sh
   yarn husky install
   ```

### Prerequisites

To run SIR you will need to have installed Python and NodeJs with yarn installed (NPM Package). Here is an example of how to install those softwares:
* npm
  ```sh
  yum install npm nodejs
  ```
* yarn
  ```sh
  npm install yarn -g
  ```
* python
  ```sh
  yum install python3
  ```
* docker
  ```sh
  yum install docker-ce docker-ce-cli containerd.io docker-compose-plugin
  ```

## Usage

This project has two executions types, one that counts with a single pod containing a the basic pyton scripts and jenkins with template pipelines for commands, the second is the basic pod with basic python scripts and jenkins and other pods to enable graphana graphs.

To start the bot you will need to configure environment variables at the docker composer file. Docker file will be at `/docker/basic-bot/docker-compose.yaml` and `/docker/bot+sre/docker-compose.yaml`.

### Start Pod

To start the pod build the image first, to do that run the following command: `yarn build`. 

To start the bot use `yarn docker-up:basic` or `yarn docker-up:sre`.

### Configuration

| parameter | values | description |
| --- | --- | --- |
| CLANID | string | the server id that will be bind to bot |
| COMMAND | string | the command used to call bot |
| ME | string | account id connected at bot  |
| TOKEN | string | discord access token |
| DEBUGLOG | boolean | if true will print more logs about the discord connection |

### Creating Commands

To create a command you must create a jenkins job, you may use the templates available, if you want to send a message you could copy the `./Templates/template-speak`, if you want more steps you could use `./Templates/pipeline-template`.

### Using Commands

To call a command that has been created on discord you can send a message on the server binded to the bot or directly to the account binded to the bot.

All commands expect the parameters `AUTHOR` and `CHANNEL`, those are passed on by the python script. All other parameters must be passed down on the message sended to the bot.

A message to trigger a bot command should be as `{{COMMAND}} {{jenkins_job}} {{PARAMETER}}={{value}}&{{PARAMETER}}={{value}}`. So a command can be something o the lines of: `/bot hello` or `/bot run-e2e application=internal&type=full_test`

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Customizing Your Bot

To customize the connection or process present on bot you could change pipelines on jenkins or at the python files: `/docker/image/bot/listen.py` or `/docker/image/bot/speak.py`.

The **listen** file is responsable to connect to discord using *websockets* to watch over discord notification and messages on the configure account.

The **speak** file is responsable to connect to discord and send messages using HTTP requests.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact

Fulvio Coelho - contato@fulviocoelho.dev

Project Link: [https://github.com/fulviocoelho/jenkins-bot](https://github.com/fulviocoelho/jenkins-bot)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/fulviocoelho/jenkins-bot.svg?style=for-the-badge
[contributors-url]: https://github.com/fulviocoelho/jenkins-bot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/fulviocoelho/jenkins-bot.svg?style=for-the-badge
[forks-url]: https://github.com/fulviocoelho/jenkins-bot/network/members
[stars-shield]: https://img.shields.io/github/stars/fulviocoelho/jenkins-bot.svg?style=for-the-badge
[stars-url]: https://github.com/fulviocoelho/jenkins-bot/stargazers
[issues-shield]: https://img.shields.io/github/issues/fulviocoelho/jenkins-bot.svg?style=for-the-badge
[issues-url]: https://github.com/fulviocoelho/jenkins-bot/issues
[license-shield]: https://img.shields.io/github/license/fulviocoelho/jenkins-bot.svg?style=for-the-badge
[license-url]: https://github.com/fulviocoelho/jenkins-bot/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/fulvio-coelho
[product-screenshot]: images/screenshot_vscode.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Python.py]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Node.js]: https://img.shields.io/badge/Node.js-43853D?style=for-the-badge&logo=node.js&logoColor=white
[Jenkins]: https://img.shields.io/badge/Jenkins-D33833?style=for-the-badge&logo=jenkins&logoColor=white
[Docker]: https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white
[AWS]: https://img.shields.io/badge/Amazon_AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white
[Next-url]: https://nextjs.org/
[Python-url]: https://www.python.org/
[Node-url]: https://nodejs.org/en/
[Jenkins-url]: https://www.jenkins.io/
[Docker-url]: https://www.docker.com/
[AWS-url]: https://aws.amazon.com/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
