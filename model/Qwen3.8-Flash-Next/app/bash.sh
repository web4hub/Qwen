# install doc-builder (if not done already)
pip install hf-doc-builder

# you may also need to install some extra dependencies
pip install black watchdog

# run `doc-builder preview` cmd
doc-builder preview hub {YOUR_PATH}/hub-docs/docs/hub/ --not_python_module
