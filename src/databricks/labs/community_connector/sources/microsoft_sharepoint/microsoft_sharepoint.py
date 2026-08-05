from pyspark.sql.types import StructType, StructField, StringType

class LakeflowConnect:
    def __init__(self, options: dict[str, str]) -> None:
        """Initialize connection parameters and API clients here."""
        self.api_token = options.get("api_token", "default_token")

    def list_tables(self) -> list[str]:
        """Defines the tables available for ingestion."""
        return ["sharepoint_documents"]

    def get_table_schema(self, table_name: str, table_options: dict[str, str]) -> StructType:
        """Defines the Spark schema for the destination table."""
        return StructType([
            StructField("id", StringType(), False),
            StructField("file_name", StringType(), True),
            StructField("author", StringType(), True),
            StructField("updated_at", StringType(), True)
        ])

    def read_table_metadata(self, table_name: str) -> dict[str, str]:
        """Defines primary keys, cursors, and the ingestion type."""
        # This is the exact field the user in the forum was trying to update to "snapshot"
        return {
            "primary_keys": ["id"],
            "cursor_field": "updated_at",
            "ingestion_type": "snapshot" 
        }

    def read_table(self, table_name: str, start_offset: str) -> tuple[list[dict], str]:
        """Yields records as dictionaries and returns the next pagination offset."""
        # Mock data extraction
        data = [
            {"id": "doc_1", "file_name": "architecture_v1.pdf", "author": "Shamen", "updated_at": "2026-08-01"},
            {"id": "doc_2", "file_name": "q3_budget.xlsx", "author": "Christian", "updated_at": "2026-08-05"}
        ]
        
        new_offset = "2026-08-05" # In a real scenario, this is dynamically captured from the API
        return data, new_offset