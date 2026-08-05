# Databricks notebook source

import sys
from databricks.labs.community_connector.pipeline import ingest

# Define the pipeline specification
pipeline_spec = {
    # connection_name usually maps to a Databricks Connection object, 
    # but for local mock testing, it acts as a placeholder identifier.
    "connection_name": "mock_sharepoint_conn", 
    "objects": [
        {"table": {"source_table": "sharepoint_documents"}},
    ],
}

# The 'spark' session is implicitly provided by the Databricks environment
ingest(spark, pipeline_spec)