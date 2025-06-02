import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  #env 파일을 읽어올 수 있게 해줌

# GPT AI 와 연결하는 함수
client = OpenAI(
    api_key = os.getenv("API_KEY") # API_KEY 변수 이름을 읽어와서 해당 변수에 그 값을 저장
)

# LLM 이용
# temperature: 출력의 무작위성(창의성), 범위 0.0<=x<1.0
# 값이 낮을수록 결정론적, 높을수록 무작위성
# 결정론적: 거의 비슷한 값 (같은 입력->같은 출력), 정답형 질문
# 무작위성: 그때 그때마다 창의적인 답변 (마케팅문구, 스토리 작성)
response = client.chat.completions.create(
    # 모델 선택
    model = "gpt-4.1-2025-04-14",
    messages=[
        {"role":"user","content":"왜 강남은 강남이라고 할까요?"}
    ],temperature=0.0
) 

#print(response)
print(response.choices[0].message.content)
'''
choices[0]항목에서 message -> content 를 읽겠다라는 의미

ChatCompletion(id='chatcmpl-Bdyfi2IKuTaY0Kk3AZJTAqjQ98ZNv', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='"강남"이라는 이름은 한자로 "江南" 
이라고 쓰며, 여기서 "강(江)"은 한강(漢江)을, "남(南)"은 남쪽을 의
미합니다. 즉, "강남"은 "한강의 남쪽"이라는 뜻입니다.\n\n서울의 지
명에서 "강남"은 한강을 기준으로 남쪽에 위치한 지역을 가리키는 말 
로, 1970년대 이후 도시 개발이 본격화되면서 널리 사용되기 시작했습
니다. 특히, 오늘날 "강남"이라고 하면 서울특별시 강남구, 서초구,  
송파구 등 한강 이남의 주요 부유층 거주 지역을 통칭하는 의미로도  
많이 쓰입니다.\n\n정리하자면,  \n**"강남"은 \'한강의 남쪽\'이라는
 뜻에서 유래한 지명**입니다.'
'''