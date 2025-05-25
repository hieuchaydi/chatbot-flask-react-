from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

print("🔄 Đang tải mô hình từ 'trained_model/'...")
tokenizer = AutoTokenizer.from_pretrained("trained_model")
model = AutoModelForCausalLM.from_pretrained("trained_model")
model.eval()  # chế độ inference

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
    if "Bot:" in response:
        return response.split("Bot:")[-1].strip()
    return response.strip()
