# -*- coding: utf-8 -*-

#
# inputファイルの内容をDeepL APIで任意の言語に翻訳してoutファイルに出力
#

import datetime
import os

import deepl
from dotenv import load_dotenv
load_dotenv()

def main():
    #
    # settings
    #
    input_file = "./input/input.txt"
    target_lang="EN-US"
    # 現在の日付を取得
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = f"./out/script_{current_time}.txt"
    # 改行を取り除くか
    one_line = False
    #
    # settings
    #

    # Deepl API の準備
    DEEPL_API_KEY = os.getenv("API_KEY")
    translator = deepl.Translator(DEEPL_API_KEY)

    try:
        # 入力ファイルから翻訳前の文字列を取り出す
        with open(input_file, mode="r", encoding="utf-8") as input_file:
             input_text = input_file.read() # 全てのテキストを読み出す
        
        # チャプターファイルを書き込むためのファイルハンドルを開きます
        with open(output_file, mode='w', encoding='utf-8') as output_file:
                # strip():前後の空白を取り除く
                input_text = input_text.strip()
                if one_line:
                    # 改行削除
                    input_text = input_text.replace('\n', '')
                # 翻訳
                translated_text = translator.translate_text(input_text, target_lang=target_lang).text
                # 出力
                print(f'{translated_text}\n')
                output_file.write(f'origin: {input_text}\n')
                output_file.write(f'trans : {translated_text}\n')
                
                print('翻訳が完了しました')

    except FileNotFoundError:
        print(f'エラー: ファイルが見つかりません')
    except IOError:
        print(f'エラー: チャプターファイルを書き込む際にエラーが発生しました。')



if __name__ == "__main__":
    main()

