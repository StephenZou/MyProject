from flask import Flask
from flask import render_template
from flask import request
import text_rank
import summary_embedding

app = Flask(__name__)

summary_embedding = summary_embedding.summary()


@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.route('/analysis')
def analysis():
    #print('服务端数据' + request.args.get('corpus'))
    # rcdata = models.resolve(request.args.get('corpus'))
    # print(rcdata)
    return {'data': [{'person': '赵律师', 'view': '这是一个违法的行为！'}, {'person': '李老师', 'view': '他是一个好学生！'}]}


@app.route('/text_rank_summary')
def text_rank_summary():
    text_info = str(request.args.get('textInfo'))
    summary = ' '.join(text_rank.get_summarization_simple_with_text_rank(text_info))
    return {'summary': summary}


@app.route('/embedding_rank_summary')
def embedding_rank_summary():
    text_info = str(request.args.get('textInfo'))
    summary = ' '.join(summary_embedding.get_summary_simple_by_sen_embedding(text_info))
    return {'summary': summary}


@app.route('/view_analysis', methods=['GET'])
def view_analysis():
    return render_template('view-analytics.html')


@app.route('/comment_analysis', methods=['GET'])
def comment_analysis():
    return render_template('comment-analytics.html')


@app.route('/test', methods=['GET'])
def test():
    return render_template('test.html')


@app.route('/auto_summary', methods=['GET'])
def auto_summary():
    return render_template('auto-summary.html')


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0', port=5001)
