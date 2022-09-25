import telegram
import time

telegram_config = {}
# config 파일 읽기
with open('/./Academinu_package/Mod/telegram_config', 'r') as f:
    # 모든 줄 읽어오기
    configs = f.readlines()
    # 한 줄씩 확인해서
    for config in configs:
        # 줄바꿈기호 제거(\n) 후 =로 문자열 분리에)
        key, value = config.rstrip().split('=')
        # config 딕셔너리에 키-값 추가
        # key, value로 언패킹 (2개 나올것이 확실하기 때문
        telegram_config[key] = value

token = telegram_config['token']

#봇구동
bot = telegram.Bot(token)
updates = bot.get_updates()

#사용자메시지로부터 ID받아옴
chat_id = updates[-1].message.chat.id
last_id = updates[-1].update_id


# 서버에서 텔레그램 메시지 확인, 응답 보내기
bot.send_message(chat_id, '은평구 아파트 단지 시세조회 시작!\n원하는 동을 입력하세요\n(갈현, 구산, 녹번, 대조, 불광, 수색, 신사, 역촌, 응암, 증산, 진관)')
while True:
    
    try:
        # 신규 메시지가 없을 경우 에러가 발생 
        # list index out of range
        # 따라서, try - except 문으로 묶어줌
        
        new_message = bot.get_updates(offset=last_id)[-1]

        if new_message.message.text == '갈현':
            # 관련 메시지 발송
            bot.send_document(chat_id, open('./Legion/갈현.xlsx', 'rb'))
        
        elif new_message.message.text == '구산':
            bot.send_document(chat_id, open('./Legion/구산.xlsx', 'rb'))

        elif new_message.message.text == '녹번':
            bot.send_document(chat_id, open('./Legion/녹번.xlsx', 'rb'))

        elif new_message.message.text == '대조':
            bot.send_document(chat_id, open('./Legion/대조.xlsx', 'rb'))

        elif new_message.message.text == '불광':
            bot.send_document(chat_id, open('./Legion/불광.xlsx', 'rb'))    

        elif new_message.message.text == '수색':
            bot.send_document(chat_id, open('./Legion/수색.xlsx', 'rb'))

        elif new_message.message.text == '신사':
            bot.send_document(chat_id, open('./Legion/신사.xlsx', 'rb'))

        elif new_message.message.text == '역촌':
            bot.send_document(chat_id, open('./Legion/역촌.xlsx', 'rb'))

        elif new_message.message.text == '응암':
            bot.send_document(chat_id, open('./Legion/응암.xlsx', 'rb')) 

        elif new_message.message.text == '증산':
            bot.send_document(chat_id, open('./Legion/증산.xlsx', 'rb'))
            
        elif new_message.message.text == '진관':
            bot.send_document(chat_id, open('./Legion/진관.xlsx', 'rb'))

         
 
        # offset 값 최신화 (update_id) + 1 해줘서 그 다음부터 메시지부터 확인하도록
        last_id = new_message.update_id + 1
    except:
        pass

    time.sleep(3)



