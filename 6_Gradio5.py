import gradio as gr

def add(num1, num2):
    return num1 + num2

interface = gr.Interface(
    fn = add,
    inputs= ['number','number'],
    outputs= 'number',
    title= '계산기',
description= '숫자 두 개를 입력하세요',
flagging_mode = "never"  # falg를 하지 않음
# 하나의 전체적인 화면을 만들때는 인터페이스로 만들기

# submit 버튼을 누르면 add 함수를 호출
)

interface.launch()