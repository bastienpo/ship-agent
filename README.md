<div align="center">

<picture>
    <source media="(prefers-color-scheme: light)" srcset="/docs/logo_fastagent.jpg">
    <img alt="fastagent logo" src="/docs/logo_fastagent.jpg" width="25%" height="25%">
</picture>

**fastagent**: a tool that lets you quickly create FastAPI servers for your DSPy applications

<h3>

[Homepage](https://github.com/bastienpo/fastagent)

</h3>

![GitHub Repo stars](https://img.shields.io/github/stars/bastienpo/fastagent)

</div>

---

The goal of this project is not to create a new AI framework, but to make it easier to ship your application with AI. I find that most of my time is spent trying to set up my server, database, and other dependencies because the incredible AI frameworks make it so easy to build amazing applications. That's why I decided to start this side project.

## Installation

> [!WARNING]
> Work in progress. The project is under active development.

## Usage

## Features

## Roadmap

- [ ] Create the core library that will let you ship your DSPy applications as a FastAPI server
    - [ ] Inference of the dspy pipeline (current focus at the moment, maybe optimization in the future)
    - [ ] Expose the pipeline as a FastAPI endpoint
    - [ ] Simplify best practices for FastAPI (logging, async, etc.)
- [ ] Create the CLI tool to avoid boilerplate code
    - [ ] Use typer and granian to create a server that you can immediately run for development and testing
    - [ ] Generate a docker image for the server
- [ ] Generate the OpenAPI specification for the Agent
    - [ ] Support streaming responses
    - [ ] Add tracing with monitoring tools (langfuse, phoenix, etc.) and posthog for experimentation
    - [ ] Support some kind of authentication and authorization

> [!NOTE]
> The roadmap is not set in stone. It will evolve as we progress. This project is a side project, I just do it for fun. It comes from an observation: that most of the time, the hardest part is to ship the application in production with most of the AI frameworks.

## Resources

This project uses a few other projects, check them out they are great!

- [DSpy](https://github.com/stanfordnlp/dspy)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Granian](https://granian.dev/)
