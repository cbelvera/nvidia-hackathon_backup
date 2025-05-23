# remove the .git from the AIQToolkit project
rm -rf AIQToolkit/.git



cp scripts/bootstrap_milvus.sh AIQToolkit/scripts

cp scripts/langchain_web_ingest.py AIQToolkit/scripts

cp scripts/eval_config.yml AIQToolkit/examples/simple_rag/configs

cp scripts/milvus_rag_config.yml AIQToolkit/examples/simple_rag/configs

cp -r scripts/eval_data AIQToolkit/examples/simple_rag

