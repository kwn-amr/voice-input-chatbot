import streamlit as st
import os
from groq import Groq
import random

from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os 
import pyaudio
import wave
import speech_recognition as sr

load_dotenv()

groq_api_key = os.environ['GROQ-API-KEY']

def record_audio(chat_record_length):
    CHUNK = 1024  
    FORMAT = pyaudio.paInt16  
    CHANNELS = 2  
    RATE = 44100  
    RECORD_SECONDS = chat_record_length

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    frames = []

    print("Gravando...")

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Gravação concluída.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    filename = "output.wav"
    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    return filename 

def main():
    st.title("Chatbot com entrada de áudio")

    st.sidebar.title('Selecione uma IA')
    model = st.sidebar.selectbox(
        'Escolha um modelo de IA',
        ['llama-3.1-8b-instant','llama-3.1-70b-versatile','mixtral-8x7b-32768']
    )

    input_type = st.sidebar.selectbox("Escolha o tipo de entrada:", ["Texto", "Áudio"])
    conversational_memory_length = st.sidebar.slider('Comprimento da memória da IA:', 1, 10, value = 5)
    llm_temperature = st.sidebar.slider('Temperatura da IA:',0.0,2.0, value = 0.3, step = 0.1)
    chat_record_length = st.sidebar.slider('Duração da gravação:', 1, 10, value = 5)
    memory=ConversationBufferWindowMemory(k=conversational_memory_length)

    groq_chat = ChatGroq(
            groq_api_key=groq_api_key, 
            model_name=model,
            temperature=llm_temperature
    )

    conversation = ConversationChain(
            llm=groq_chat,
            memory=memory
    )

    if 'chat_history' not in st.session_state:
        st.session_state.chat_history=[]
    else:
        for message in st.session_state.chat_history:
            memory.save_context({'input': message['human']}, {'response': message['AI']})

    if input_type == "Texto":
        user_question = st.chat_input(placeholder="Digite alguma coisa...")
        if user_question:
            response = conversation(user_question)
            message = {'human':user_question,'AI':response['response']}
            st.session_state.chat_history.append(message)
    elif input_type == "Áudio":
        user_question = st.chat_input(placeholder="Digite alguma coisa...")
        if st.button("Gravar Áudio"):
            filename = record_audio(chat_record_length)
            client = Groq(api_key=groq_api_key)
            with open(filename, "rb") as file:
                transcription = client.audio.transcriptions.create(
                  file=(filename, file.read()),
                  model="whisper-large-v3",
                  response_format="json",  # Optional
                  temperature=0.0  # Optional
                )
                transcripted_text = transcription.text
                print(transcripted_text)
                response = conversation(transcripted_text)
                message = {'human':transcripted_text,'AI':response['response']}
                st.session_state.chat_history.append(message)

    chat_container = st.container()   

    for i, message in enumerate(st.session_state.chat_history):
        with chat_container:
            if message['human']:
                with st.chat_message("user"):
                    st.write("Você: " + message['human'])

            if message['AI']:
                with st.chat_message("AI"):
                    st.write(message['AI'])
        
if __name__ == "__main__":
    main()
