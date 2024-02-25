import json
import os
import sys
import boto3
from langchain.llms.bedrock import Bedrock
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain import SQLDatabase
from langchain.chains import create_sql_query_chain
from langchain_experimental.sql import SQLDatabaseChain

bedrock=boto3.client(service_name='bedrock-runtime',
                     region_name="us-east-1",
                     aws_access_key_id='',
                     aws_secret_access_key=''
                     )
llm=Bedrock(model_id="amazon.titan-text-express-v1",client=bedrock,
                model_kwargs={})
db = SQLDatabase.from_uri(
    "postgresql+psycopg2://your postgresdb url",
)

QUERY = """
Given an input question, first create a syntactically correct postgresql query to run, then look at the results of the query and return the answer.
Use the following format:

Question: Question here
SQLQuery: SQL Query to run
SQLResult: Result of the SQLQuery
Answer: Final answer here

{question}
"""

# Setup the database chain
db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True)


def get_prompt():
    print("Type 'exit' to quit")

    while True:
        prompt = input("Enter a prompt: ")

        if prompt.lower() == 'exit':
            print('Exiting...')
            break
        else:
            try:
                question = QUERY.format(question=prompt)
                print(db_chain.run(question))
            except Exception as e:
                print(e)

get_prompt()
