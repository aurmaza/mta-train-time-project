from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load T5 model and tokenizer
model_name = "t5-small"  # Use 't5-base' or 't5-large' for better quality, but smaller models work well too
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def summarize_article_in_one_sentence(article):
    """
    Summarizes a given article into a single sentence.
    :param article: The full text of the news article
    :return: One-sentence summary
    """
    input_text = "summarize: " + article  # Prefix the article with the 'summarize:' keyword (used in T5 training)
    
    # Tokenize the input text
    inputs = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)

    # Generate a one-sentence summary
    summary_ids = model.generate(inputs, max_length=50, min_length=30, length_penalty=2.0, num_beams=4, early_stopping=True)

    # Decode and return the summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    
    # Limit the output to one sentence (remove any trailing sentences or fragments)
    summary = summary.split('.')[0]  # Take the first sentence
    return summary

# Example usage:
article = "Apple reported record quarterly earnings with a massive increase in iPhone sales despite the global chip shortage..."
summary = summarize_article_in_one_sentence(article)
print("Summary:", summary)
