# main.py

import os
import json
from datasets import load_dataset
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    TrainingArguments,
    Trainer,
    DataCollatorForLanguageModeling
)

# ✍️ Dữ liệu huấn luyện mẫu (có thể thay bằng dữ liệu thực tế)
samples = [
    {"prompt": "Hi", "response": "Hello! How can I help you today?"},
    {"prompt": "What's your name?", "response": "I'm your AI assistant."},
    {"prompt": "Tell me a joke", "response": "Why did the computer get cold? Because it forgot to close its Windows."},
    {"prompt": "What is Python?", "response": "Python is a powerful, easy-to-learn programming language."},
    {"prompt": "How are you?", "response": "I'm doing great, thank you!"},
    {"prompt": "Who created you?", "response": "I was built by an awesome developer."},
    {"prompt": "What can you do?", "response": "I can chat with you and help answer questions."},
    {"prompt": "Goodbye", "response": "Goodbye! Have a nice day!"}
]

# 📁 Tạo thư mục data nếu chưa có
os.makedirs("data", exist_ok=True)
data_path = os.path.join("data", "train.json")

# 💾 Ghi file JSON nếu chưa tồn tại
if not os.path.exists(data_path):
    with open(data_path, "w", encoding="utf-8") as f:
        json.dump(samples, f, ensure_ascii=False, indent=2)
    print("✅ Đã tạo file data/train.json")
else:
    print("📁 Đã có file data/train.json, sử dụng lại.")

# 🔄 Load tokenizer và model (dùng distilgpt2 nhẹ, nhanh)
print("🔄 Đang tải tokenizer và mô hình distilgpt2...")
tokenizer = AutoTokenizer.from_pretrained("distilgpt2")

# Sửa lỗi thiếu pad token
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained("distilgpt2")

# 📂 Load và chuẩn hóa dữ liệu
print("📂 Đang load dữ liệu...")
dataset = load_dataset("json", data_files={"train": data_path}, split="train")

def tokenize(example):
    text = f"User: {example['prompt']}\nBot: {example['response']}"
    return tokenizer(text, truncation=True, padding="max_length", max_length=128)

tokenized_dataset = dataset.map(tokenize)

# ⚙️ Thông số huấn luyện
training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=3,
    per_device_train_batch_size=2,
    logging_dir="./logs",
    save_total_limit=1,
    logging_steps=5,
    save_strategy="no"
)

# 🧱 Collator cho causal LM
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

# 🚀 Huấn luyện mô hình
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
    tokenizer=tokenizer,
    data_collator=data_collator
)

print("🚀 Bắt đầu huấn luyện...")
trainer.train()
print("✅ Huấn luyện xong!")

# 💾 Lưu mô hình
save_dir = "trained_model"
model.save_pretrained(save_dir)
tokenizer.save_pretrained(save_dir)
print(f"✅ Mô hình đã lưu tại: {save_dir}/")
