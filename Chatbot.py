# Improved local chatbot using Hugging Face Transformers + Tkinter GUI
# Works offline after the first model download (free!)

import tkinter as tk
from tkinter import scrolledtext
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# ---------------------------------------------------------------
# 1. Load model + tokenizer
#    The 'microsoft/DialoGPT-medium' model gives smoother replies
#    (about 1.2 GB RAM usage).
# ---------------------------------------------------------------
MODEL_NAME = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

# store conversation context for slightly better coherence
chat_history_ids = None

# ---------------------------------------------------------------
# 2. Core function: get bot reply from model
# ---------------------------------------------------------------
def get_reply(user_input):
    global chat_history_ids

    # Encode the new user input, append the <eos> end‑of‑sentence token
    new_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')

    # append tokens to chat history (if any)
    bot_input_ids = torch.cat([chat_history_ids, new_input_ids], dim=-1) if chat_history_ids is not None else new_input_ids

    # generate the model output
    reply_ids = model.generate(
        bot_input_ids,
        max_length=1000,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.75
    )

    # update chat history with new reply
    chat_history_ids = reply_ids

    # decode only the model's newest output tokens
    reply_text = tokenizer.decode(reply_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    return reply_text.strip()

# ---------------------------------------------------------------
# 3. Tkinter GUI
# ---------------------------------------------------------------
def send_message():
    user_input = entry_box.get("1.0", "end-1c").strip()
    if not user_input:
        return
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, f"You: {user_input}\n", "user")
    entry_box.delete("1.0", tk.END)

    try:
        reply = get_reply(user_input)
    except Exception as e:
        reply = f"[Error creating reply: {e}]"

    chat_box.insert(tk.END, f"Bot: {reply}\n\n", "bot")
    chat_box.config(state=tk.DISABLED)
    chat_box.yview(tk.END)

# GUI window
root = tk.Tk()
root.title("Offline AI Chatbot (Improved)")
root.geometry("520x600")
root.configure(bg="#222222")

chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled',
                                     bg="#1e1e1e", fg="white", font=("Helvetica", 12))
chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

entry_box = tk.Text(root, height=3, bg="#333333", fg="white", font=("Helvetica", 12))
entry_box.pack(padx=10, pady=(0,10), fill=tk.X)

send_btn = tk.Button(root, text="Send", command=send_message,
                     bg="#00aa88", fg="white", font=("Helvetica", 12, "bold"))
send_btn.pack(padx=10, pady=10)

root.mainloop()