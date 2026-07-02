from core import generate_reply

message = input("Enter message: ")

reply = generate_reply(message)

print("\nGenerated Reply:\n")
print(reply)