
**Aplicativo de chatbot IA com entrada de áudio**
=====================================================

**Introdução**
Esse é um aplicativo de chatbot que permite usuários se comunicarem usando o microfone. 

**Características técnicas**
* Criado usando o Streamlit e outras bibliotecas
* USA a API da Groq.com para fazer o processamento da voz, tanto quanto as respostas do chatbot
* Usa o modelo de áudio para texto whisper-v3 da OpenAI para transcrição da fala

**Como o "app" funciona**
O aplicativo usa a entrada de áudio do usuário para gravar um trcho que áudio, que em seguida é processado e transformado num prompt que é enviado à IA. 

**Recursos**
* Interface de chatbot simples com opções adicionais no menu lateral
* Transcrição de fala usando o modelo de áudio para texto

**Como usar**
=====================================================
Primeiro baixe os arquivos no seu computador e extraia.
Em seguida abra a pasta numa IDE de código, abra o terminal dentro da IDE e digite o seguinte comando:
```bash
pip install -r requirements.txt
````
Ele irá baixar todos os pacotes inclusos dentro do requirements.txt

Após instalar as dependências necessárias, digite o seguinte comando no seu terminal:
```bash
streamlit run app.py
````
O aplicativo irá abrir em uma nova aba no seu navegador padrão.



