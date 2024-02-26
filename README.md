**README**

## Querying SQLDB in Natural Language with Bedrock

This repository contains a Python script for interacting with a SQL database using conversational queries powered by Bedrock, an AI model from AWS.

### Prerequisites

Before running the script, ensure you have the following dependencies installed:

- Python 3.x
- `boto3`

You can install the dependencies via pip:

```bash
pip install boto3
```

### Configuration

Ensure you have configured your AWS credentials properly. You can set up your AWS credentials using AWS CLI or directly in the script.

### Usage

1. Clone the repository:

```bash
git clone https://github.com/your-username/conversational-sql-query.git
cd SQLDB_ChatBot_using_AWSBedrock
```

2. Update the AWS credentials and database URL in the script.

3. Run the Python script `main.py`:

```bash
python main.py
```

### Description

This script allows users to interact with a PostgreSQL database using natural language queries. It utilizes Bedrock, an AI model from AWS, to understand and execute SQL queries based on user prompts.

### Input

Users can input natural language prompts such as questions or commands to retrieve information from the database.

### Output

The script generates SQL queries based on user prompts, executes them against the PostgreSQL database, and returns the results. It provides a conversational interface for querying the database.

### Contributing

Contributions are welcome! If you have suggestions, feature requests, or bug fixes, please feel free to open an issue or create a pull request.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Acknowledgements

- [boto3](https://github.com/boto/boto3) - AWS SDK for Python.
- [AWS Bedrock](https://aws.amazon.com/bedrock/) - AI model for natural language understanding and generation.
- [SQLAlchemy](https://www.sqlalchemy.org/) - Python SQL toolkit and Object-Relational Mapper.
