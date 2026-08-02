## 1. Git clone this repository

```
git clone https://github.com/cbfbl/run_ai_locally.git
```

## 2. Install UV (python environment manager)

Download and install UV from the offical website

#### Windows
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
#### Mac and Linux
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## 2. Install Ollama

Download and install Ollama from the official website:

https://ollama.com

Follow the installation instructions for your operating system.

## 3. Check Which Models Your System Supports

goto https://www.caniran.ai

Use the site to determine which AI models are supported by your system hardware before downloading or running a model.

## 4. Run a Model Locally

Change the model and prompt in main.py and run the script

```bash
uv run main.py
```
