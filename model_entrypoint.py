from resources.registry.agents.file_access_agent import FileAccessAgent
from resources.registry.agents.python_code_exec_agent import PythonExecAgent


prompt = """Use the file co_high_temps.json for your analysis.
The JSON data represents daily high temperature values in Fahrenheit for a specific location. The structure of the JSON data is as follows:
data: This key contains an array of objects. Each object represents a location and its associated daily high temperature values.
meta: This key contains metadata about the location.

uid: A unique identifier for the location.
ll: An array representing the latitude and longitude of the location.
sids: An array of station identifiers associated with the location.
state: The state where the location is situated.
elev: The elevation of the location in feet.
name: The name of the location.
data: This key stores an array of daily high temperature values in Fahrenheit. Each element in the array is a sub-array containing a single string value representing the temperature for each day of the year in 2024.

Here is an example of an entry from the json data:
{
    "data": [
        {
            "meta": {
                "uid": 18,
                "ll": [
                    -107.76023,
                    37.1431
                ],
                "sids": [
                    "93005 1",
                    "052433 2",
                    "DRO 3",
                    "KDRO 5",
                    "USW00093005 6",
                    "USW00093005 32"
                ],
                "state": "CO",
                "elev": 6629.0,
                "name": "DURANGO LA PLATA COUNTY AP"
            },
            "data": [
                [
                    "44"
                ],
                [
                    "45"
                ],
                ...
            ]
        }
    }
}   
"""

print("Setup: ")
print(prompt)

print("Setting up the agents... ")

# Instantiate the agents with the default constructor defined values
# Developer may override the default values - prompt, model, logger, and language model interface if needed

# This agent use gpt-4o by default
file_ingestion_agent = FileAccessAgent()

# Let's make sure agent uses o3-mini model and set the reasoning_effort to high
#data_analysis_agent = PythonExecAgent(model_name='o1-mini', reasoning_effort='high')
data_analysis_agent = PythonExecAgent(model_name='gpt-4o-mini')


print("Understanding the contents of the file...")
# Give a task to the file ingestion agent to read the file and provide the context to the data analysis agent 
file_ingestion_agent_output = file_ingestion_agent.task(prompt)

# Add the file content as context to the data analysis agent
# The context is added to the agent's tool manager so that the tool manager can use the context to generate the code 

data_analysis_agent.add_context(prompt)
data_analysis_agent.add_context(file_ingestion_agent_output)

while True:

    print("Type your question related to the data in the file. Type 'exit' to exit.")
    user_input = input("Type your question.")

    if user_input == "exit":
        print("Exiting the application.")
        break

    print(f"User question: {user_input}")

    print("Generating dynamic tools and using code interpreter...")
    data_analysis_agent_output = data_analysis_agent.task(user_input)

    print("Output...")
    print(data_analysis_agent_output)
