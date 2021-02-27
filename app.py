import flask_debugtoolbar
from flask import Flask, render_template, redirect, url_for, request, session
from operate import UserLogin, UserRegister, SubmitTest
import json
import config
from flask_login import login_user
from sqlalchemy import create_engine

app = Flask(__name__)

# 配置debugToolbar
app.config['SECRET_KEY'] = 'codeboy'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False  # 不拦截重定向
toolbar = flask_debugtoolbar.DebugToolbarExtension()
toolbar.init_app(app)


@app.route('/login/', methods=('GET', 'POST'))  # 登录
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        data = json.loads(request.get_data(as_text=True))
        response = UserLogin(data['email'], data['pswd'])
        return response


@app.route('/signup/', methods=('GET', 'POST'))  # 登录
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    if request.method == 'POST':
        data = json.loads(request.get_data(as_text=True))
        response = UserRegister(data['username'], data['pswd'], data['email'], data['invitation'])
        return response


@app.route('/read', methods=['GET'])
def read():
    if session.get('userid') is None:
        return redirect(url_for('login'), code=302)
    else:
        data = {
            'name': '现代文阅读',
            'content': '''<div><p>（2017·德州）现代文阅读</p><p align="center">精神明亮的人</p><p 
            align="center">王开岭</p><p>&nbsp;&nbsp;&nbsp; 
            ①十九世纪的一个黎明，在巴黎乡下一栋亮灯的木屋里，居斯塔夫·福楼拜在给最亲密的女友写信:“我拼命工作，天天洗澡，不接待来访，不看报纸，按时看日出(
            像现在这样)。我工作到深夜，窗户敞开，不穿外衣，在寂静的书房里……”</p><p>&nbsp;&nbsp;&nbsp; 
            ②“按时看日出”，我被这句话猝然<u>绊倒</u>了。</p><p>&nbsp;&nbsp;&nbsp; 
            ③一位以“面壁写作”为誓志的世界文豪，一个如此吝惜时间的人，却每天惦记着“日出”，把再寻常不过的晨曦之降视若一件盛事，当作一门必修课来迎对……为什么?</p><p>&nbsp;&nbsp;&nbsp; 
            ④它像一盆水波醒了我，浑身打个激凌。我竭力去想象、去模拟那情景，并久久地揣摩、体味着它……</p><p>&nbsp;&nbsp;&nbsp; 
            ⑤陪伴你的，有刚苏醒的树木，略含咸味的风，玻璃般的草叶，潮湿的土腥味，清脆的雀啼，充满果汁的空气，仍在饶舌的蟋蟀……还有远处闪光的河带，岸边的薄雾，红或蓝的牵牛花，隐隐颤栗的棘条，一两滴被蛐声惊落的露珠，月挂树梢的氤氲，那蛋壳般薄薄的静……</p><p>&nbsp;&nbsp;&nbsp; ⑥从词的意义上说，黑夜意味着堰息和孕育；而日出，则象征着一种诞生，一种升跃和伊始，乃富有动感、饱含汁液和青春性的一个词。它意味着你的生命画册又添置了新的页码，你的体能电池又注入了新的热力。</p><p>&nbsp;&nbsp;&nbsp; ⑦正像分娩决不重复，“日出”也从不重复。它拒绝抄袭和雷同，因为它是艺术，是大自然的最宠爱的一幅杰作。</p><p>&nbsp;&nbsp;&nbsp; ⑧黎明，拥有一天中最纯澈、最鲜泽、最让人激动的光线，那是灵魂最易受孕、最受鼓舞的时刻，那是生命最易受鼓舞、最能添置信心和热望的时刻，也是最让青春荡漾、幻念勃发的时刻。使我们看清了远方的事物，看清了险些忘却的东西，看清了梦想、光阴、生机和道路……</p><p>&nbsp;&nbsp;&nbsp; ⑨迎接晨曦，不仅是感官愉悦，更是精神体验；不仅是人对自然的阅读，更是大自然以其神奇作用于生命的一轮撞击。它意味着一场相遇，让我们有机会和生命完成一次对视，有机会深情地打量自己，获得对个体更细腻、清新的感受。</p><p>&nbsp;&nbsp;&nbsp; ⑩“按时看日出”，乃生命健康与积极性情的一个标志，更是精神明亮的标志。它不仅代表了一记生存姿态，更昭示着一种热爱生活的理念，一种生命哲学和精神美学。</p><p>&nbsp;&nbsp;&nbsp; ⑪透过那橘色晨曦，我触摸到了一幅优美剪影:一个人在给自己的生命举行升旗!</p><p>&nbsp;&nbsp;&nbsp; ⑫在一个普通人的生涯中，有过多少次沐浴晨曦的体验?我们创造过多少这样的机会?</p><p>&nbsp;&nbsp;&nbsp; ⑬仔细想想，或许确有过那么一两回吧。可那又是怎样的情景呢?比如某个刚下火车的凌晨——睡眼惺松，满脸疲态的你，不情愿地背着包，拖着灌铅的腿，被人流推操着，在昏黄的路灯陪衬下，涌向出站口。踩上站前广场的那一刹，一束极细的腥红的浮光突然鱼鳍般游来，吹在你脸上——你倏地意识到:日出了!但这个闪念并没有打动你，你丝毫不关心它……</p><p>&nbsp;&nbsp;&nbsp; ⑭或许还有其它的机会，比如登黄山、游五岳什么的:蹲在人山人海中，蜷在租来的军大衣里，无聊而焦急地看夜光表，熬上一宿。终于，当人群开始骚动，在巨大的欢呼声中，大幕拉开，期待已久的演出来了……然而，这一切都是在混乱、嘈杂、拥挤不堪中进行的，越过无数的后脑勺和下巴，你终于看见了，和预期的一模一样。你会突然惊醒:这是早就被设计好了的，美则美，但就是感觉不对劲儿。</p><p>&nbsp;&nbsp;&nbsp; ⑮而更多的人，或许连一次都没有!一生中的那个时刻，他们无不蜷缩在被子里。他们在昏迷，在蒙头大睡，在<u>冷漠</u>地打着呼噜——第一万次、几万次地打着呼噜。那光线永远照不到他们，照不见那身体和灵魂。</p><p>&nbsp;&nbsp;&nbsp; ⑯放弃早晨，意味着什么呢?意味着你已先被遗弃了。意味着你所看到的世界是旧的，和昨天一模一样的“陈”。仿佛一个人老是吃经年发霉的粮食，永远轮不上新的，永远只会把新的变成旧的。意味着不等你开始，不等你站在起点上，就已被抛至中场，就像一个人未谙童趣即已步入中年。</p><p>&nbsp;&nbsp;&nbsp; ⑰多少年，我都没有因光线而激动的生命清晨了。</p><p align="right">&nbsp;(有删改)</p><p><img src="http://img.51jiaoxi.com/questions/1ac115d0-f969-11e9-b643-cb6effb73675.jpg" v:shapes="图片_x0020_6" width="312" height="247"></p></div>''',
            'exam': [
                {
                    'content': '文章以一封信开头，请分析其作用',
                    'type': 0,
                },
                {
                    'content': '第⑤段想象丰富，用词新颖别致，试举一例简要分析',
                    'type': 0,
                },
                {
                    'content': '解释下面句子中加下划线词语的含义',
                    'type': 1,
                },
                {
                    'content': '“按时看日出”，我被这句话猝然绊倒了',
                    'type': 2,
                },
                {
                    'content': '他们在昏迷，在蒙头大睡，在冷漠地打着呼噜——第一万次、几万次地打着呼噜',
                    'type': 2,
                },
                {
                    'content': '“与福楼拜相比，我们对自然又是怎样的态度呢?”这句话应放在文中哪两段之间，为什么?',
                    'type': 0,
                },
                {
                    'content': '如果你去看日出，会有什么不同于作者的启示?',
                    'type': 0,
                }
            ],
            'examid': 1,
        }
        return render_template('read.html', book=data)


@app.route('/submit_test', methods=['POST'])
def submitTest():
    data = json.loads(request.get_data(as_text=True))
    res = SubmitTest(data['examid'], data['answer'])
    return res


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
