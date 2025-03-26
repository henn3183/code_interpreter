# Introduction
The intention of this repository is to simplify the setup of the "Build Your Own Code Interpreter" cookbook example from OpenAI.  For detailed information about the structure and purpose of the components within this repository please refer to [Secure_code_interpreter_tool_for_LLM_agents](./Secure_code_interpreter_tool_for_LLM_agents).

# Getting Started
1) Create a virtual environment in the workspace's root directory:
    `python -m venv ./venv`
2) Activate virtual environment:
    `source ./venv/bin/activate`
3) Install uv:
    `pip install uv`
4) Create the requirements.txt
    `uv export > requirements.txt`
5) Install the requirements:
    `uv pip install -r requirements.txt`
6) Build Docker image:
    `docker build -t python_sandbox:latest ./resources/docker 2>&1`
7) Run Docker image:
    `docker run -d --name sandbox --network none --cap-drop all --pids-limit 64 --tmpfs /tmp:rw,size=64M   python_sandbox:latest sleep infinity`
    Optionally you can include a mount to a local drive to easily retreive file outputs from the model:
    `docker run -d --name sandbox --network none --cap-drop all --pids-limit 64 --tmpfs /tmp:rw,size=64M -v /path/on/host:/path/in/container python_sandbox:latest sleep infinity`
8) Add a .env file with the environment variable `OPENAI_API_KEY`
9) Run the model_entrypoint.py script to kick off the code interpreter tool locally.
    `python ./model_entrypoint.py`

# code_interpreter
Standalone repo for the Object Oriented Agent Approach OPENAI-COOKBOOK example.
