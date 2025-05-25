from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Bước 1: Tải mô hình đã huấn luyện
print("🔄 Đang tải mô hình từ 'trained_model/'...")
tokenizer = AutoTokenizer.from_pretrained("trained_model")
model = AutoModelForCausalLM.from_pretrained("trained_model")
model.eval()  # Đặt chế độ đánh giá

# Bước 2: Hàm chat
def chat_with_bot(user_input, max_length=100):
    prompt = f"User: {user_input}\nBot:"
    inputs = tokenizer(prompt, return_tensors="pt")

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_length=max_length,
            pad_token_id=tokenizer.eos_token_id,
            do_sample=True,
            top_k=50,
            top_p=0.95
        )

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Cắt phần Bot trả lời
    if "Bot:" in response:
        return response.split("Bot:")[-1].strip()
    else:
        return response.strip()

# Bước 3: Vòng lặp hội thoại
print("✅ Mô hình đã sẵn sàng. Nhập 'exit' để thoát.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Bot: Goodbye!")
        break
    reply = chat_with_bot(user_input)
    print("Bot:", reply)
