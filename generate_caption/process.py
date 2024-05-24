from transformers import GPT2TokenizerFast, ViTImageProcessor, VisionEncoderDecoderModel
from googletrans import Translator
from PIL import Image
import urllib.request

BN = Translator()
IP = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = GPT2TokenizerFast.from_pretrained("nlpconnect/vit-gpt2-image-captioning")


def show_generate(url, img, greedy=True, translator=BN, image_processor=IP, model=model, tokenizer=tokenizer):
    urllib.request.urlretrieve(url)
    image = Image.open(img)
    # print(image)
    pixel_values = image_processor(image, return_tensors="pt").pixel_values

    if greedy:
        generated_ids = model.generate(pixel_values, max_new_tokens=30)
    else:
        generated_ids = model.generate(
            pixel_values,
            do_sample=True,
            max_new_tokens=30,
            top_k=5)

    generated_text = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    bangla = translator.translate(generated_text, dest='bn')
    return generated_text.capitalize(), bangla.text
