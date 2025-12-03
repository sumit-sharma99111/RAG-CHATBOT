from src.ragchain import build_chain

# ✅ Sample correct questions and expected answers
correct_answers = {
    "What is an NBFC?": "An NBFC is a Non-Banking Financial Company that provides financial services similar to banks but cannot accept demand deposits.",
    "Who regulates NBFCs?": "The Reserve Bank of India regulates NBFCs under the RBI Act, 1934.",
    "Do NBFCs need to get registered with RBI?": "Yes, NBFCs must register with the Reserve Bank of India before commencing business."
}

chain, _ = build_chain(k=4)

print("🔍 Running evaluation...\n")

for question, expected in correct_answers.items():
    try:
        # ✅ Try normal invoke, fallback to direct call if missing
        try:
            response = chain.invoke(question)
        except AttributeError:
            response = chain(question)

        # Extract text cleanly
        answer = (
            response.content.strip()
            if hasattr(response, "content")
            else str(response)
        )

        print(f"❓ Q: {question}")
        print(f"🤖 Bot: {answer}")
        print(f"✅ Expected: {expected}")
        print("-" * 80)

    except Exception as e:
        print(f"⚠️ Error while evaluating '{question}': {e}")
