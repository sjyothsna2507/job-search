# from typing import Type
# from pydantic import BaseModel, Field
# # from crewai import tool
# from crewai.tools import tool

# import smtplib
# import json
# from email.mime.text import MIMEText

# class EmailToolInput(BaseModel):
#     """Input schema for EmailTool."""
#     recipient: str = Field(..., description="Email address of the recipient.")
#     subject: str = Field(..., description="Subject of the email.")
#     body: str = Field(..., description="Body content of the email.")

# @tool
# class EmailTool:
#     name: str = "Email Tool"
#     description: str = "Sends an email or saves it as a draft based on the draft_mode flag."
#     args_schema: Type[BaseModel] = EmailToolInput

#     def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str, draft_mode: bool = True, draft_storage: str = 'email_drafts.json'):
#         if not smtp_server or not smtp_port or not username or not password:
#             raise ValueError("SMTP server, port, username, and password must be provided.")

#         self.smtp_server = smtp_server
#         self.smtp_port = smtp_port
#         self.username = username
#         self.password = password
#         self.draft_mode = draft_mode
#         self.draft_storage = draft_storage

#     def _run(self, recipient: str, subject: str, body: str) -> str:
#         if self.draft_mode:
#             return self.save_draft(recipient, subject, body)
#         else:
#             return self.send_email(recipient, subject, body)

#     def send_email(self, recipient: str, subject: str, body: str) -> str:
#         msg = MIMEText(body)
#         msg['Subject'] = subject
#         msg['From'] = self.username
#         msg['To'] = recipient

#         try:
#             with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
#                 server.starttls()
#                 server.login(self.username, self.password)
#                 server.send_message(msg)
#             return "✅ Email sent successfully!"
#         except Exception as e:
#             return f"❌ Error sending email: {e}"

#     def save_draft(self, recipient: str, subject: str, body: str) -> str:
#         draft = {
#             "recipient": recipient,
#             "subject": subject,
#             "body": body
#         }

#         try:
#             with open(self.draft_storage, 'r') as f:
#                 drafts = json.load(f)
#         except FileNotFoundError:
#             drafts = []

#         drafts.append(draft)

#         with open(self.draft_storage, 'w') as f:
#             json.dump(drafts, f, indent=2)
#         return "✅ Draft saved."

# from langchain_community.tools.gmail.create_draft import GmailCreateDraft
# from langchain_community.agent_toolkits import GmailToolkit
# from langchain.tools import tool
# from pydantic import BaseModel, Field
# from typing import List

# class CreateDraftInput(BaseModel):
#     recipient: str = Field(..., description="Email address of the recipient.")
#     subject: str = Field(..., description="Subject of the email.")
#     body: str = Field(..., description="Body content of the email.")

# @tool("Create Draft")
# def create_draft(data: CreateDraftInput):
#     """
#     Creates a draft email in Gmail with the provided recipient, subject, and body.
#     """
#     gmail = GmailToolkit()
#     draft = GmailCreateDraft(api_resource=gmail.api_resource)
#     result = draft({
#         'to': [data.recipient],
#         'subject': data.subject,
#         'message': data.body
#     })
#     return f"Draft created: {result}"
