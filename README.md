# Wedding web

[![Python](https://img.shields.io/badge/Python-3.11+-yellow?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://python.org)
[![Reflex](https://img.shields.io/badge/Reflex-0.4.3+-5646ED?style=for-the-badge&logo=reflex&logoColor=white&labelColor=101010)](https://reflex.dev)

## Personal frontend web development project with Python for managing the invitations to my wedding

![Picture of the bride and groom.](/assets/images/almendros_.webp)

## Project

As the project's name suggests, I'm getting married this year. And since I didn't want to make paper wedding invitations, I thought about making a website. For this, I've used *[Reflex](https://reflex.dev)*, a modern Python framework that serves to create web pages with few lines of code. Reflex utilizes a UI component library based on *[Radix](https://www.radix-ui.com/)*, to which you can add all the *[CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference)* properties you want.

Let me show you some images of the incredible things that can be done with very few lines of code.

<a href="https://boda-vicky-alex.vercel.app/"><img src="/assets/images/header.webp" alt="Header card image" style="height: 35%; width:35%;"/></a>

The sections are hosted within customized cards with icons, texts, and buttons. For example, the contact card has two buttons that redirect directly to WhatsApp to get in touch with the bride and groom.

<a href="https://boda-vicky-alex.vercel.app/#contact_section"><img src="/assets/images/contact_card.webp" alt="Contact card image" style="height: 35%; width:35%;"/></a>

There's also a card that uses JavaScript to create a countdown to the event date.

<a href="https://boda-vicky-alex.vercel.app/#confirmation_section"><img src="/assets/images/confirmation_card.webp" alt="Confirmation card image" style="height: 35%; width:35%;"/></a>

## How to run the project

To launch the project, you can follow the introduction guide from *[Reflex](https://reflex.dev/docs/getting-started/installation/)* or follow these steps:

### 1. Create the project directory

```cmd
mkdir my_app_name
cd my_app_name
```

### 2. Setup virtual environment

Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows:

```python
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Reflex package

Reflex is available as a pip package.

```python
pip install reflex
```

### 4. Initialize the project

```cmd
reflex init
```

### 5. Run the App

```cmd
reflex run
```

<a href="https://boda-vicky-alex.vercel.app/#confirmation_section"><img src="/assets/images/reflex_run.webp" alt="Reflex run command in CMD" style="height: 75%; width:75%;"/></a>

## Deploy

To deploy the project, I use *[Vercel](https://vercel.com/)*, but you can use the service provided by Reflex (*[you can see the documentation here](https://reflex.dev/docs/hosting/self-hosting/#exporting-a-static-build)*).
In my case, I have automated the deployment process with a GitHub Action following Reflex's instructions when exporting the frontend. If you want to add states and backend, you should review this point as Vercel doesn't play well with Python code (an alternative is *[Railway](https://railway.app/)*).

```sh
python -m pip install --upgrade pip
pip install -r requirements.txt
rm -fr public
isort wedding/
black wedding/
reflex init
reflex export --frontend-only
unzip frontend.zip -d public
rm -f frontend.zip
```

### 💻 [Access the project's code](./wedding)
