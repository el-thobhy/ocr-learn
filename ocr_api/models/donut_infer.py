from transformers import DonutProcessor, VisionEncoderDecoderModel
from PIL import Image

processor = DonutProcessor.from_pretrained("naver-clova-ix/donut-base", use_fast=False)
model = VisionEncoderDecoderModel.from_pretrained("naver-clova-ix/donut-base-finetuned-docvqa")

def run_ocr(image: Image.Image):
    task_prompt = "<s_docvqa><s_question>what is shown?</s_question><s_answer>"
    pixel_values = processor(image, return_tensors="pt").pixel_values
    decoder_input_ids = processor.tokenizer(task_prompt, add_special_tokens=False, return_tensors="pt").input_ids
    outputs = model.generate(pixel_values, decoder_input_ids=decoder_input_ids)
    result = processor.batch_decode(outputs, skip_special_tokens=True)[0]
    return {"result": result}
    