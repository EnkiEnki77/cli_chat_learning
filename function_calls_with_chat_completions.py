# Function calling in chat completions API allows to define specific functions the LLM can identify
# and suggest calling when appropriate.
# When a model determines a function should be called, it outputs a formatted json object containing the
# function name and parameters, which can then be executed by the application to perform certain actions
# such as data retrieval.

# Rather than executing functions directly the LLM outputs structured json objects that describe the intended
# function call. The output is then processed by the application to invoke the actual function. Allowing
# controlled interaction between the LLM and external systems.

# Function calls in chat completions  enable:
# 1. Access to external databases and API's for real-time information
# 2. Execution of programmatic operations like scheduling
# 3. Handling of user input with structured responses and reactions

import json
import os
from dotenv import  load_dotenv
from openai import  OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"), base_url=os.getenv("BASE_URL"))

# Acts as database of appointments with their status:
appointment_status = {
    '12345': 'Confirmed',
    '67890': 'Pending',
    '54321': 'Cancelled',
    '98765': 'Completed'
}

# Takes a patient id, and queries db for appointment based on id, returns info about appointment status.
def get_appointment_status(patient_id):
    status = appointment_status.get(patient_id, "No appointment found")
    return status

# List of json objects that define functions for the LLM to pass to the application to be invoked in certain
# situations.
# LLM's determine when a function should be called based on user's input, and the description for the function.

functions_list = [
    {
        "type": "function",
        "function": {
            # Name of the function to be called
            "name": "get_appointment_status",
            # Details about when to call the function
            "description": "Get the appointment status for a patient",
            # Info about the parameters object of the function
            "parameters": {
                "type": "object",
                # Object containing all the parameters and their info
                "properties": {
                    "patient_id": {"type": "string", "description": "The patient ID"},
                },
                # List of the parameters required by the function
                "required": ["patient_id"]
            }
        }
    }
]