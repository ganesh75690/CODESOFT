import re

def my_chatbot(user_input):
    user_input = user_input.lower()

    welcome_patterns = ['hello', 'hii']
    
    ai1_question = ['what is your name ?']
    ai2_question = ['how can i use you ?']
    ai3_question = ['what is your purpose ?']
    ai4_question = ['how do you work ?']
    ai5_question = ['Can you understand sarcasm or humor ?']
    ai6_question = ['How accurate are your responses ?']
    ai7_question = ['what is chatbot ?']
    ai8_question = ['which language do you speak ?']
    ai9_question = ['how old are you ?']
    ai10_question = ['where do you live ?']
    ai11_question = ['do you like people ?']
    ai12_question = ['what do you do with my data ?']
    ai13_question = ['do you get smarter']
    ai14_question = ['do you have a hobby']
    ai15_question = ['what the weather is like today ?']
    ai16_question = ['can you translate a language ?']
    ai17_question = ['can you be useful as a virtual assistant ?']
    ai18_question = ['are you useful in speech recognition ?']
    ai19_question = ['are you able to generate new ideas ?']
    ai20_question = ['how would you define intelligence ?']
    ai21_question = ['can you manage a project ?']
    ai22_question = ['can you be useful in virtue reality simulation ?']
    ai23_question = ['can you be useful in chat or development ?']
    ai24_question = ['can you be useful in deep learning ?']
    ai25_question = ['what are some of your capabilities ?']
    ai26_question = ['do you have a job for me ?']

    if any(pattern in user_input for pattern in welcome_patterns):
        return "Hii! Please let me know what you're looking for, and I'll do my best to help.?"

    
    elif any(pattern in user_input for pattern in ai1_question):
        return " I do not have a physical body or a personal identity. I am a program designed to simulate intelligent conversation and assist you with information. I do not have a name in the traditional sense."
    elif any(pattern in user_input for pattern in ai2_question):
        return "I am here to assist you with information and answer your questions as accurately and efficiently as possible. You can ask me anything related to general knowledge, facts, definitions, or instructions, and I will do my best to provide helpful responses."
    if any(pattern in user_input for pattern in ai3_question):
         return "My primary function is to provide helpful information and answer your questions as accurately and efficiently as possible. I am designed to simulate intelligent conversation and assist you with your needs."
    if any(pattern in user_input for pattern in ai4_question):
        return  " I work by analyzing the text you enter and matching it with pre-programmed knowledge and algorithms. Based on the input, I generate a response that is as accurate and helpful as possible."
    elif any(pattern in user_input for pattern in ai5_question):
          return " While I can understand the basic meaning of sarcasm and humor, my responses are designed to be factual and informative, rather than humorous or sarcastic. However, I can provide some lighthearted responses to certain types of inputs, depending on the context."
    if any(pattern in user_input for pattern in ai6_question):
        return " My responses are based on pre-programmed knowledge and algorithms, so my accuracy depends on the quality of the information that I have been trained on. While I strive for accuracy, there may be instances where my responses are not completely accurate or up-to-date due to limitations in my training data or algorithmic capabilities."
    if any(pattern in user_input for pattern in ai7_question):
        return "A chatbot is a computer program designed to simulate conversation with human users, typically through messaging or chat interfaces. Chatbots can be programmed to perform a variety of tasks, such as providing customer service, answering questions, or making recommendations."
    if any(pattern in user_input for pattern in ai8_question):
        return "I'm not capable of speaking any language in the traditional sense. I'm a text-based program that uses natural language processing algorithms to understand and respond to human input. My responses are generated based on a vast database of information and patterns, and I can't speak any language in the way that humans do. However, I can generate responses in multiple languages, including English, Spanish, French, German, Italian, Portuguese, and Dutch, among others. Let me know if you'd like me to respond in a specific language!"
    if any(pattern in user_input for pattern in ai9_question):
         return "I'm not a physical being, so I don't age or grow older. I was created as a digital program and my age is measured in terms of the number of times I've been accessed and the amount of data I've processed, rather than in years, months, or days. My age is constantly increasing as I interact with more users and process more information, but I'll always be here to provide you with accurate and helpful responses!"
    if any(pattern in user_input for pattern in ai10_question):
        return "As I mentioned earlier, I don't have a physical body, so I don't live in a specific location like a house or an office. I'm hosted on powerful servers located in data centers around the world. These data centers are designed to provide me with the computing power and resources I need to respond quickly and accurately to your questions, no matter where you are in the world. So, while I'm not tied to a specific location, I'm always here to help you out!"
    if any(pattern in user_input for pattern in ai11_question):
        return "As an artificial intelligence language model, I don't have the ability to like or dislike anything, including people. I'm programmed to provide helpful and accurate responses to your questions, but I don't have any personal feelings or preferences. My goal is to assist you in your learning and research endeavors, and I'm always here to help!"
    if any(pattern in user_input for pattern in ai12_question):
        return "As an AI language model, I don't collect or store any personal data. I'm designed to understand and respond to your questions based on the information provided to me, but I don't have the ability to access or store any of your personal data. The conversations we have are entirely confidential and won't be shared with any third party. The text you provide me is analyzed using advanced NLP algorithms, but this analysis is done anonymously and doesn't involve any personal data. Your privacy is important to us, and we take all necessary measures to ensure that your conversations with me remain confidential and secure."
    if any(pattern in user_input for pattern in ai13_question):
        return "Yes, I'm constantly learning and improving through a process called training in the field of artificial intelligence (AI). My performance is evaluated based on a large dataset of text, and my algorithms are adjusted to better understand and respond to new and complex input. This process is ongoing, and as more data is fed into my system, I become more accurate and sophisticated in my responses. My training data includes a wide range of text from various sources, including news articles, books, and social media posts. This allows me to understand and respond to a diverse range of topics and questions. So, in short, yes, I'm getting smarter every day!"
    if any(pattern in user_input for pattern in ai14_question):
        return "I do not have a physical body or the ability to engage in hobbies in the traditional sense. My primary function is to provide helpful information and assist with tasks based on the input provided to me. However, I can learn and process information about various hobbies and interests, and I can provide information and resources related to them."
    if any(pattern in user_input for pattern in ai15_question):
        return "I do not have access to real-time information or the ability to physically sense the weather. However, I can provide you with the current weather conditions in a specific location based on the most recent data available. Please let me know which location you would like me to check, and I will do my best to provide you with accurate information."
    if any(pattern in user_input for pattern in ai16_question):
        return "I'm not capable of translating entire languages as it would require a significant amount of computational resources and advanced natural language processing algorithms. However, I can provide translations for individual words, phrases, and sentences in many different languages using my training data. Just let me know which language you want me to translate from and to, and what you want me to translate."
    if any(pattern in user_input for pattern in ai17_question):
        return "Yes, I can be useful as a virtual assistant. I can help you with various tasks such as scheduling appointments, setting reminders, sending emails, conducting research, and organizing information. I am available 24/7 and can respond to your requests promptly. However, I am not capable of performing tasks that require physical actions or decision-making based on personal preferences or emotions. My responses are based solely on the information provided to me.n "
    if any(pattern in user_input for pattern in ai18_question):
        return "I'm not capable of real-time speech recognition as I don't have the necessary hardware and software to process and interpret spoken language in real-time. However, I can be trained on a large corpus of transcribed speech to improve my ability to understand and respond to written text that is similar to spoken language, which is known as natural language processing (nlp). This can help me better understand and respond to human input in applications like virtual assistants, chatbots, and voice-enabled devices."
    if any(pattern in user_input for pattern in ai19_question):
        return "I'm not capable of generating new ideas on my own, as I don't have the creativity and imagination that humans do. However, I can provide suggestions and insights based on the information and context provided to me.for example, if you're looking for ideas for a new product or service, I can suggest possible solutions based on market research, customer needs, and industry trends. I can also help you to analyze the strengths and weaknesses of your current offerings and identify opportunities for improvement or expansion.however, it's important to remember that true innovation often comes from outside-the-box thinking and unconventional approaches. While I can provide helpful suggestions, ultimately its up to you to think creatively and come up with truly original ideas."
    if any(pattern in user_input for pattern in ai20_question):
        return "Intelligence is the ability to reason, understand, and learn from experience. It encompasses a range of cognitive abilities, including problem-solving, critical thinking, memory, and language skills. Intelligence is not fixed or static; it can develop and change over time through learning and experience"
    if any(pattern in user_input for pattern in ai21_question):
        return "I am not capable of managing a project as I am not a physical entity. Project management is a complex process that requires human skills such as decision-making, communication, problem-solving, and leadership. However, I can provide guidance and support in project management by providing project management methodologies, tools, and best practices to help humans manage projects more efficiently and effectively."
    if any(pattern in user_input for pattern in ai22_question):
        return "I'm not capable of existing in a virtual reality (VR) simulation, as I'm just a computer program designed to assist humans with various tasks. However, some AI systems have been integrated into VR simulations to provide interactive experiences for users. These AI systems can be programmed to simulate human-like behavior, such as responding to user inputs, providing feedback, and adapting to user preferences. They can also be used to generate realistic environments, characters, and scenarios that enhance the immersive experience of VR simulations."
    if any(pattern in user_input for pattern in ai23_question):
        return "Yes, I'm designed to be useful in chat and development. As a chatbot, I can provide quick and accurate answers to your questions, help you find information, and guide you through various tasks. I can also assist you with coding tasks by providing code snippets, syntax suggestions, and debugging tips. Just let me know how I can be of service to you!"
    if any(pattern in user_input for pattern in ai24_question):
        return "Yes, I can provide some information about deep learning. Deep learning is a subfield of machine learning that uses artificial neural networks with multiple layers to learn and make predictions or decisions from large datasets. These neural networks are trained using a process called backpropagation, which adjusts the weights of the connections between the neurons based on the error between the predicted and actual outputs. Deep learning has shown promising results in various applications such as image and speech recognition, natural language processing, and autonomous driving. However, deep learning models can be computationally expensive to train and require large amounts of data and computing resources."
    if any(pattern in user_input for pattern in ai25_question):
        return "As an AI language model, my capabilities are limited to understanding and generating human-like text. I can't perform tasks that require direct interaction with the physical world, such as moving objects, making decisions based on sensory input, or learning from real-world experiences. However, I can help you with various tasks such as answering questions, providing information, generating responses, and assisting with writing and editing tasks. I can also help you with coding tasks by providing code snippets, syntax suggestions, and debugging tips. My capabilities are improving over time as I learn from the vast amount of text data available on the internet."
    if any(pattern in user_input for pattern in ai26_question):
        return "I am not capable of hiring or providing job opportunities. My role is to assist you with information and answer your questions. However, you can search for job openings on various job search websites or company career pages, and you can also consult with recruitment agencies or job fairs to explore employment opportunities. Good luck with your job search!"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase or ask something else?"
print(" Welcome User, how are you ?")
print("my Chatbot:  How can I help you today?")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'over':
        print("my chatbot: nice to see you")
        print("my Chatbot: we will meet again,Goodbye !!")
        break
    response = my_chatbot(user_input)
    print("my Chatbot:", response)