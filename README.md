# LLM Platform
Open Source LLM Platform that serves as an abstraction layer for both open-source and commercial APIs under a single API scheme

## Getting started
To get started, run:
```
llm-platform start
```

## Platform Architecture
This platform has two main components, a server acting as an abstraction layer over commercial APIs and open-source models and a configuration UI.

### Configuration UI
The configuration UI can be used to enable and configure the commercial APIs that are enabled for users.

In addition the configuration UI can be used to manage the open-source models deployed through the platform.

### Server
The server acts as a serving layer on top of commercial APIs or the hosted open-source models. This server can be configured to log the prompts and responses in a centralised manner for better analysis.