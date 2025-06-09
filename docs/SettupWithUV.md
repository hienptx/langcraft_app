## UV INSTALLATION

### Set up uv in linux
```
pip3 isntall uv
git clone .... project_name
cd project_name
uv init
uv add <package> # this will automatically pull .venv
```

#### WSL2 environment
* Create binary file
```
echo 'export PATH="$HOME/.cargo/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```
* Install uv with
```
curl -Ls https://astral.sh/uv/install.sh | bash
```

## PROJECT INITIALIZATION WITH UV

Project LangCraft - UV Setup for Dependency Management

1. Initialize UV project (if not already done)
```
uv init langcraft
cd langcraft
```

2. Add core LangChain
```
uv add langchain
```

3. Add specific integrations (choose what you need)
- OpenAI Integration
```
uv add langchain-openai
```

- Anthropic Integration (for Claude)
```
uv add langchain-anthropic
```

- Google Integration
```
uv add langchain-google-genai
```

- Mistral AI Integration
```
uv add langchain-mistralai
```

- Hugging Face Integration
```
uv add langchain-huggingface
```
- Vector stores (for advanced features later)
```
uv add langchain-chroma
uv add langchain-pinecone
```
- Other useful packages
```
uv add python-dotenv fastapi uvicorn sqlalchemy
```

4. For Jupyter notebook support
```
uv add jupyter ipykernel
```

5. Create virtual environment and activate
```
uv venv
On Windows: .venv\Scripts\activate
On Mac/Linux: source .venv/bin/activate
```

6. Install kernel for Jupyter
```
uv run python -m ipykernel install --user --name=langcraft
```

Your pyproject.toml will look like this:
[project]
name = "langcraft"
version = "0.1.0"
dependencies = [
    "langchain",
    "langchain-openai",
    "langchain-anthropic",
    "python-dotenv",
    "fastapi",
    "uvicorn",
    "jupyter",
]

> [!NOTE]
> Useful information that users should know, even when skimming content.



