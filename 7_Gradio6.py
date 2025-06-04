import gradio as gr

def favorite_language(language):
    messages = {
        "Python": "Python은 데이터 과학, 웹 개발, AI에 아주 적합한 언어입니다!",
        "JavaScript": "JavaScript는 웹 개발에 강력하며, 프론트엔드와 백엔드에서 모두 사용됩니다.",
        "Java": "Java는 안정성과 성능으로 유명하며, 대규모 시스템에 적합합니다.",
        "C++": "C++는 고성능 애플리케이션과 게임 개발에 자주 사용됩니다."
    }
    return messages.get(language, '선택된 언어에 대한 정보가 없습니다')
# submit을 누르면 language의 key를 입력받아 value를 찾고 get을 통해 그 value의 메세지를 리턴

interface = gr.Interface(
    fn=favorite_language,
    inputs = gr.Radio(['Python', 'JavaScript', 'Java', 'C++'], label='좋아하는 언어'),
    # Radio: 여러가지 중에서 선택할 수 있는 버튼을 보여주는 함수
    outputs = 'text',
    title='좋아하는 언어',
    description='라디오 버튼에서 좋아하는 프로그래밍 언어를 선택하세요'
)

interface.launch()