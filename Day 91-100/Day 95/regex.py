import re

pattern = r"[a-z]+tual"
text = '''
Ye to misery wisdom plenty polite to as. Prepared interest proposal it he exercise. My wishing an in attempt ferrars. Visited eat you why service looking engaged. At place no walls hopes rooms fully in. Roof hope shy tore leaf joy paid boy. Noisier out brought entered detract because sitting sir. Fat put occasion rendered off humanity has.

Death there mirth way the noisy merit. Piqued shy spring nor six though mutual punctual living ask extent. Replying of dashwood advanced ladyship smallest disposal or. Attempt offices own improve now see. Called person are around county talked her esteem. Those fully these way nay thing seems.

Literature admiration frequently indulgence announcing are who you her. Was least quick after six. So it yourself repeated together cheerful. Neither it cordial so painful picture studied if. Sex him position doubtful resolved boy expenses. Her engrossed deficient northward and neglected favourite newspaper. But use peculiar produced concerns ten.

'''

matches = re.finditer(pattern, text)
for match in matches:
    print(match)