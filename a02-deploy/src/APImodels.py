from pydantic import BaseModel

"""
JSON data Example
{
  "age": 42,
  "job": "entrepreneur",
  "marital": "married",
  "education": "primary",
  "balance": 558,
  "housing": "yes",
  "duration": 186,
  "campaign": 2
}
"""

class Person(BaseModel):
    age: int
    job: str
    marital: str
    education: str
    balance: int
    housing: str
    duration: int
    campaign: int
