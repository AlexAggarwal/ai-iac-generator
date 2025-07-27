from fastapi import FastAPI, Request
from pydantic import BaseModel
import openai
import os
from prompts import terraform_prompt, diagram_prompt

app = FastAPI()
openai.api_key = os.getenv("OPENAI_API_KEY")

class InfraRequest(BaseModel):
    natural_language: str

@app.post("/generate")
async def generate_iac(req: InfraRequest):
    user_input = req.natural_language

    # Generate Terraform
    terraform_response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an expert DevOps engineer generating production-grade Terraform code."},
            {"role": "user", "content": terraform_prompt(user_input)}
        ]
    )
    terraform_code = terraform_response.choices[0].message.content

    # Generate Mermaid Diagram
    diagram_response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a cloud architect who explains cloud infrastructure visually."},
            {"role": "user", "content": diagram_prompt(user_input)}
        ]
    )
    diagram_code = diagram_response.choices[0].message.content

    # Save to files (optional)
    os.makedirs("output", exist_ok=True)
    with open("output/main.tf", "w") as f:
        f.write(terraform_code)
    with open("output/diagram.mmd", "w") as f:
        f.write(diagram_code)

    return {"terraform": terraform_code, "mermaid": diagram_code}