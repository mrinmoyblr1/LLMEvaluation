from ragas.metrics._context_precision import LLMContextPrecisionWithoutReference


# user_input = Query
# response = response
# reference = Ground Truth (Which we already know)
# retrived_context =>  Top k retrieved docs


def test_context_precision():


# Create objects of the class for the specified matrix
context_precision = LLMContextPrecisionWithoutReference()

# Feed Data
# Get the Score
