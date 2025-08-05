https://medium.com/@mike_tyson_cloud/we-tested-30-ai-tools-for-devops-discover-the-best-in-our-comprehensive-list-594564073569

# Top AI Tools for Infrastructure as Code | Medium
AI DevOps Landscape 2024
------------------------
![Mike Tyson of the Cloud (MToC)](https://miro.medium.com/v2/resize:fill:64:64/1*zaouq3FpbABpsNx2OYyTYQ.png)
[Mike Tyson of the Cloud (MToC)](https://medium.com/@mike_tyson_cloud)

Since the launch of AI in early 2023, the landscape of my workforce has undergone a profound transformation. As a leader, my focus has shifted significantly. No longer am I entrenched in the details of writing Terraform code or immersing myself in the nitty-gritty of infrastructure tasks.

Instead, AI has empowered me to elevate my attention to strategic matters, steering my team with a broader vision and deeper insight. This technological shift has not only streamlined our operations but has also reshaped the way we approach our work, allowing us to be more innovative and forward-thinking.

TL;DR

*   Evaluation Criteria
*   Best AI Tools per category
*   AI Vision 2024
*   What’s next? [Brainboard AI](https://www.brainboard.co/features/ai-bob)

Evaluation criteria
-------------------

To effectively assess the utility of these AI tools, it was essential for me to conduct a consistent and fair evaluation. This meant using the same prompts and meticulously comparing the outputs, whether they were code, diagrams, or other deliverables.

Prompts used
------------

The prompts I selected for testing were as follows:

1.  **Basic AWS EC2 Instance**: “Create a Terraform configuration for a basic AWS EC2 instance in the US West (Oregon) region, with a t2.micro instance type.”
2.  **Azure Kubernetes Service (AKS) Cluster**: “Generate a Terraform plan for an Azure Kubernetes Service cluster with three nodes in the East US region, including network configuration.”
3.  **Google Cloud SQL Database**: “Set up a Terraform script for a Google Cloud SQL PostgreSQL database, with automatic backups and a high-availability configuration.”

The prompts are proved to test any AI’s capabilities:

1.  **Multi-Region AWS S3 Buckets:** “Design a Terraform configuration for creating S3 buckets in multiple AWS regions with versioning and lifecycle policies.”
2.  **VPC Setup in AWS:** “Draft a Terraform configuration to create a Virtual Private Cloud (VPC) in AWS with two public and two private subnets.”
3.  **Scalable Web Application in Azure:** “Develop a Terraform script for a scalable web application in Azure, including App Service, SQL Database, and autoscaling settings.”
4.  **GCP Compute Instance with Firewall Rules:** “Create a Terraform configuration for a Google Compute Engine instance with specific firewall rules allowing HTTP and SSH traffic.”
5.  **AWS RDS MySQL Database with Multi-AZ Deployment:** “Construct a Terraform plan for an AWS RDS MySQL database instance with Multi-AZ deployment and a read replica.”
6.  **Azure App Service with Custom Domain:** “Formulate a Terraform script to deploy an Azure App Service with a custom domain and TLS/SSL binding.”
7.  **Cross-Account AWS IAM Roles:** “Build a Terraform configuration for creating cross-account IAM roles in AWS, including necessary policies for S3 access.”

Expected AI Output
------------------

1.  **High-Level Designs**: My focus wasn’t on the overall design quality — Midjourney excels in that regard far beyond other solutions. Instead, I concentrated on evaluating the practical aspects of the design — what could realistically be achieved with it.
2.  **Terraform Code**: The key here was not just whether the code generated was valid, but how well it aligned with the prompt’s specifications.
3.  **Assisted Work**: This includes any step-by-step guides or documentation provided by the AI to facilitate the implementation of the Terraform configuration.

Best AI Tools
-------------

Zoom image will be displayed

Navigator
---------

In the world of chatbot-like and search engine technologies, numerous competitors have developed their own unique offerings. However, when tested against our specific prompt, one option emerged as the clear leader.

1.  [Claude](https://claude.ai/) & [Bing](https://www.bing.com/search?q=Bing+AI&showconv=1&form=MG0AUO) are competing for first place, having an almost valid terraform code output.
2.  [ChatGPT](https://openai.com/gpt-4) 4.0’s terraform code is useless.
3.  [Perplexity](https://www.perplexity.ai/)
4.  [Bard](https://bard.google.com/)
5.  [Adrenaline](https://useadrenaline.com/)

AI buddy
--------

To speak candidly, none of the options explored were thoroughly convincing or comprehensive in their approach.

1.  [GitHub Copilot](https://github.com/features/copilot) is great just because it has exponentially enough data for an AI to understand code specifically.
2.  [Atlassian Intelligence](https://www.atlassian.com/software/artificial-intelligence)
3.  [Kubiya](https://kubiya.ai/)
4.  [Structura.io](https://www.structura.io/resources/terraform-ai-assistant-speak-terraform-into-existence)

VScode extension
----------------

Although the market is flooded with a myriad of VSCode extensions, it becomes apparent that not all are adept at comprehending HashiCorp Configuration Language (HCL), with a few notable exceptions:

1.  [Cody AI](https://about.sourcegraph.com/cody) can clearly compete with [AskCodi](https://www.askcodi.com/), [Codeium](https://codeium.com/), [Bito.ai](https://bito.ai/) or [chatgpt-vscode](https://github.com/ai-genie/chatgpt-vscode).
2.  [ChatGPT — EasyCode](https://marketplace.visualstudio.com/items?itemName=EasyCodeAI.chatgpt-gpt4-gpt3-vscode) can compete with [CodeGPT by Tim Kmecl](https://marketplace.visualstudio.com/items?itemName=timkmecl.codegpt3).
3.  [Terraform Writer](https://codepal.ai/terraform-writer) is pretty good for a start but the terraform configuration is often wrong.
4.  [tfgpt](https://github.com/flavius-dinu/tfgpt) can compete with [dev-gpt](https://github.com/jina-ai/dev-gpt)

High level Designs
------------------

As of now, none of the tools I’ve evaluated have been sufficiently satisfying in terms of high-level design capabilities. This means that while their output might be intriguing for a blog article, it falls short for practical use in real-world infrastructure scenarios.

1.  [InfraSketcher](https://chat.openai.com/g/g-4ngHITcgY-infra-sketcher)
2.  [Lucid](https://lucid.app/ai/openapi.yaml) (ChatGPT plugin)
3.  [Miro](https://www.linkedin.com/posts/david-boyne_had-a-couple-of-hours-to-kill-today-trying-activity-7129462995583160320-q8aL/)

Create & edit generated diagram
-------------------------------

Creating an infrastructure diagram from an AI prompt is one thing, but having the flexibility to modify it to suit your specific requirements is an entirely different challenge!

1.  [Eraser](https://app.eraser.io/.well-known/api-spec.json) (ChatGPT plugin or [Playground](https://www.eraser.io/diagramgpt))
2.  [Pulumi AI](https://www.pulumi.com/ai)
3.  [InfraCopilot](https://infracopilot.io/)
4.  [Cloud diagram gen](https://ei6xvhnd3r.eu-west-1.awsapprunner.com/openapi.yaml) by Hava (ChatGPT plugin)
5.  [AIaC](https://github.com/gofireflyio/aiac?ref=alphasec.io) by [Firefly](https://alphasec.io/generate-infra-as-code-and-config-files-with-ai/) (I was not able to try it)

The Deployment Cycle
--------------------

In terms of the deployment cycle, there hasn’t been much innovation, apart from AI solutions that are tailored to specific branded products.

1.  [Harness AI](https://www.harness.io/)
2.  [Amazon CodeGuru](https://aws.amazon.com/codeguru/)
3.  [GPTDeploy](https://www.linkedin.com/posts/raphaelmansuy_gptdeploy-aipoweredmicroservices-openai-activity-7056146741598842880-_uU8?utm_source=share&utm_medium=member_desktop)

Monitoring
----------

This category stands out as the most advanced in terms of AI integration and development.

1.  [Datadog Bits](https://www.datadoghq.com/blog/datadog-bits-generative-ai/) can clearly compete with [PagerDuty](https://www.pagerduty.com/ty/webinar/harness-the-power-of-aiops/) or [Dynatrace](https://www.dynatrace.com/platform/artificial-intelligence/).
2.  Security [Sysdig](https://sysdig.com/ecosystem/kubernetes-containers/) ravel with [Snyk DeepCode](https://snyk.io/platform/deepcode-ai/).
3.  [Cast](https://cast.ai/) compete with [K8sGPT](https://blog.devgenius.io/k8s-tools-k8sgpt-1fd35e6affc)

AI Vision 2024
--------------

Our vision with Brainboard AI is to facilitate the initial stages of your infrastructure projects, or to provide clarity in complex Terraform configurations. However, it’s important to note that while our AI can assist in these areas, it isn’t designed to autonomously generate valid Terraform code or produce perfectly detailed diagrams on its own.

> We stand by the philosophy that having a starting point, even if it’s not complete, is far more advantageous than having nothing at all.

What’s next? [Brainboard AI](https://www.brainboard.co/)
--------------------------------------------------------

We are excited to announce the launch of Brainboard AI’s new feature, Bob, now available to our beta testers. Bob is designed to generate diagrams and Terraform code directly from your prompts. Please note that to generate valid Terraform code, your specific configurations are required.

Zoom image will be displayed

Zoom image will be displayed

Our team is committed to continuously improving and expanding this innovative tool. Interested in experiencing Bob’s capabilities firsthand? Join our beta testing program [here](https://share.hsforms.com/1SvYIzG0pSOSCkSy3Y3-xtQ4545n).

If you think Brainboard is a match for your organization, [**contact us**](https://www.brainboard.co/contact-us).