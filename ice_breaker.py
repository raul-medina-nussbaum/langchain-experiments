import os
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from third_parties.linkedin import scrap_linkedin_profile

if __name__ == "__main__":
    
    summary_template = """
        given the LinkedIn information {information} about a person from I want to create:
        1. a short summary of the person
        2. two interesting fact about them
    """

    summary_prompt_template  = PromptTemplate(input_variables=["information"], template=summary_template)
    
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrap_linkedin_profile()    

    print(chain.run(information=linkedin_data))
