from tensor_flow import TensorFlow


resp = TensorFlow(intents="intent.json")
tag, data = resp.response("goat")
print(data)
