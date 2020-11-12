# Reproduce too few inodes issue

Run this script in a container to create a lot of small files to reproduce `no space left on device` error happening due to lack of inodes.

1. Create a new Codefresh pipeline using `exhaust-inodes-pipeline.yaml` definition.
2. Trigger the pipeline.
3. Wait until `Build Docker image` step fails with `no space left on device` error.
