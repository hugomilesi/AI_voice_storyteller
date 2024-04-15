# Voice StoryTeller
![image](https://github.com/hugomilesi/AI_voice_storyteller/assets/71730507/76df2998-48c6-4561-ae3f-9fb7bf6f7728)

Embark on a journey of imagination with Voice StoryTeller. A project that combines cutting-edge AI models to transform your images into captivating audio stories.

Models used:
- [**Salesforce blip-image-captioning-large**](https://huggingface.co/Salesforce/blip-image-captioning-large) with inference API to describe the image.
- [**Google gemini-pro**](https://python.langchain.com/docs/integrations/chat/google_generative_ai/) via LangChain to create a story based on the image description.
- [**Espnet kan-bayashi_ljspeech_vits**](https://huggingface.co/espnet/kan-bayashi_ljspeech_vits) to convert the story to audio.

# Usage

1. Upload Your Image: Choose an image file (JPEG, PNG, etc.) that you want to create a story about. You can select a picture that inspires you, sparks your imagination, or simply piques your interest.
2. After uploading your image, click the "Generate Story" button to start the process. This action will prompt the system to analyze the visual content of your image and craft a narrative based on its interpretation.
3. Once you've clicked the button, give the system a moment to generate the story.
4. After the story has been generated, you'll be presented with the image description and the narrative inspired by the uploaded image. Take your time to read through the story and see how the system interpreted the visual cues in your image.

---

Ready to create your own audio adventures? [**Get started here.**](https://huggingface.co/spaces/hugo-milesi/AI_voice_storyteller)
