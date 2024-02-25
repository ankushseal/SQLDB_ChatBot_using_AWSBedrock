import json
import os
import sys
import boto3
from langchain.llms.bedrock import Bedrock
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

bedrock=boto3.client(service_name='bedrock-runtime',
                     region_name="us-east-1",
                     aws_access_key_id='AKIATCKATT6OKJ7I726R',
                     aws_secret_access_key='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'
                     )
llm=Bedrock(model_id="amazon.titan-text-express-v1",client=bedrock,
                model_kwargs={})
response=llm.invoke("what is capital of india?")
print(response)
