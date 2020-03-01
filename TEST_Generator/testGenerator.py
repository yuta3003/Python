# -*- coding: utf-8 -*-
import random

capitals = {#  '問題':'正解',
            '関係演算の射影の説明として，適切なものはどれか。':'表の中から指定された属性だけを抜き出して，新しい表を作る。',
            'キューに関する記述として，最も適切なものはどれか。':'最初に格納されたデータが最初に取り出される。',
            '負数を2の補数で表すとき，すべてのビットが1であるnビットの2進数"1111…11"が表す数値又はその数式はどれか。':'－1',
            'DFDの説明はどれか。':'適用業務をデータの流れに注目して視覚的に表現したもの',
            'USBの特徴はどれか。': '三つのデータ転送モードがあり，ハイスピードモードは外付け磁気ディスクなどの接続に使用される。', 
            'レーザプリンタの性能を表す指標として，最も適切なものはどれか。': '1インチ(2.54cm)当たりのドット数と1分間に印刷できるページ数', 
            'システム監査規程の最終的な承認者はだれか。': '経営者', 
            'IPv4においてIPアドレスからMACアドレスを取得するために用いるプロトコルはどれか。': 'ARP', 
            'コンパイラにおける最適化の説明として，適切なものはどれか。': 'プログラムコードを解析して，実行時の処理効率を高めたオブジェクトコードを生成する。', 
            'Javaのアプリケーションプログラムがデータベースにアクセスするための標準的なAPI(Application Program Interface)はどれか。': 'JDBC', 
            'プロジェクトのリスクに対応する戦略として，損害発生時のリスクに備え，損害賠償保険に加入することにした。PMBOKによれば，該当する戦略はどれか。': '転嫁', 
            'モジュールテストで使用されるドライバ又はスタブの機能に関する記述のうち，適切なものはどれか。': 'ドライバはテスト対象モジュールに引数を渡して呼び出す。',
            '当期の建物の減価償却費を計算すると、何千円になるか。ここで建物の取得価格は10,000円, 前期までの減価償却累計額は3,000千円であり、償却法は定額法会計期間は1年間, 太陽年数は20年間とする。':'500',
            '斜線や曲線に生じるギザギザを目立たなくする技術をなんというか.':'アンチエイリアシング'
            }

# 問題集と解答集の作成
quiz_file = open('FEtest.txt', 'w', encoding='utf-8')
answer_file = open('FEanswer.txt', 'w', encoding='utf-8')

# 問題の順番をシャッフル
fequestion = list(capitals.keys())
random.shuffle(fequestion)

# リストをループしてそれぞれ問題を作成する
for question_num in range(len(fequestion)):
    # 正解と誤答を取得する

    # 正当のindexを取得
    correct_answer = capitals[fequestion[question_num]]
    # 辞書の値を全て取得しリスト化
    wrong_answers = list(capitals.values())
    # リストから正解を削除
    del wrong_answers[wrong_answers.index(correct_answer)]
    # 誤答リストからランダムに3つ取得
    wrong_answers = random.sample(wrong_answers, 3)
    # 3つの誤答と正解を選択肢リストとする
    answer_option = wrong_answers + [correct_answer]
    # 選択肢リストをシャッフル
    random.shuffle(answer_option)

    # 問題文と回答選択肢を問題ファイルに書く
    quiz_file.write('{}. {}\n'.format(question_num + 1, fequestion[question_num]))
    logging.debug('{}. {}\n'.format(question_num + 1, fequestion[question_num]))

    for i in range(4):
        quiz_file.write(' {}. {}\n'.format('ABCD'[i], answer_option[i]))
        logging.debug(' {}. {}\n'.format('ABCD'[i], answer_option[i]))

    quiz_file.write('\n')

    answer_file.write('{}. {}\n'.format(question_num + 1, 'ABCD'[answer_option.index(correct_answer)]))

quiz_file.close()