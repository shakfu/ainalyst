import lmstudio as lms

# model = lms.llm() # use current model


# lmstudio server must be running
model = lms.llm("llama-3.2-1b-instruct")

print(model.respond("What the Ruy Lopez opening in chess?"))


