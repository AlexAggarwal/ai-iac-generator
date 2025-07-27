def terraform_prompt(user_input):
    return f"""
Generate a Terraform script for the following infrastructure request:
"""
{user_input}
"""
Use Azure provider. Include all necessary resources and variables. Output in HCL.
"""

def diagram_prompt(user_input):
    return f"""
Create a Mermaid diagram representing the architecture for this request:
"""
{user_input}
"""
Use 'graph TD' style and label the components clearly.
"""
