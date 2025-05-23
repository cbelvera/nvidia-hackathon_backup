# NVIDIA Hackathon – Agent for Legal Precedents in Hate Crime Cases (Spain)

This project converts PDF documents to plain text for use with the NVIDIA's **AgentIQ** toolkit, OCR support with Tesseract, and automated cleaning pipelines. The processed texts are then indexed and retrieved within a Retrieval-Augmented Generation (RAG) system that powers a legal assistant capable of answering questions grounded in real legal case documents.

---

## Project Structure
```
NVIDIA_Hackathon/
├── AIQToolkit/ # External toolkit (cloned from GitHub and modififed for this project)
├── data/
│ ├── input/ # Original PDFs, organized in folders (Capsulas, Jornadas, Jurisprudencia)
│ └── output/ # Cleaned .txt files ready for retrieval
├── utilities/
│ ├── convert_pdfs.py # Extracts text from PDFs (uses OCR if needed)
│ ├── clean_existing_output.py # Cleans headers, footers, and blank lines from .txt files
│ └── validate_clean_output.py # Validates that output files are clean (no headers/footers, no blank lines)
├── run_pipeline.bat # Batch file to automate conversion, cleaning, and validation
├── move_files.sh # File to copy the files into the toolkit
└── README.md # This file
```
---

## Prerrequisits

0) Before you begin using AgentIQ, ensure that you meet the following software prerequisites.

- Install Git

- Install Git Large File Storage (LFS)

- Install uv

1) Clone the AIQToolkit repository. To do so, open the terminal inside the nvidia-hackathon project and run

```bash
git clone https://github.com/NVIDIA/AIQToolkit.git
cd AIQToolkit
```

2) Initialize, fetch, and update submodules in the Git repository.

```bash
git submodule update --init --recursive
```

3) Fetch the data sets by downloading the LFS files.

```bash
git lfs install
git lfs fetch
git lfs pull
```


4) Create a Python environment.

```bash
uv venv --seed .venv
source .venv/bin/activate
```

5) Install the AgentIQ library along with all of the optional dependencies. 

```bash
uv sync --all-groups --all-extras
```


## RAG pipeline

To run the RAG (Retrieval-Augmented Generation) system—whether you're posing a query, running an evaluation, or modifying the data ingestion files—follow the following instructions. This instructions assume that you are already in the AIQToolkit folder.

1) Install the necessary libraries:
    ```bash
    uv pip install -e examples/simple_rag
    ```

2) Move the new scripts inside the simple_rag example project. This file also removes the .git from the AIQToolkit folder.
    ```bash
    ../move_files.sh
    ```

3) Start the docker compose [Skip this step if you already have Milvus running]
    ```bash
    docker compose -f examples/simple_rag/deploy/docker-compose.yaml up -d
    ```

4) Export your NVIDIA API key:
    ```bash
    export NVIDIA_API_KEY=<YOUR API KEY HERE>
    ```

5) Next, execute the `bootstrap_milvus.sh` script as illustrated below.
    ```bash
    scripts/bootstrap_milvus.sh
    ```

6) Run the workflow.
    ```bash
    aiq run --config_file examples/simple_rag/configs/milvus_rag_config.yml --input "¿Qué criterios utiliza el Tribunal Supremo y las Audiencias Provinciales para diferenciar entre un discurso amparado por la libertad de expresión y un discurso que constituye delito de odio según el artículo 510 del Código Penal?"
    ```

7) Evaluate the responses.
   ```bash
   aiq eval --config_file=examples/simple_rag/configs/eval_config.yml
   ```
In order to do so, you have to select in the examples/simple_rag/configs/eval_config.yml file, inside eval/ general/dataset/file_path you have to select the json containing the answer you want to evaluate. In my case, I have created a data folder inside the simple_rag folder in which I have placed 5 different jsons with 5 different questions to evaluate.
The results of the evaluation will appear in a temporal folder inside the AIQToolkit folder.

---


## Pipeline for converting the PDFs to .txt files
### Full automated pipeline for converting the PDFs

To run the entire process of converting the PDFs to .txt files (PDF extraction, cleaning, validation) with one command:

```bash
python run_pipeline.bat
```

This will:
1. Extract text from PDFs (convert_pdfs.py)
2. Clean blank lines (clean_existing_output.py)
3. Validate the output files are ready for retrieval (validate_clean_output.py)

### Manual usage for converting the PDFs
1. Convert PDFs to TXT:
```bash
python utilities/convert_pdfs.py
```
2. Clean .txt outputs:
```bash
python utilities/clean_existing_output.py
```
3. Validate cleaned outputs:
```bash
python utilities/validate_clean_output.py
```   


## OCR (Scanned PDFs)

This project uses [Tesseract](https://github.com/tesseract-ocr/tesseract) and `pdf2image` to handle scanned PDFs.

### On Windows, follow these steps:

1. Install [Tesseract for Windows](https://github.com/UB-Mannheim/tesseract/wiki)
2. Add it to your PATH (e.g. `C:\Program Files\Tesseract-OCR\`)
3. Install Poppler from:  
   https://github.com/oschwartz10612/poppler-windows/releases
4. Add `C:\poppler\Library\bin` to your PATH

---

## Git Ignore

This project properly ignores:

- AIQToolkit

---

## Contact

For any questions, contact the project team.
