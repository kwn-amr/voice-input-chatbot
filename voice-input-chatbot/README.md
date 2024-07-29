
**Aplicativo de chatbot IA com entrada de áudio**
=====================================================

**Introdução**
Esse é um aplicativo de chatbot que permite usuários se comunicar usando entrada de áudio com voz para texto. Esse aplicativo oferece uma maneira mais intuitiva e sem o uso das mãos para interagir com o chatbot.

**Características técnicas**
* Foi criado usando o Streamlit e outras bibliotecas
* USA a API da Groq.com para fazer o processamento da voz, tanto quanto as respostas do chatbot
* Usa o modelo de áudio para texto whisper-v3 da OpenAI para transcrição da fala

**Como o "app" funciona**
O aplicativo usa a entrada de áudio do usuário para gerar texto, que é processado e respondido pela interface de bate-papo. A entrada de áudio é convertida em texto usando o modelo de áudio para texto da OpenAI, e o texto resultante é usado para gerar uma resposta.

**Recursos**
* Interface de bate-papo com as mãos livres usando entrada de áudio
* Reconhecimento e transcrição precisos de fala usando o modelo de áudio para texto da OpenAI
* Processamento de dados dimensionável e eficiente usando a API do Groq
