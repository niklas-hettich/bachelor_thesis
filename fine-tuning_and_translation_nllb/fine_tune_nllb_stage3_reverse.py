import os
import torch
from datasets import load_dataset
from transformers import (
    AutoTokenizer,
    AutoModelForSeq2SeqLM,
    DataCollatorForSeq2Seq,
    Seq2SeqTrainingArguments,
    Seq2SeqTrainer
)

data_path = "data/stage3_train_data.jsonl"
output_dir = "models/nllb-finetuned-stage3_reverse"

model_name = "facebook/nllb-200-distilled-600M"
source_lang = "deu_Latn" 
target_lang = "zxx_Latn" 

max_length = 128
batch_size = 8
epochs = 3
learning_rate = 2e-5

tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.src_lang = source_lang
tokenizer.tgt_lang = target_lang

model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

raw_dataset = load_dataset("json", data_files={"train": data_path})

def preprocess_function(examples):
    inputs = [ex["de"] for ex in examples["translation"]]
    targets = [ex["hsb"] for ex in examples["translation"]]
    
    model_inputs = tokenizer(
        inputs,
        text_target=targets,
        max_length=max_length,
        truncation=True
    )
    return model_inputs

tokenized_dataset = raw_dataset.map(
    preprocess_function, 
    batched=True, 
    remove_columns=["translation"]
)

data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, model=model)

training_args = Seq2SeqTrainingArguments(
    output_dir=output_dir,
    learning_rate=learning_rate,
    per_device_train_batch_size=batch_size,
    weight_decay=0.01,
    save_total_limit=1,
    num_train_epochs=epochs,
    predict_with_generate=True,
    fp16=True,
    logging_steps=100,
    # save_strategy="epoch",
    save_strategy="no",
    report_to="none"
)

trainer = Seq2SeqTrainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"],
    tokenizer=tokenizer,
    data_collator=data_collator,
)

trainer.train()

trainer.save_model(output_dir)
tokenizer.save_pretrained(output_dir)
print("Done!")