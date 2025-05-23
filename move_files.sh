# remove the .git from the AIQToolkit project
rm -rf AIQToolkit/.git

# move the files

cp ../scripts/bootstrap_milvus.sh scripts

cp ../scripts/langchain_web_ingest.py scripts

cp ../scripts/eval_config.yml examples/simple_rag/configs

cp ../scripts/milvus_rag_config.yml examples/simple_rag/configs

cp -r ../scripts/eval_data examples/simple_rag

